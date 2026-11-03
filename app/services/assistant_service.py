from abc import ABC, abstractmethod
from enum import Enum
from typing import TypedDict


class ResponseType(str, Enum):
    summary = "summary"
    flashcard = "flashcard"
    quizz = "quizz"

class Message(TypedDict):
    role: str
    content: str

class AssistantService(ABC):

    @abstractmethod
    def generate_result(self, input: str, response_type: ResponseType, model, tokenizer, device) -> str:
        pass

    @abstractmethod
    def generate_prompt(self, response_type: ResponseType, content: str) -> list[Message]:
        pass

class GenerationService(AssistantService):

    def generate_prompt(
        self,
        response_type: ResponseType,
        content: str
    ) -> list[Message]:

        if response_type == ResponseType.summary:
            instruction = """
            Summarize the following study material.

            Requirements:
            - Include the important concepts.
            - Use clear and natural language.
            - Organize the summary logically.
            - Avoid unnecessary introductions and conclusions.
            """

        elif response_type == ResponseType.flashcard:
            instruction = """
            Create 5 flashcards from the following study material.

            Requirements:
            - Each flashcard must have a question and an answer.
            - Focus on important concepts and definitions.
            - Keep questions and answers concise.
            - Use only information supported by the study material.
            """

        elif response_type == ResponseType.quizz:
            instruction = """
            Create exactly 5 multiple-choice questions (MCQs)
            based on the following study material.

            Requirements:
            - Each question must have exactly 4 options (A, B, C, D).
            - Only one option must be correct.
            - Make the incorrect options plausible but clearly incorrect.
            - Include the correct answer after each question.
            - Include a brief explanation of why the answer is correct.
            - Do not create open-ended questions.
            - Do not introduce information outside the study material.

            Additional quality requirements:

            - Every question must have exactly one unambiguously
            correct answer.
            - All four options must be distinct.
            - Incorrect options must be plausible but factually incorrect.
            - Questions and answers must be supported by the
            provided study material.
            - Do not introduce unsupported facts or examples.
            - Verify that the correct answer matches the source
            material before presenting the question.

            Use this format:

            Question 1: [Question]

            A. [Option]
            B. [Option]
            C. [Option]
            D. [Option]

            Correct Answer: [Letter]
            Explanation: [Brief explanation]
            """

        else:
            raise ValueError(f"Unsupported response type: {response_type}")

        return [
            {
                "role": "user",
                "content": f"{instruction}\n\nStudy Material:\n{content}"
            }
        ]

    def generate_result(
            self, 
            input: str, 
            response_type: ResponseType, 
            model, 
            tokenizer,
            device
        ) -> str:
        messages = self.generate_prompt(response_type=response_type, content=input)
        inputs = tokenizer.apply_chat_template(
	                messages,
                    add_generation_prompt=True,
                    tokenize=True,
                    return_dict=True,
                    return_tensors="pt",
                    enable_thinking=False
                ).to(device)
        generated_tokens = model.generate(**inputs, max_new_tokens=2048)
        input_length = inputs['input_ids'].shape[1]
        generated_tokens = generated_tokens[:, input_length:]

        return tokenizer.decode(
            generated_tokens[0],
            skip_special_tokens=True
        ).strip()