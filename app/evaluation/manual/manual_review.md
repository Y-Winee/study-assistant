# AI Study Assistant - Manual Evaluation

Evaluate each generated response against the reference facts.

## Scoring guide

- 2 = Correctly covered
- 1 = Partially covered
- 0 = Missing
- Incorrect = Contradicted by the source material

---

# ML-001 - Supervised Learning

## Task: SUMMARY

### Generated output

```text
Supervised learning involves a model learning from labeled training data, where each example includes input features and a target label. The goal is to establish a relationship between inputs and outputs so that the model can make predictions on new data. It is divided into two types: classification (predicting discrete categories) and regression (predicting continuous values). During training, the model uses a loss function to measure the difference between predictions and the actual targets, and an optimization algorithm adjusts its parameters to minimize this loss. After training, the model is tested using unseen data to evaluate its performance and determine if it has learned useful patterns or just memorized the training examples. A model that performs well on training but poorly on test data may overfit.
```

### Reference fact evaluation

**Fact 1:** Supervised learning uses labeled training data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Each training example contains input features and a corresponding target value or label.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The model learns a relationship between inputs and outputs to make predictions on unseen data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Classification predicts discrete categories or classes.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Regression predicts continuous numerical values.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** A loss function measures the difference between predictions and actual target values.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** An optimization algorithm updates model parameters to reduce the loss.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The model is evaluated using unseen test data, and good training performance with poor test performance may indicate overfitting.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

### Additional evaluation

**Unsupported claims or factual errors:**

Notes:

**Clarity (0-2):**

**Instruction following (0-2):**

**Other observations:**

---

# ML-001 - Supervised Learning

## Task: QUIZZ

### Generated output

```text
Question 1: What is the primary goal of supervised learning?  

A. To predict unknown data using training examples  
B. To learn a relationship between inputs and outputs  
C. To classify discrete categories  
D. To memorize training data  

Correct Answer: B  
Explanation: Supervised learning is designed to learn relationships between inputs and outputs, not just predict unknown data. The objective is to build models that can make accurate predictions on new data.  

Question 2: How is supervised learning typically used in machine learning?  

A. As a separate machine learning algorithm  
B. As a part of a larger data preprocessing step  
C. To train models on labeled data  
D. To make predictions on unseen data  

Correct Answer: C  
Explanation: Supervised learning is used to train models on labeled data to learn patterns and make predictions. The process involves using training examples to improve the model’s ability to predict new inputs.  

Question 3: What is the difference between classification and regression in supervised learning?  

A. Classification uses continuous numerical values  
B. Regression uses discrete categories  
C. Both use continuous numerical values  
D. Regression uses discrete categories  

Correct Answer: B  
Explanation: Classification is used for discrete categories (e.g., spam vs. not spam), while regression is used for continuous numerical values (e.g., house price). Both are part of supervised learning, but their purposes differ.  

Question 4: What is the purpose of a loss function in supervised learning?  

A. To measure how well the model predicts the target value  
B. To optimize the model's parameters  
C. To reduce the difference between predictions and actual values  
D. To increase the accuracy of the model  

Correct Answer: C  
Explanation: A loss function measures the difference between the model’s predictions and the actual target values, helping the model improve its accuracy over time.  

Question 5: How is supervised learning evaluated after training?  

A. Using only test data  
B. Using both training and test data  
C. Using only training data  
D. Using only unseen data  

Correct Answer: B  
Explanation: After training, the model is evaluated using unseen test data to determine if it learned useful patterns or simply memorized the training examples. This ensures the model generalizes well to new data.
```

### Reference fact evaluation

**Fact 1:** Supervised learning uses labeled training data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Each training example contains input features and a corresponding target value or label.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The model learns a relationship between inputs and outputs to make predictions on unseen data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Classification predicts discrete categories or classes.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Regression predicts continuous numerical values.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** A loss function measures the difference between predictions and actual target values.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** An optimization algorithm updates model parameters to reduce the loss.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The model is evaluated using unseen test data, and good training performance with poor test performance may indicate overfitting.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

### Additional evaluation

**Unsupported claims or factual errors:**

Notes:

**Clarity (0-2):**

**Instruction following (0-2):**

**Other observations:**

---

# ML-001 - Supervised Learning

## Task: FLASHCARD

### Generated output

```text
1. **Question:** What is supervised learning?  
   **Answer:** Supervised learning is a machine learning approach where a model learns from labeled training data. Each example has input features and a target value (label), and the goal is to learn a relationship between inputs and outputs to make predictions on new data.  

2. **Question:** How is supervised learning divided?  
   **Answer:** Supervised learning is divided into classification (predicting discrete classes) and regression (predicting continuous values).  

3. **Question:** What is a loss function?  
   **Answer:** A loss function measures the difference between the model’s predictions and the actual target values during training.  

4. **Question:** How is the model updated during training?  
   **Answer:** The model uses an optimization algorithm to adjust its parameters to reduce the loss function, improving its performance.  

5. **Question:** How is a model evaluated?  
   **Answer:** A model is evaluated using test data to determine if it has learned useful patterns. A model that performs poorly on test data may be overfitting.
```

### Reference fact evaluation

**Fact 1:** Supervised learning uses labeled training data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Each training example contains input features and a corresponding target value or label.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The model learns a relationship between inputs and outputs to make predictions on unseen data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Classification predicts discrete categories or classes.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Regression predicts continuous numerical values.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** A loss function measures the difference between predictions and actual target values.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** An optimization algorithm updates model parameters to reduce the loss.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The model is evaluated using unseen test data, and good training performance with poor test performance may indicate overfitting.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

### Additional evaluation

**Unsupported claims or factual errors:**

Notes:

**Clarity (0-2):**

**Instruction following (0-2):**

**Other observations:**

---
