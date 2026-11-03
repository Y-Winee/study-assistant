from .model import BASE_MODEL, DEVICE, TOKENIZER
from .services.assistant_service import (
    AssistantService,
    GenerationService,
    ResponseType,
)

ML_CONTENT = """
Supervised learning is a machine learning approach in
which a model learns from labeled training data. Each
training example contains input features and a
corresponding target value or label. The objective is
to learn a relationship between the inputs and outputs
so that the model can make predictions on new,
unseen data.

Supervised learning is commonly divided into two
categories: classification and regression.

Classification predicts discrete categories or classes.
For example, an email classification model can predict
whether an incoming email is spam or not spam. Other
examples include image classification and disease
classification.

Regression predicts continuous numerical values.
For example, a house price prediction model estimates
the selling price of a house based on features such as
its size, location, and number of bedrooms.

During training, the model makes predictions using
the training data. A loss function measures the
difference between its predictions and the actual
target values. An optimization algorithm then updates
the model's parameters to reduce this loss.

After training, the model should be evaluated using
unseen test data. This helps determine whether the
model has learned useful patterns or simply memorized
the training examples. A model that performs well on
training data but poorly on unseen data may be
overfitting.
"""

service: AssistantService = GenerationService()

summary_result = service.generate_result(
    input=ML_CONTENT,
    response_type= ResponseType.summary,
    model= BASE_MODEL,
    tokenizer=TOKENIZER,
    device=DEVICE
)
print(summary_result)

quizz_result = service.generate_result(
    input=ML_CONTENT,
    response_type= ResponseType.quizz,
    model= BASE_MODEL,
    tokenizer=TOKENIZER,
    device=DEVICE
)
print(quizz_result)

flashcard_result = service.generate_result(
    input=ML_CONTENT,
    response_type= ResponseType.flashcard,
    model= BASE_MODEL,
    tokenizer=TOKENIZER,
    device=DEVICE
)
print(flashcard_result)