# Deployment Guide: Make the Demo Link Work

`http://127.0.0.1:8000/` only works on your own computer while the server is running. Judges cannot open that link from their computers. For hackathon submission, deploy the app and submit the hosted URL.

## Fastest Option: Render

1. Push this repo to GitHub.
2. Open Render and choose **New → Web Service**.
3. Connect the GitHub repo.
4. Render can read `render.yaml`, or use these settings manually:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. After deploy, open the Render URL. It should look like:

```text
https://cricket-lad.onrender.com/
```

6. Paste that hosted URL into the hackathon submission form.

## Local Test Before Submitting

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/
```

## Docker Option

```bash
docker build -t cricket-lad .
docker run -p 8000:8000 cricket-lad
```

Then open `http://127.0.0.1:8000/`.

## Troubleshooting

- If the page opens but the button fails, the backend is not running or `/api/lab/run` is unreachable.
- If a hosted URL sleeps on a free plan, wait 30–60 seconds and refresh.
- Do not put API keys in the GitHub repo. Add secrets in the hosting provider dashboard.
