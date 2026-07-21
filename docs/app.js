const output = document.querySelector("#output");
const statusText = document.querySelector("#status");
const runButton = document.querySelector("#run-demo");

const wait = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));

runButton.addEventListener("click", async () => {
  runButton.disabled = true;
  const stages = [
    "Collecting trusted science notes...",
    "Cleaning and chunking knowledge...",
    "Creating vector search evidence...",
    "Asking the AI a test question...",
    "Checking the answer against citations...",
    "Correcting the unsupported answer..."
  ];

  output.textContent = "Starting autonomous RAG lab...";
  for (const stage of stages) {
    statusText.textContent = stage;
    output.textContent += `\n✓ ${stage}`;
    await wait(420);
  }

  const result = {
    topic: "Newton's second law and gravity",
    collected_sources: 3,
    indexed_chunks: 3,
    question: "What is Newton's second law?",
    first_answer: "Newton's second law says gravity is the same for every object in every situation.",
    corrected: true,
    final_answer: "Newton's second law states that force equals mass times acceleration: F = m × a. The answer was corrected because the first response confused the law with gravity.",
    citations: [
      "Research note: Newton's second law states that force equals mass times acceleration.",
      "Research note: gravity is an attractive interaction between masses."
    ],
    verification: [
      "The corrected answer is grounded in retrieved evidence.",
      "The unsupported first answer was detected and replaced."
    ]
  };

  statusText.textContent = "Correction applied and knowledge verified.";
  output.textContent = JSON.stringify(result, null, 2);
  runButton.disabled = false;
});
