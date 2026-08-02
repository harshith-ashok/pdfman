---
title: Bibliographic Information – IN202641052767 A1
source: Details.pdf
date: 2026-05-08
tags:
  - patent
  - bibliographic
related:
  - [[Patent Summary – IN202641052767 A1]]
  - [[Core Problem Addressed]]
  - [[Inventive Solution – High-Level Overview]]
  - [[Detailed System Components]]
  - [[Autonomous Agents]]
---

# 📄 Patent Summary – IN202641052767 A1  

## 1. Bibliographic Information  

- **Publication No:** IN202641052767 A1  
- **Filing Date:** 25‑04‑2026  
- **Publication Date:** 08‑05‑2026 (Journal No 19/2026)  
- **Applicant(s):**  
  - Srm Institute Of Science And Technology, Ramapuram Campus  
  - Easwari Engineering College  
- **Inventor(s):** Harshith Ashok, R Krishnan, Dr. M.S. Bennet Praba  
- **International Classification:**  
  - `G06F 17/30` – Interaction techniques  
  - `H04L 12/58` – Retrieval of stored data  
  - `G06Q 10/10` – Business data processing, e.g., workflow management  
  - `G06F 17/27` – Interaction with a user or a system for input manipulation  
  - `G06F 16/951` – Information extraction; Information retrieval  

## 2. Core Problem Addressed  

- **Document‑centric retrieval limitations**  
  - Reliance on explicit identifiers (keywords, filenames, timestamps).  
  - Users often recall only high‑level situational cues.  

- **Fragmented digital traces**  
  - Interactions span email, documents, browsers, social media, and app logs, producing disjoint logs.  

- **Inadequate reconstruction mechanisms**  
  - Traditional search and static filters cannot re‑assemble episodic experiences from scattered traces.  

## 3. Inventive Solution – High‑Level Overview  

- **Agentic architecture** – Autonomous software agents run persistently, aggregating activity fragments.  
- **Multi‑source correlation** – Combines:  
  - `temporal proximity analysis` – Groups events close in time.  
  - `semantic similarity modelling` – Uses vector embeddings to find meaning overlaps.  
  - `behavioural pattern inference` – Learns user‑specific habits.  
- **Event‑graph construction** – Structured graph visualizing relationships among actions, applications, and information objects.  
- **Narrative synthesis** – Traverses the event graph to generate a coherent, timeline‑based narrative.  
- **Interactive recall interface** – Users inspect, refine, and expand queries, receiving readable stories.  
- **Privacy‑by‑design** – All data stored locally unless user opts for remote storage.  

## 4. Detailed System Components  

### 4.1. Autonomous Agents  

- **Data collection agents** – Harvest logs from email clients, document repositories, web browsers, and application logs.  
- **Context‑analysis agents** – Extract metadata and perform lightweight NLP for semantic cues.  

### 4.2. Correlation Engine  

- **Temporal proximity analysis** – Groups events within configurable windows (e.g., ±5 minutes).  
- **Semantic similarity modelling** – Utilizes embeddings (BERT, FastText) to quantify meaning overlap.  
- **Behavioural pattern inference** – Machine‑learning classifiers detect recurring user sequences.  
- **Output** – Weighted edge list linking events in the event graph; edge weights reflect combined confidence.  

### 4.3. Event Graph  

- **Node types**  
  - Communication (emails, chat messages)  
  - Document interaction (open, edit, save)  
  - Web activity (visited URLs, tabs)  
  - Application usage (IDE, media player)  
- **Edge semantics** – Temporal, semantic, and behavioural similarity scores.  

### 4.4. Reconstruction Engine  

- Traverses the event graph to assemble a chronological narrative.  
- Generates natural‑language summaries with contextual highlights.  

### 4.5. User Interface  

- Interactive timeline view with expandable event nodes.  
- Query refinement tools (keyword, time range, semantic filter).  
- Export options: plain text, PDF, or structured JSON.  

## 5. Autonomous Agents (Reference)  

For a deeper dive into the agent design, see [[Autonomous Agents]].  

---