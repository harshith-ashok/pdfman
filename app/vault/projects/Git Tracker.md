Git Tracker is a local dashboard for monitoring and managing many git repositories from a single place. It is designed for folder structures like `Dev/<Language>/<Project>/repo/...` and gives you a fast overview of repo health, recent commits, remotes, and quick git actions.

## What It Does

- Scans a root development folder that you choose at runtime
- Finds nested repositories by walking downward until a `.git` directory is present
- Keeps the highest matching git folder when nested repos overlap
- Shows repositories in a two-column dashboard on larger screens
- Displays branch, remote URL, latest commit, commit date, and working tree status
- Lets you run `git add .`, `git commit`, and `git push` from the dashboard
- Provides the same git controls on each repo detail page
- Renders the repository README on a dedicated detail view
- Includes a custom GitHub activity panel built from recent public push events

## Stack

- Vue 3
- Vue Router
- Tailwind CSS v4
- GSAP
- Express
- `simple-git`

## Project Structure


## Local Development

Install dependencies:

```bash
npm install
```

Start the frontend and API together:

```bash
npm run dev
```

Default local ports:

- Frontend: `http://localhost:5173`
- API: `http://localhost:4174`


## How Repo Detection Works

The scanner searches downward from the chosen root folder for `.git` directories. Every matching parent folder is treated as a candidate repository. If one detected repo sits inside another detected repo, the app keeps only the highest valid git root so the same project is not shown multiple times.

## GitHub Activity Panel

The GitHub section is based on recent public `PushEvent` data from the GitHub API. It renders:

- A native 35-day heatmap
- A lightweight push trend chart

Because this data comes from recent public events, it is best-effort and does not represent your full private or historical contribution graph.

## Notes

- This app is meant to run locally because it needs direct filesystem access and permission to execute git commands.
- Large development folders will take longer to scan.
- Git actions use the local machine state of each repository exactly as it exists on disk.