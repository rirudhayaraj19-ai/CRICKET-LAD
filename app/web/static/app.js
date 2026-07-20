const output = document.querySelector("#output");
const statusText = document.querySelector("#status");

document.querySelector("#run-demo").addEventListener("click", async () => {
  statusText.textContent = "Researching, vectorizing, questioning, and correcting...";
  output.textContent = "Running autonomous lab cycle...";
  const response = await fetch("/api/lab/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ topic: "Newton's second law and gravity", difficulty: "judge-demo" })
  });
  const data = await response.json();
  statusText.textContent = data.corrected ? "Correction applied and knowledge verified." : "Answer verified from evidence.";
  output.textContent = JSON.stringify(data, null, 2);
});
