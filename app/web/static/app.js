const output = document.querySelector("#output");
const statusText = document.querySelector("#status");
const runButton = document.querySelector("#run-demo");

runButton.addEventListener("click", async () => {
  runButton.disabled = true;
  statusText.textContent = "Researching, vectorizing, questioning, and correcting...";
  output.textContent = "Running autonomous lab cycle...";

  try {
    const response = await fetch("/api/lab/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic: "Newton's second law and gravity", difficulty: "judge-demo" })
    });

    if (!response.ok) {
      throw new Error(`Demo API returned ${response.status}`);
    }

    const data = await response.json();
    statusText.textContent = data.corrected
      ? "Correction applied and knowledge verified."
      : "Answer verified from evidence.";
    output.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    statusText.textContent = "Demo backend is not reachable.";
    output.textContent = [
      "The website loaded, but the API link is not running yet.",
      "",
      "Fix:",
      "1. Run: uvicorn app.main:app --reload",
      "2. Open: http://127.0.0.1:8000/",
      "3. For hackathon judges, deploy to Render/Railway/Fly.io and submit the hosted URL.",
      "",
      `Details: ${error.message}`
    ].join("\n");
  } finally {
    runButton.disabled = false;
  }
});
