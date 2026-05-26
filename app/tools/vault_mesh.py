from __future__ import annotations

import os
import re
from dataclasses import dataclass


APP_DIR = os.path.dirname(
    os.path.dirname(__file__)
)
VAULT_PATH = os.path.join(APP_DIR, "vault")
CONNECTED_SECTION = "## Connected Notes"
MAX_SECTION_LINKS = 12


@dataclass
class NoteRecord:
    path: str
    title: str
    frontmatter: str
    body: str
    tags: set[str]
    existing_links: set[str]


def mesh_vault_notes(vault_path: str = VAULT_PATH) -> dict[str, object]:
    notes = _load_notes(vault_path)

    if not notes:
        return {
            "vault_path": os.path.abspath(vault_path),
            "processed_files": 0,
            "updated_files": 0,
            "links_added": 0
        }

    title_map = {
        note.title.casefold(): note.title
        for note in notes
    }

    related_map = _build_related_map(notes)

    updated_files = 0
    links_added = 0

    for note in notes:
        new_body, body_links_added = _link_note_body(
            note=note,
            title_map=title_map
        )

        connected_titles = _choose_connected_titles(
            note=note,
            related_map=related_map
        )

        final_body, section_links_added = _upsert_connected_section(
            body=new_body,
            connected_titles=connected_titles
        )

        total_added = body_links_added + section_links_added

        if final_body != note.body:
            with open(note.path, "w", encoding="utf-8") as handle:
                handle.write(note.frontmatter + final_body)

            updated_files += 1

        links_added += total_added

    return {
        "vault_path": os.path.abspath(vault_path),
        "processed_files": len(notes),
        "updated_files": updated_files,
        "links_added": links_added
    }


def _load_notes(vault_path: str) -> list[NoteRecord]:
    records: list[NoteRecord] = []

    for root, dirnames, filenames in os.walk(vault_path):
        dirnames[:] = [
            dirname
            for dirname in dirnames
            if dirname != ".obsidian"
        ]

        for filename in filenames:
            if not filename.endswith(".md"):
                continue

            path = os.path.join(root, filename)

            with open(path, "r", encoding="utf-8") as handle:
                content = handle.read()

            frontmatter, body = _split_frontmatter(content)
            title = _extract_title(content, filename)
            tags = _extract_tags(frontmatter)
            existing_links = set(_extract_wikilinks(content))

            records.append(
                NoteRecord(
                    path=path,
                    title=title,
                    frontmatter=frontmatter,
                    body=body,
                    tags=tags,
                    existing_links=existing_links
                )
            )

    return records


def _split_frontmatter(content: str) -> tuple[str, str]:
    if not content.startswith("---\n"):
        return "", content

    marker = "\n---\n"
    closing_index = content.find(marker, 4)

    if closing_index == -1:
        return "", content

    frontmatter = content[:closing_index + len(marker)]
    body = content[closing_index + len(marker):]

    return frontmatter, body


def _extract_title(content: str, filename: str) -> str:
    title_match = re.search(
        r"(?m)^title:\s*(.+?)\s*$",
        content
    )

    if title_match:
        return _strip_quotes(title_match.group(1).strip())

    heading_match = re.search(
        r"(?m)^#\s+(.+?)\s*$",
        content
    )

    if heading_match:
        return heading_match.group(1).strip()

    return os.path.splitext(filename)[0]


def _extract_tags(frontmatter: str) -> set[str]:
    tags: set[str] = set()

    if not frontmatter:
        return tags

    for match in re.findall(r"(?m)^\s*-\s+(.+?)\s*$", frontmatter):
        cleaned = _strip_wikilink(_strip_quotes(match.strip()))
        if cleaned:
            tags.add(cleaned.casefold())

    return tags


def _extract_wikilinks(content: str) -> list[str]:
    links = []

    for raw in re.findall(r"\[\[([^\]]+)\]\]", content):
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.append(target)

    return links


def _build_related_map(notes: list[NoteRecord]) -> dict[str, dict[str, int]]:
    related_map: dict[str, dict[str, int]] = {}

    for note in notes:
        this_key = note.title.casefold()
        related_map[this_key] = {}

        note_tokens = _title_tokens(note.title)

        for other in notes:
            other_key = other.title.casefold()

            if this_key == other_key:
                continue

            score = 0

            if other.title in note.existing_links:
                score += 6

            shared_tags = note.tags & other.tags
            score += len(shared_tags) * 3

            shared_tokens = note_tokens & _title_tokens(other.title)
            score += len(shared_tokens)

            if score > 0:
                related_map[this_key][other.title] = score

    return related_map


def _link_note_body(
    note: NoteRecord,
    title_map: dict[str, str]
) -> tuple[str, int]:
    body = note.body
    links_added = 0

    candidates = sorted(
        (
            title
            for key, title in title_map.items()
            if key != note.title.casefold()
        ),
        key=len,
        reverse=True
    )

    code_fence_open = False

    updated_lines = []

    for line in body.splitlines():
        stripped = line.strip()

        if stripped.startswith("```"):
            code_fence_open = not code_fence_open
            updated_lines.append(line)
            continue

        if code_fence_open or "[[" in line:
            updated_lines.append(line)
            continue

        new_line = line

        for candidate in candidates:
            if candidate.casefold() in note.existing_links:
                continue

            pattern = re.compile(
                rf"(?<!\[\[)(?<![A-Za-z0-9])({re.escape(candidate)})(?![A-Za-z0-9])"
            )

            new_line, replacements = pattern.subn(
                rf"[[\1]]",
                new_line,
                count=1
            )

            if replacements:
                note.existing_links.add(candidate)
                links_added += replacements

        updated_lines.append(new_line)

    return "\n".join(updated_lines), links_added


def _choose_connected_titles(
    note: NoteRecord,
    related_map: dict[str, dict[str, int]]
) -> list[str]:
    scores = related_map.get(
        note.title.casefold(),
        {}
    )

    ranked = sorted(
        scores.items(),
        key=lambda item: (-item[1], item[0].casefold())
    )

    return [
        title
        for title, _score in ranked[:MAX_SECTION_LINKS]
    ]


def _upsert_connected_section(
    body: str,
    connected_titles: list[str]
) -> tuple[str, int]:
    if not connected_titles:
        return body, 0

    section_body = "\n".join(
        f"- [[{title}]]"
        for title in connected_titles
    )

    new_section = f"{CONNECTED_SECTION}\n\n{section_body}\n"
    pattern = re.compile(
        rf"\n{re.escape(CONNECTED_SECTION)}\n(?:.*\n?)*$",
        re.DOTALL
    )

    section_links_added = len(connected_titles)

    if CONNECTED_SECTION in body:
        updated = pattern.sub(f"\n{new_section}", body.rstrip() + "\n")
        return updated.rstrip() + "\n", 0

    updated = body.rstrip() + "\n\n" + new_section
    return updated, section_links_added


def _title_tokens(title: str) -> set[str]:
    return {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9]+", title)
        if len(token) > 2
    }


def _strip_wikilink(value: str) -> str:
    match = re.fullmatch(r"\[\[([^\]]+)\]\]", value)
    if not match:
        return value

    return match.group(1).split("|", 1)[0].strip()


def _strip_quotes(value: str) -> str:
    return value.strip("\"'")
