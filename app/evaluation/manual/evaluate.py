import json
from pathlib import Path

from ...model import BASE_MODEL, DEVICE, TOKENIZER
from ...services.assistant_service import (
    AssistantService,
    GenerationService,
    ResponseType,
)

service: AssistantService = GenerationService()

DATASET_PATH = Path(__file__).resolve().parent / "dataset.json"

with open(DATASET_PATH, "r", encoding="utf-8") as file:
    dataset = json.load(file)

response_types = [
    ResponseType.summary,
    ResponseType.quizz,
    ResponseType.flashcard
]

results = []

for data in dataset:
    print(f"\nEvaluating : {data['id']} - {data['topic']}")
    for response_type in response_types:
        response = service.generate_result(
            data['content'],
            response_type=response_type,
            model=BASE_MODEL,
            tokenizer=TOKENIZER,
            device=DEVICE
        )

        results.append({
            "id": data['id'],
            "topic": data['topic'],
            "task": response_type.value,
            "generated_output": response
        })

RESULT_PATH = Path(__file__).resolve().parent / "result.json"

with open(RESULT_PATH, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)