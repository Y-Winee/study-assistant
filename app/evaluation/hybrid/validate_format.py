
import json
import re
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent

with open(CURRENT_DIR.parent / "result.json", encoding="utf-8") as f:
    results = json.load(f)


EXPECTED_QUESTIONS = 5
EXPECTED_FLASHCARDS = 5

issues = []

def add_issue(case_id, task, message):
    issues.append({
        "id": case_id,
        "task": task,
        "issue": message
    })

def normalize_text(text):
    """Normalize text for duplicate detection."""
    return re.sub(r"[\W_]", "", text).casefold()

def check_no_brackets(case_id, task, text):
    if "[" in text or "]" in text:
        add_issue(
            case_id,
            task,
            "Square brackets detected in the output"
        )

def validate_summary(case_id, text):

    sentence_endings = re.findall(
        r"[.!?]+(?=\s|$)",
        text.strip()
    )

    total_sentences = len(sentence_endings)

    if not 5 <= total_sentences <= 10:
        add_issue(
            case_id,
            "summary",
            f"Expected 5-10 sentences, found {total_sentences}"
        )

def get_question_blocks(text):

    matches = list(re.finditer(
        r"(?im)^\s*Question\s+\d+\s*:",
        text
    ))

    return [
        text[m.start():matches[i + 1].start()]
        if i + 1 < len(matches)
        else text[m.start():]
        for i, m in enumerate(matches)
    ]

def validate_quizz(case_id, text):

    questions = get_question_blocks(text)

    if len(questions) != EXPECTED_QUESTIONS:
        add_issue(
            case_id,
            "quizz",
            f"Expected {EXPECTED_QUESTIONS} questions, found {len(questions)}"
        )

    for number, question in enumerate(questions, 1):

        # Check question text
        question_match = re.search(
            r"(?im)^\s*Question\s+\d+\s*:\s*(.+)",
            question
        )

        if not question_match or not question_match.group(1).strip():
            add_issue(
                case_id,
                "quizz",
                f"Question {number}: Missing question text"
            )

        # Check options
        options = re.findall(
            r"(?im)^\s*([A-D])\.\s*(.+?)\s*$",
            question
        )

        option_labels = [label for label, _ in options]
        option_texts = [value for _, value in options]

        if len(options) != 4 or set(option_labels) != {"A", "B", "C", "D"}:
            add_issue(
                case_id,
                "quizz",
                f"Question {number}: Expected exactly 4 options (A-D)"
            )

        # Check duplicate options
        normalized_options = [
            normalize_text(option)
            for option in option_texts
        ]

        if len(normalized_options) != len(set(normalized_options)):
            add_issue(
                case_id,
                "quizz",
                f"Question {number}: Duplicate options detected"
            )

        # Check correct answer
        answers = re.findall(
            r"(?im)^\s*Correct Answer:\s*(.*?)\s*$",
            question
        )

        if len(answers) != 1:
            add_issue(
                case_id,
                "quizz",
                f"Question {number}: Expected exactly one correct answer"
            )

        elif answers[0].strip() not in {"A", "B", "C", "D"}:
            add_issue(
                case_id,
                "quizz",
                f"Question {number}: Invalid correct answer"
            )

        # Check explanation
        explanations = re.findall(
            r"(?im)^\s*Explanation:\s*(.*?)\s*$",
            question
        )

        if len(explanations) != 1 or not explanations[0].strip():
            add_issue(
                case_id,
                "quizz",
                f"Question {number}: Missing or invalid explanation"
            )

        # Check square brackets
        check_no_brackets(case_id, "quizz", question)

def validate_flashcard(case_id, text):

    matches = list(re.finditer(
        r"(?im)^\s*\d+\.\s*\*\*Question:\*\*",
        text
    ))

    if len(matches) != EXPECTED_FLASHCARDS:
        add_issue(
            case_id,
            "flashcard",
            f"Expected {EXPECTED_FLASHCARDS} flashcards, found {len(matches)}"
        )

    cards = [
        text[m.start():matches[i + 1].start()]
        if i + 1 < len(matches)
        else text[m.start():]
        for i, m in enumerate(matches)
    ]

    questions = []

    for number, card in enumerate(cards, 1):

        # Check question
        question_match = re.search(
            r"(?im)^\s*\d+\.\s*\*\*Question:\*\*\s*(.+?)\s*$",
            card
        )

        if not question_match:
            add_issue(
                case_id,
                "flashcard",
                f"Flashcard {number}: Missing question"
            )
        else:
            questions.append(
                normalize_text(question_match.group(1))
            )

        # Check answer
        answer_match = re.search(
            r"(?im)^\s*\*\*Answer:\*\*\s*(.+)",
            card
        )

        if not answer_match or not answer_match.group(1).strip():
            add_issue(
                case_id,
                "flashcard",
                f"Flashcard {number}: Missing answer"
            )

    # Check duplicate questions
    if len(questions) != len(set(questions)):
        add_issue(
            case_id,
            "flashcard",
            "Duplicate flashcard questions detected"
        )

for result in results:

    case_id = result["id"]
    task = result["task"]
    generated_output = result["generated_output"]

    if not isinstance(generated_output, str):
        add_issue(
            case_id,
            task,
            "Generated output must be a string"
        )
        continue

    if task == "summary":
        validate_summary(case_id, generated_output)

    elif task == "quizz":
        validate_quizz(case_id, generated_output)

    elif task == "flashcard":
        validate_flashcard(case_id, generated_output)

    else:
        add_issue(
            case_id,
            task,
            "Unknown task type"
        )

failed_outputs = {
    (issue["id"], issue["task"])
    for issue in issues
}

total_outputs = len(results)
failed_count = len(failed_outputs)
passed_count = total_outputs - failed_count

validation_report = {
    "status": "failed" if issues else "passed",
    "total_outputs": total_outputs,
    "passed_outputs": passed_count,
    "failed_outputs": failed_count,
    "issues": issues
}


# Save JSON report
output_path = CURRENT_DIR.parent / "format_validation.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(
        validation_report,
        f,
        indent=4,
        ensure_ascii=False
    )