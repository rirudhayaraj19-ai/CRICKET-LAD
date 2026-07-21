# Paste-Ready Hackathon Submission

## Project Title
CRICKET LAD — Autonomous AI Learning Lab

## One-Line Pitch
An AI lab built by a 12-year-old that researches trusted knowledge, turns it into vectors, tests itself, and corrects wrong answers using RAG.

## Submission Description
CRICKET LAD is an autonomous learning platform for the OpenAI Codex Hackathon. The system collects knowledge from connector-ready sources, cleans and chunks it, stores it in a vector index, retrieves evidence, answers questions, verifies the answer, and corrects mistakes. The live demo shows the full loop with a science question: it starts with a wrong answer, checks retrieved evidence, and replaces it with a grounded answer.

## Demo Link
Local demo after running the app:

```text
http://127.0.0.1:8000/
```

If you deploy it, replace the local URL above with your hosted URL from Render, Railway, Fly.io, Vercel, or another hosting provider.

## What Judges Should Try
1. Open the website.
2. Click **Run Live Lab**.
3. Watch the app collect demo research packets and index chunks.
4. Notice the intentionally wrong first answer.
5. See the corrected answer, citations, and verification notes.
6. Open `/docs` to inspect the API.

## Why It Is Interesting
Most chat apps only answer. CRICKET LAD demonstrates an AI workflow that can study, test itself, detect a wrong answer, and improve using evidence. It is designed to become a real platform with Google research, official social APIs, Pinecone vectors, OpenAI embeddings, and automated background learning.

## Important Safety Note
Do not paste API keys into public submissions or GitHub. Store OpenAI, Pinecone, Google, Facebook, and Instagram credentials only in private environment variables.
