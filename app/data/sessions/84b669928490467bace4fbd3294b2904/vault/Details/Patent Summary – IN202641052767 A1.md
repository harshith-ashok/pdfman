---
title: "Patent Summary – IN202641052767 A1"
date: 2026-05-08
patent_number: IN202641052767 A1
tags: [patent, digital-memory, agentic-system]
---

# 📄 Patent Summary – IN202641052767 A1  

## Chunk Overview  
This section details an Indian patent application (IN202641052767 A1) filed on 25 April 2026, titled **“Agentic system for contextual digital memory reconstruction using multi‑source activity correlation.”** The invention proposes a background‑running digital assistant that aggregates activity logs from disparate platforms, correlates them through temporal, semantic, and behavioural analyses, and synthesizes a coherent, timeline‑based narrative of a user’s past digital experiences. By presenting this reconstructed memory through an interactive interface, the system aims to improve recall, productivity, and overall human‑computer interaction.

---

## 1. Bibliographic Information [[Bibliographic Information]]  

- **Publication No:** IN202641052767 A1  
- **Filing Date:** 25‑04‑2026  
- **Publication Date:** 08‑05‑2026 (Journal No 19/2026)  
- **Applicant(s):**  
  - **Srm Institute Of Science And Technology, Ramapuram Campus**  
  - **Easwari Engineering College**  
- **Inventor(s):** Harshith Ashok, R Krishnan, Dr. M.S. Bennet Praba  
- **International Classification:**  
  - `G06F 17/30` – Interaction techniques  
  - `H04L 12/58` – Retrieval of stored data  
  - `G06Q 10/10` – Business data processing, e.g., workflow management  
  - `G06F 17/27` – Interaction with a user or a system for input manipulation  
  - `G06F 16/951` – Information extraction; Information retrieval  

---

## 2. Core Problem Addressed [[Core Problem Addressed]]  

- **Document‑centric retrieval limitations**  
  - Existing systems rely heavily on explicit identifiers such as keywords, filenames, participants, or timestamps.  
  - Users often remember only **high‑level situational cues** (e.g., “the morning I discussed the project with the team while browsing research papers”) rather than exact search terms.  

- **Fragmented digital traces**  
  - Daily interactions span **email, documents, browsers, social media, and app logs**, producing disjoint activity logs that are hard to piece together.  

- **Inadequate reconstruction mechanisms**  
  - Traditional keyword search, static filters, or single‑service history views cannot **re‑assemble an episodic experience** from scattered traces.  

---

## 3. Inventive Solution – High‑Level Overview [[Inventive Solution – High-Level Overview]]  

- **Agentic architecture**  
  - A suite of **autonomous software agents** runs persistently in the background, collecting activity fragments from multiple digital sources.  

- **Multi‑source correlation**  
  - The **correlation engine** applies three complementary analyses:  
    - `temporal proximity analysis` – Detects events occurring close together in time.  
    - `semantic similarity modelling` – Computes meaning‑level overlaps between content (e.g., email subject vs. document title).  
    - `behavioural pattern inference` – Learns user‑specific habits (e.g., opening a PDF right after a calendar reminder).  

- **Event‑graph construction**  
  - Correlated fragments are organized into a **structured event graph** that visualizes relationships among actions, applications, and information objects.  

- **Narrative synthesis**  
  - The **reconstruction engine** traverses the event graph to generate a **coherent, timeline‑based narrative** reflecting the user’s experience.  

- **Interactive recall interface**  
  - Users can **inspect**, **refine**, and **expand queries** adaptively, receiving a readable story rather than a list of isolated documents.  

- **Privacy‑by‑design**  
  - All activity data is stored **locally on the user’s personal computer** unless the user explicitly configures remote storage.  

---

## 4. Detailed System Components [[Detailed System Components]]  

### 4.1. Autonomous Agents [[Autonomous Agents]]  

- **Data collection agents**  
  - Continuously harvest logs from:  
    - Email clients (`SMTP`, `IMAP` stores)  
    - Document repositories (file system, cloud‑sync folders)  
    - Web browsers (history, tabs, cookies)  
    - Application logs (e.g., IDE, multimedia tools)  

- **Context‑analysis agents**  
  - Extract metadata (timestamps, participants, file types) and perform lightweight NLP to capture **semantic cues**.  

### 4.2. Correlation Engine  

- **Temporal proximity analysis** (`temporal proximity analysis`)  
  - Groups events within configurable time windows (e.g., ±5 minutes) to infer possible **single episodes**.  

- **Semantic similarity modelling** (`semantic similarity modelling`)  
  - Utilizes vector‑space embeddings (e.g., BERT, FastText) to quantify meaning overlap between textual artifacts.  

- **Behavioural pattern inference** (`behavioural pattern inference`)  
  - Applies machine‑learning classifiers to detect recurring user sequences (e.g., “open calendar → join video call → open meeting notes”).  

- **Output** – Produces a **weighted edge list** linking nodes (events) in the event graph, where edge weights reflect combined temporal‑semantic‑behavioural confidence.  

### 4.3. Event Graph  

- **Node types**  
  - **Communication** (emails, chat messages)  
  - **Document** (files, PDFs, slides)  
  - **Web activity** (pages visited, searches)  
  - **Application usage** (IDE sessions, media playback)  

- **Edge semantics**  
  - Temporal adjacency, semantic similarity score, behavioural correlation flag.  

- **Visualization**  
  - Interactive graph view with zoomable timeline, filterable by node/edge type, and searchable captions.  

### 4.4. Narrative Synthesis Engine  

- Traverses the event graph using depth‑first or heuristic‑guided paths to construct human‑readable sentences (e.g., “At 09:12 AM, you opened the project proposal PDF after receiving an email from R Krishnan confirming the meeting schedule.”).  

- Supports **user‑driven refinement**: users can merge, split, or reorder events to tailor the story.  

### 4.5. User Interface  

- **Dashboard** – Overview of recent reconstructed episodes.  
- **Search pane** – Accepts natural‑language cues (“the day I prepared the budget”) and maps them to graph substructures.  
- **Privacy controls** – Toggle local‑only mode, selective source inclusion, and data expiration policies.  

---  

*End of note.*