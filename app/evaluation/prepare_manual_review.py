import json
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent

DATASET_PATH = CURRENT_DIR / "dataset.json"
RESULT_PATH = CURRENT_DIR / "result.json"
REVIEW_PATH = CURRENT_DIR / "manual_review.md"

# Load dataset and generated results
with open(DATASET_PATH, "r", encoding="utf-8") as file:
    dataset = json.load(file)

with open(RESULT_PATH, "r", encoding="utf-8") as file:
    results = json.load(file)

# Index generated results by ID and task
result_lookup = {
    (item["id"], item["task"]): item["generated_output"]
    for item in results
}

response_types = ["summary", "quizz", "flashcard"]

lines = [
    "# AI Study Assistant - Manual Evaluation",
    "",
    "Evaluate each generated response against the reference facts.",
    "",
    "## Scoring guide",
    "",
    "- 2 = Correctly covered",
    "- 1 = Partially covered",
    "- 0 = Missing",
    "- Incorrect = Contradicted by the source material",
    "",
    "---",
    ""
]

for item in dataset:

    case_id = item["id"]
    topic = item["topic"]

    for task in response_types:

        output = result_lookup.get((case_id, task))

        if output is None:
            continue

        lines.extend([
            f"# {case_id} - {topic}",
            "",
            f"## Task: {task.upper()}",
            "",
            "### Generated output",
            "",
            "```text",
            output,
            "```",
            "",
            "### Reference fact evaluation",
            ""
        ])

        for index, fact in enumerate(item["key_facts"], start=1):

            lines.extend([
                f"**Fact {index}:** {fact}",
                "",
                "- [ ] 2 - Correctly covered",
                "- [ ] 1 - Partially covered",
                "- [ ] 0 - Missing",
                "- [ ] Incorrect / contradicted",
                ""
            ])

        lines.extend([
            "### Additional evaluation",
            "",
            "**Unsupported claims or factual errors:**",
            "",
            "Notes:",
            "",
            "**Clarity (0-2):**",
            "",
            "**Instruction following (0-2):**",
            "",
            "**Other observations:**",
            "",
            "---",
            ""
        ])

# Save review document
REVIEW_PATH.write_text(
    "\n".join(lines),
    encoding="utf-8"
)

print(f"Manual evaluation report created: {REVIEW_PATH}")