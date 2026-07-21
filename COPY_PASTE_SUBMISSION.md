# Copy-Paste Hackathon Submission Answers

## Project Title
AutoLearn Lab — A Self-Correcting AI Study Engine

## Short Project Name
AutoLearn Lab

## One-Line Pitch
AutoLearn Lab is an autonomous AI learning system that collects knowledge, turns it into vectors, asks itself questions, verifies answers with evidence, and corrects mistakes.

## Project Description
AutoLearn Lab is a polished AI automation and RAG demo built for the OpenAI Codex Hackathon. The goal is to show an AI system that does more than answer questions. It studies information, cleans it, stores it in a vector search system, retrieves useful evidence, answers a question, checks whether the answer is supported, and corrects itself when the answer is wrong.

The demo focuses on a science learning example. When the user clicks **Run Live Lab**, the system simulates collecting trusted notes about Newton’s second law and gravity, vectorizes the evidence, asks “What is Newton’s second law?”, detects an incorrect first answer, and replaces it with a grounded corrected answer. This demonstrates the full loop: research → clean → vectorize → retrieve → answer → verify → correct.

## Use Case
The use case is an automated AI study and training assistant for students, researchers, and builders. A student can give the system a topic such as physics, biology, chemistry, history, or technology. The system can collect trusted learning material, convert it into searchable knowledge, quiz itself, detect weak or wrong answers, and improve its final answer using evidence.

This can help students learn faster because the AI is not just giving an answer. It is showing the evidence, checking itself, and improving the explanation.

## OpenAI Model and API Usage
This project was built with help from OpenAI Codex as the coding agent. Codex helped generate and organize the FastAPI backend, RAG services, website UI, deployment files, documentation, and tests.

The current demo is designed to run locally without requiring a paid API key, so the live demo uses a deterministic local RAG pipeline instead of calling the OpenAI API at runtime. The code includes OpenAI-ready environment variables for future integration:

- `OPENAI_API_KEY`
- `OPENAI_MODEL`
- `OPENAI_EMBEDDING_MODEL`

In a production version, I would connect OpenAI embeddings for better semantic search and an OpenAI chat or responses model for stronger grounded answer generation.

## Other APIs or Models Used
The current demo does not call external APIs at runtime. It uses local deterministic demo connectors and a local TF-IDF vector search system so judges can try it without API keys.

The project is designed to support future integrations with:

- Pinecone for hosted vector storage
- Google Programmable Search or Custom Search for web research
- Meta Graph API for Facebook and Instagram data with user consent
- OpenAI embeddings and generation models for production RAG

These integrations are not required for the current demo link.

## Model Process / System Workflow
The project follows this process:

1. **Collect knowledge** — The connector layer gathers topic-related knowledge packets.
2. **Clean text** — The system normalizes messy text into clean content.
3. **Chunk documents** — Long content is split into smaller searchable chunks.
4. **Create vector index** — The chunks are converted into searchable vector-style representations using TF-IDF.
5. **Retrieve evidence** — When a question is asked, the system finds the most relevant chunks.
6. **Generate answer** — The RAG service creates an answer from retrieved evidence.
7. **Verify answer** — The answer is checked against citations and verification notes.
8. **Correct mistakes** — If the first answer is unsupported or wrong, the system replaces it with an evidence-grounded answer.
9. **Show result** — The website displays the corrected answer, citations, and verification details.

## Coding Agent Explanation
I used OpenAI Codex as my AI engineering partner. Codex helped me design the architecture, create the FastAPI backend, implement the local vector search system, build the RAG and autonomous lab workflow, design the polished website, add deployment files, and write documentation.

The coding agent workflow was:

1. Define the hackathon idea and product goal.
2. Create a modular backend with API routes, services, schemas, config, and tests.
3. Build a polished frontend that explains the idea clearly to judges.
4. Add a standalone GitHub Pages demo so the project can be submitted with a public link.
5. Add deployment documentation for the full backend version.
6. Improve the submission text so it is easy to copy and paste.

## Setup Steps to Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/
```

## Fast Public Demo Setup
For a quick public hackathon link, use GitHub Pages:

1. Push the repo to GitHub.
2. Go to **Settings → Pages**.
3. Choose **Deploy from a branch**.
4. Select the current branch.
5. Select the `/docs` folder.
6. Save and wait 1–3 minutes.
7. Submit this link format:

```text
https://YOUR-GITHUB-USERNAME.github.io/CRICKET-LAD/
```

## About the Name “CRICKET LAD”
“CRICKET LAD” is only the repository/project brand name. The project is not about cricket sports. The actual product idea is AutoLearn Lab: an AI automation and self-correcting RAG learning platform.

If the competition form asks for a clear title, use:

```text
AutoLearn Lab — A Self-Correcting AI Study Engine
```

## Final Copy-Paste Summary
AutoLearn Lab is an autonomous AI study engine built for the OpenAI Codex Hackathon. It collects trusted knowledge, cleans and chunks it, turns it into vector-searchable evidence, retrieves context, answers questions, verifies the answer, and corrects mistakes. The demo shows a science learning workflow where the AI catches a wrong answer about Newton’s second law and replaces it with an evidence-grounded correction. I used OpenAI Codex as my coding agent to design the system, build the backend, create the RAG workflow, polish the website, and prepare deployment and submission files. The current demo runs without external API keys, and it is ready for future OpenAI, Pinecone, Google Search, and official social API integrations.
