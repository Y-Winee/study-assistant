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
Supervised learning involves training a model using labeled data, where each example includes input features and a target value (label). The goal is to learn patterns between inputs and outputs so that the model can make accurate predictions on new data. It is commonly divided into classification (predicting discrete categories) and regression (predicting continuous numerical values). During training, the model uses a loss function to measure the difference between its predictions and the actual values, and an optimization algorithm adjusts its parameters to minimize this loss. After training, the model is tested using unseen data to evaluate its performance, helping determine if it overfits or if it has learned the training patterns.
```

### Reference fact evaluation

**Fact 1:** Supervised learning uses labeled training data.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Each training example contains input features and a corresponding target value or label.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The model learns a relationship between inputs and outputs to make predictions on unseen data.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Classification predicts discrete categories or classes.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Regression predicts continuous numerical values.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** A loss function measures the difference between predictions and actual target values.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** An optimization algorithm updates model parameters to reduce the loss.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The model is evaluated using unseen test data, and good training performance with poor test performance may indicate overfitting.

- [ * ] 2 - Correctly covered
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
Question 1: What is the primary goal of supervised learning in machine learning?

A. To predict new data based on existing data
B. To classify data into predefined categories
C. To find patterns in existing data
D. To estimate continuous numerical values

Correct Answer: B  
Explanation: Supervised learning is primarily used for classification tasks where the model learns to predict discrete categories or classes, such as email spam detection. Option A is general and does not reflect the core goal. Option C is too vague and does not specify the type of learning. Option D is about regression, which is a different type of supervised learning.

Question 2: How does supervised learning differ from unsupervised learning?

A. Supervised learning uses only labeled data
B. Supervised learning uses only unlabeled data
C. Supervised learning finds patterns in unlabeled data
D. Supervised learning is used for both classification and regression

Correct Answer: A  
Explanation: Supervised learning uses labeled training data, meaning the model learns from both input and output data. Unsupervised learning, on the other hand, uses unlabeled data and does not involve labeled outputs. Option C is incorrect because it refers to unsupervised learning, not supervised. Option B is also incorrect because it describes a different type of learning. Option D is incorrect as well.

Question 3: In supervised learning, what is a loss function used for?

A. To measure the difference between predictions and actual values
B. To find the best fit for the model
C. To find the best model for the data
D. To find the best model for the training data

Correct Answer: A  
Explanation: The loss function is used to measure the difference between the predicted values and the actual target values in supervised learning. Option B and C are incorrect because they refer to other components of the model. Option D is incorrect as well.

Question 4: What is the main purpose of the training phase in supervised learning?

A. To use the data for prediction
B. To use the data for classification
C. To use the data for regression
D. To use the data for both classification and regression

Correct Answer: A  
Explanation: During training, the model uses the training data to make predictions on new, unseen data. Option B and C are incorrect because they refer to different tasks. Option D is incorrect as well.
```

### Reference fact evaluation

**Fact 1:** Supervised learning uses labeled training data.

- [ ] 2 - Correctly covered
- [ * ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Each training example contains input features and a corresponding target value or label.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ * ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The model learns a relationship between inputs and outputs to make predictions on unseen data.

- [ ] 2 - Correctly covered
- [ * ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Classification predicts discrete categories or classes.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ * ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Regression predicts continuous numerical values.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ * ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** A loss function measures the difference between predictions and actual target values.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** An optimization algorithm updates model parameters to reduce the loss.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ * ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The model is evaluated using unseen test data, and good training performance with poor test performance may indicate overfitting.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ * ] 0 - Missing
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
   **Answer:** A machine learning approach where a model learns from labeled training data to predict outputs on unseen data.  

2. **Question:** How is supervised learning divided?  
   **Answer:** Supervised learning is divided into classification and regression. Classification predicts discrete categories, while regression predicts continuous values.  

3. **Question:** What is the objective of supervised learning?  
   **Answer:** To learn a relationship between inputs and outputs so that the model can predict new data.  

4. **Question:** What is the role of a loss function in supervised learning?  
   **Answer:** The loss function measures the difference between predictions and actual target values, helping the model minimize this difference.  

5. **Question:** How is a model evaluated after training?  
   **Answer:** After training, the model is evaluated using unseen test data to determine if it learned useful patterns or just memorized the training data.
```

### Reference fact evaluation

**Fact 1:** Supervised learning uses labeled training data.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Each training example contains input features and a corresponding target value or label.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The model learns a relationship between inputs and outputs to make predictions on unseen data.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Classification predicts discrete categories or classes.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Regression predicts continuous numerical values.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** A loss function measures the difference between predictions and actual target values.

- [ * ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** An optimization algorithm updates model parameters to reduce the loss.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ * ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The model is evaluated using unseen test data, and good training performance with poor test performance may indicate overfitting.

- [ * ] 2 - Correctly covered
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

# NET-001 - TCP/IP Networking

## Task: SUMMARY

### Generated output

```text
The TCP/IP protocol suite enables devices to communicate over networks, with four layers: Application, Transport, Internet, and Network Access. The Application layer provides services like web browsing and email. The Transport layer supports communication between processes, using TCP (connection-oriented, reliable delivery) and UDP (connectionless, lower overhead). The Internet layer handles logical addressing and routing, using IP addresses to route packets, and the Network Access layer manages local network communication. Each layer works together to ensure data is formatted, transmitted, and delivered correctly.
```

### Reference fact evaluation

**Fact 1:** TCP/IP is a protocol suite that enables communication between devices over networks.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** The four TCP/IP model layers described here are Application, Transport, Internet, and Network Access.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The Application layer provides network services to applications such as web browsing and email.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** The Transport layer supports communication between processes on different devices.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** TCP is connection-oriented and provides reliable, ordered delivery, including retransmission of missing data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** UDP is connectionless and does not guarantee delivery or ordering.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** The Internet layer handles logical addressing and routing between networks.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The Network Access layer handles sending data over the local network link.

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

# NET-001 - TCP/IP Networking

## Task: QUIZZ

### Generated output

```text
Question 1: What is the main function of the Internet layer in the TCP/IP model?

A. It handles logical addressing and routing between networks  
B. It provides network services to applications  
C. It covers communication over the local network link  
D. It is responsible for data transmission between devices

Correct Answer: A  
Explanation: The Internet layer, also known as the IP layer, handles logical addressing and routing between networks. It identifies network interfaces and helps route packets toward their destinations, which is a key role in the TCP/IP model.

Question 2: Which two transport protocols are commonly used in the TCP/IP model?

A. TCP and UDP  
B. TCP and HTTP  
C. UDP and TCP  
D. None of the above

Correct Answer: A  
Explanation: The two commonly used transport protocols in the TCP/IP model are TCP (Connection-oriented) and UDP (Connectionless). Both protocols play essential roles in data communication between devices.

Question 3: What is the purpose of the Network Access layer in the TCP/IP model?

A. It provides network services to applications  
B. It handles logical addressing and routing between networks  
C. It covers communication over the local network link  
D. It is responsible for data transmission between devices

Correct Answer: C  
Explanation: The Network Access layer in the TCP/IP model covers communication over the local network link. It ensures that data is sent across the physical or wireless medium between devices, which is a fundamental function of this layer.

Question 4: What is the role of the Transport layer in the TCP/IP model?

A. It provides network services to applications  
B. It supports communication between processes on different devices  
C. It handles logical addressing and routing between networks  
D. It is responsible for data transmission between devices

Correct Answer: B  
Explanation: The Transport layer in the TCP/IP model supports communication between processes on different devices. It uses protocols like TCP (Connection-oriented) and UDP (Connectionless) to ensure reliable and efficient data transfer between applications.

Question 5: What is the main purpose of the Application layer in the TCP/IP model?

A. It provides network services to applications  
B. It handles logical addressing and routing between networks  
C. It covers communication over the local network link  
D. It is responsible for data transmission between devices

Correct Answer: A  
Explanation: The Application layer in the TCP/IP model provides network services to applications, such as web browsing and email. It acts as the last layer in the communication process, ensuring that data is properly formatted and delivered to the user.
```

### Reference fact evaluation

**Fact 1:** TCP/IP is a protocol suite that enables communication between devices over networks.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** The four TCP/IP model layers described here are Application, Transport, Internet, and Network Access.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The Application layer provides network services to applications such as web browsing and email.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** The Transport layer supports communication between processes on different devices.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** TCP is connection-oriented and provides reliable, ordered delivery, including retransmission of missing data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** UDP is connectionless and does not guarantee delivery or ordering.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** The Internet layer handles logical addressing and routing between networks.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The Network Access layer handles sending data over the local network link.

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

# NET-001 - TCP/IP Networking

## Task: FLASHCARD

### Generated output

```text
1. **Question:** What is the purpose of the Internet layer in the TCP/IP model?  
   **Answer:** It handles logical addressing and routing between networks.  

2. **Question:** What is the primary function of the Transport layer?  
   **Answer:** It supports communication between processes on different devices.  

3. **Question:** What are the two common transport protocols?  
   **Answer:** TCP and UDP.  

4. **Question:** What does TCP do compared to UDP?  
   **Answer:** TCP is connection-oriented and provides reliable, ordered delivery.  

5. **Question:** What does the Network Access layer do?  
   **Answer:** It covers communication over the local network link, including data sent across physical or wireless mediums.
```

### Reference fact evaluation

**Fact 1:** TCP/IP is a protocol suite that enables communication between devices over networks.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** The four TCP/IP model layers described here are Application, Transport, Internet, and Network Access.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** The Application layer provides network services to applications such as web browsing and email.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** The Transport layer supports communication between processes on different devices.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** TCP is connection-oriented and provides reliable, ordered delivery, including retransmission of missing data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** UDP is connectionless and does not guarantee delivery or ordering.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** The Internet layer handles logical addressing and routing between networks.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The Network Access layer handles sending data over the local network link.

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

# AWS-001 - AWS EC2, S3, and Lambda

## Task: SUMMARY

### Generated output

```text
Amazon Web Services (AWS) offers cloud computing services to help organizations build and run applications. The three main services are:

- **Amazon EC2**: Provides virtual servers (instances) with configurable settings like operating systems, storage, and networking. Ideal for applications requiring server environments that can be customized.
- **Amazon S3**: Provides object storage, allowing data to be stored and retrieved without needing a server. Applications can store and access files easily.
- **AWS Lambda**: A serverless computing service where developers upload code as functions, and AWS manages the servers. It's used for event-driven tasks where developers don't need to manage underlying infrastructure.
```

### Reference fact evaluation

**Fact 1:** AWS provides cloud services for building and running applications.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Amazon EC2 provides virtual servers called instances.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** With EC2, users choose an instance type and configure details such as the operating system, storage, and networking.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Amazon S3 provides object storage.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** S3 stores objects in buckets, and objects can include documents, images, videos, and backups.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** AWS Lambda is a serverless compute service that runs functions while AWS manages the underlying servers.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Lambda functions can be invoked by events, such as an object upload to S3.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** EC2 provides configurable virtual servers, S3 provides object storage, and Lambda runs event-driven functions.

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

# AWS-001 - AWS EC2, S3, and Lambda

## Task: QUIZZ

### Generated output

```text
Question 1: What is the primary purpose of Amazon EC2?  
A. To provide virtual servers for running applications  
B. To manage servers on-premise  
C. To handle specific tasks involving data storage  
D. To run serverless applications without managing servers  

Correct Answer: A  
Explanation: The study material states that EC2 provides virtual servers, which aligns with option A. Option B is incorrect as it refers to on-premise management, not EC2. Option C is incorrect because EC2 is not for storage but for computing. Option D is incorrect as it refers to serverless.

Question 2: What is the key difference between Amazon EC2 and AWS Lambda?  
A. EC2 is for storing data, while Lambda is for processing tasks  
B. EC2 is for managing servers, while Lambda is for running functions  
C. EC2 is for handling serverless tasks, while Lambda is for running serverless functions  
D. EC2 is for managing virtual servers, while Lambda is for managing storage  

Correct Answer: B  
Explanation: The study material explains that EC2 provides virtual servers, while Lambda manages the servers without the developer managing them. Option B correctly identifies this difference.

Question 3: What is the purpose of Amazon S3?  
A. To provide object storage for storing files  
B. To manage servers on-premise  
C. To run serverless applications without managing servers  
D. To provide virtual servers for running applications  

Correct Answer: A  
Explanation: The study material states that S3 provides object storage, which aligns with option A. Option B is incorrect as it refers to on-premise management. Option C is incorrect as S3 is not serverless. Option D is incorrect as it refers to virtual servers for applications.

Question 4: What is the primary use case of AWS Lambda?  
A. To run serverless applications  
B. To manage virtual servers  
C. To handle specific tasks involving data storage  
D. To provide virtual servers for running applications  

Correct Answer: A  
Explanation: The study material explains that AWS Lambda is a serverless compute service, which aligns with option A. Option B is incorrect as it refers to on-premise management. Option C is incorrect as it refers to storage. Option D is incorrect as it refers to virtual servers for applications.
```

### Reference fact evaluation

**Fact 1:** AWS provides cloud services for building and running applications.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Amazon EC2 provides virtual servers called instances.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** With EC2, users choose an instance type and configure details such as the operating system, storage, and networking.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Amazon S3 provides object storage.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** S3 stores objects in buckets, and objects can include documents, images, videos, and backups.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** AWS Lambda is a serverless compute service that runs functions while AWS manages the underlying servers.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Lambda functions can be invoked by events, such as an object upload to S3.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** EC2 provides configurable virtual servers, S3 provides object storage, and Lambda runs event-driven functions.

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

# AWS-001 - AWS EC2, S3, and Lambda

## Task: FLASHCARD

### Generated output

```text
1. **Question:** What is the purpose of Amazon EC2?  
   **Answer:** EC2 provides virtual servers (instances) that allow users to configure and manage operating environments, storage, and networking.  

2. **Question:** What is Amazon S3 used for?  
   **Answer:** S3 provides object storage, storing files, documents, images, videos, and backups. Applications can retrieve these objects without needing a virtual server.  

3. **Question:** What is AWS Lambda?  
   **Answer:** AWS Lambda is a serverless compute service that runs functions based on events, such as S3 uploads or app requests, without managing the underlying servers.  

4. **Question:** What is the difference between EC2 and Lambda?  
   **Answer:** EC2 provides configurable virtual servers, while Lambda runs functions without requiring server management.  

5. **Question:** What are the three commonly used AWS services?  
   **Answer:** Amazon EC2, Amazon S3, and AWS Lambda.
```

### Reference fact evaluation

**Fact 1:** AWS provides cloud services for building and running applications.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Amazon EC2 provides virtual servers called instances.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** With EC2, users choose an instance type and configure details such as the operating system, storage, and networking.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Amazon S3 provides object storage.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** S3 stores objects in buckets, and objects can include documents, images, videos, and backups.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** AWS Lambda is a serverless compute service that runs functions while AWS manages the underlying servers.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Lambda functions can be invoked by events, such as an object upload to S3.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** EC2 provides configurable virtual servers, S3 provides object storage, and Lambda runs event-driven functions.

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

# DL-001 - Transformer Architecture

## Task: SUMMARY

### Generated output

```text
A transformer is a neural network architecture designed to process sequences of data, commonly used in natural language processing. Unlike traditional recurrent networks, transformers use attention mechanisms to model relationships between tokens, enabling efficient processing of sequences. 

Before processing text, it is divided into tokens, each converted into an embedding. Positional encoding is also added to preserve the order of tokens. The self-attention mechanism allows each token to incorporate information from other tokens, forming queries, keys, and values. This mechanism computes attention scores to determine how strongly a token uses information from other tokens.

Transformer layers include an attention sublayer and a feed-forward network. Residual connections and layer normalization are used to support information flow and stability. The original architecture used an encoder-decoder design, while modern models often use a decoder-only Transformer. By stacking multiple layers, the model can build increasingly contextual representations of the input sequence, making it a foundational component in modern language models.
```

### Reference fact evaluation

**Fact 1:** A Transformer is a neural network architecture designed to process sequences and is widely used in natural language processing.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Transformers use attention mechanisms rather than processing sequence elements only step by step as recurrent neural networks do.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** Text is divided into tokens, and tokens are converted into numerical embeddings.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Positional information is added to represent token order because self-attention alone does not encode sequence order.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Self-attention lets each token representation incorporate information from other tokens in the sequence.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** Scaled dot-product attention uses queries, keys, and values to calculate how information from other tokens is weighted.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Common Transformer layers include attention and feed-forward sublayers, with residual connections and layer normalization.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The original Transformer used an encoder and decoder, while many modern language models use decoder-only architectures.

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

# DL-001 - Transformer Architecture

## Task: QUIZZ

### Generated output

```text
Question 1: What is the primary purpose of the self-attention mechanism in Transformers?

A. The self-attention mechanism is used to process sequences of data in a neural network.

B. The self-attention mechanism is used to build contextual representations of input sequences.

C. The self-attention mechanism is used to convert text into numerical representations.

D. The self-attention mechanism is used to encode sequence order by itself.

Correct Answer: B  
Explanation: The self-attention mechanism is designed to allow each token in a sequence to incorporate information from other tokens in the sequence, which is crucial for building contextual representations. The other options either incorrectly state the purpose or are factually incorrect.  

Question 2: What is the role of the encoder in the Transformer architecture?

A. The encoder processes the input sequence and creates a representation of the sequence.

B. The encoder processes the input sequence and creates a representation of the sequence in the form of a matrix.

C. The encoder processes the input sequence and creates a representation of the sequence in the form of a vector.

D. The encoder processes the input sequence and creates a representation of the sequence in the form of a matrix.

Correct Answer: A  
Explanation: The encoder is responsible for processing the input sequence and creating a representation of the sequence. The other options either misrepresent the role or are factually incorrect.  

Question 3: What is the purpose of the attention mechanism in the Transformer architecture?

A. The attention mechanism is used to process sequences of data in a neural network.

B. The attention mechanism is used to build contextual representations of input sequences.

C. The attention mechanism is used to convert text into numerical representations.

D. The attention mechanism is used to encode sequence order by itself.

Correct Answer: B  
Explanation: The attention mechanism is designed to allow each token in a sequence to incorporate information from other tokens in the sequence, which is essential for building contextual representations. The other options either incorrectly describe the purpose or are factually inaccurate.  

Question 4: What is the role of the feed-forward network in the Transformer architecture?

A. The feed-forward network is used to create a residual connection between layers.

B. The feed-forward network is used to process the input sequence and create a representation of the sequence.

C. The feed-forward network is used to convert text into numerical representations.

D. The feed-forward network is used to encode sequence order by itself.

Correct Answer: B  
Explanation: The feed-forward network is responsible for processing the input sequence and creating a representation of the sequence. The other options either incorrectly describe the role or are factually inaccurate.
```

### Reference fact evaluation

**Fact 1:** A Transformer is a neural network architecture designed to process sequences and is widely used in natural language processing.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Transformers use attention mechanisms rather than processing sequence elements only step by step as recurrent neural networks do.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** Text is divided into tokens, and tokens are converted into numerical embeddings.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Positional information is added to represent token order because self-attention alone does not encode sequence order.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Self-attention lets each token representation incorporate information from other tokens in the sequence.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** Scaled dot-product attention uses queries, keys, and values to calculate how information from other tokens is weighted.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Common Transformer layers include attention and feed-forward sublayers, with residual connections and layer normalization.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The original Transformer used an encoder and decoder, while many modern language models use decoder-only architectures.

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

# DL-001 - Transformer Architecture

## Task: FLASHCARD

### Generated output

```text
1. **Question**: What is the primary purpose of a Transformer?  
   **Answer**: To process sequences of data in natural language processing.  

2. **Question**: How does a Transformer differ from a recurrent neural network?  
   **Answer**: Unlike recurrent networks, Transformers use attention mechanisms to model relationships between tokens.  

3. **Question**: What is the role of position information in a Transformer?  
   **Answer**: Positional information is added to represent the order of tokens in the sequence.  

4. **Question**: How does the self-attention mechanism work in a Transformer?  
   **Answer**: In scaled dot-product attention, the model forms queries, keys, and values from token representations, using attention scores to determine how strongly a token uses information from other tokens.  

5. **Question**: What are the key components of a Transformer layer?  
   **Answer**: An attention sublayer and a feed-forward network are included.
```

### Reference fact evaluation

**Fact 1:** A Transformer is a neural network architecture designed to process sequences and is widely used in natural language processing.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** Transformers use attention mechanisms rather than processing sequence elements only step by step as recurrent neural networks do.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** Text is divided into tokens, and tokens are converted into numerical embeddings.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** Positional information is added to represent token order because self-attention alone does not encode sequence order.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** Self-attention lets each token representation incorporate information from other tokens in the sequence.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** Scaled dot-product attention uses queries, keys, and values to calculate how information from other tokens is weighted.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Common Transformer layers include attention and feed-forward sublayers, with residual connections and layer normalization.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** The original Transformer used an encoder and decoder, while many modern language models use decoder-only architectures.

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

# ML-002 - Model Training, Validation, and Overfitting

## Task: SUMMARY

### Generated output

```text
Training a machine learning model involves adjusting its parameters so that predictions become more useful for a task. During training, the model processes examples, produces predictions, and uses a loss function to measure prediction errors. An optimization algorithm then updates the model's parameters to minimize the loss. An epoch is defined as one complete pass through the training dataset.

Data is typically divided into three sets: the training set, the validation set, and the test set. The training set is used to train the model, while the validation set is used to evaluate and refine the model during development. The test set is reserved for final evaluation to assess the model's performance on data it hasn't seen during development.

Overfitting occurs when a model learns too well from the training data, making it poor on new data. Underfitting, on the other hand, means the model is too simple to capture the necessary patterns, leading to poor performance on both training and test data.

To reduce overfitting, techniques such as regularization (discouraging complex model behavior), early stopping (ending training when validation performance plateaus), and data augmentation (adding more diverse examples) are used. These approaches are validated using the validation set, while the test set is reserved for final evaluation.
```

### Reference fact evaluation

**Fact 1:** Training adjusts model parameters to improve predictions for a task.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** A loss function measures prediction error, and an optimization algorithm uses the loss to update model parameters.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** An epoch is one complete pass through the training dataset.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** The training set is used to fit the model.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** The validation set is used during development to compare configurations and make decisions such as hyperparameter selection.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** The test set is held out to estimate performance on data not seen during development.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Overfitting occurs when a model fits training-specific details or noise and generalizes poorly to new examples.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** Underfitting occurs when a model has not learned the patterns needed to perform well, including on training data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 9:** Regularization and early stopping are approaches that can help reduce overfitting.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 10:** The test set should remain reserved for final evaluation rather than repeated model-development decisions.

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

# ML-002 - Model Training, Validation, and Overfitting

## Task: QUIZZ

### Generated output

```text
Question 1: What is the primary purpose of training a machine learning model?  

A. To improve the model's ability to predict new data.  
B. To adjust parameters to minimize error.  
C. To train the model on a single example.  
D. To use only the training data for evaluation.  

Correct Answer: B  
Explanation: Training a machine learning model is primarily to adjust its parameters so that its predictions become more useful for a task. The process involves processing examples, producing predictions, and using a loss function to measure prediction error.  

Question 2: What is the role of a loss function in training a model?  

A. To measure the difference between predicted and actual outputs.  
B. To ensure the model learns the correct patterns.  
C. To update the model's parameters to minimize the loss.  
D. To handle overfitting by discouraging complex behavior.  

Correct Answer: C  
Explanation: The loss function measures prediction error, and during training, it is used to update the model's parameters to minimize this error.  

Question 3: How does an optimization algorithm work during training?  

A. It finds the best parameters that minimize the loss function.  
B. It uses the loss function to adjust parameters in a way that reduces error.  
C. It randomly selects parameters to update.  
D. It ensures the model learns the correct patterns.  

Correct Answer: B  
Explanation: An optimization algorithm, such as gradient descent, uses the loss function to adjust the model's parameters in a way that minimizes the error.  

Question 4: What is the purpose of the validation set in machine learning training?  

A. It is used to evaluate the model's performance on new data.  
B. It is used to compare different configurations of the model.  
C. It is used to train the model on a subset of data.  
D. It is reserved for final evaluation after development.  

Correct Answer: D  
Explanation: The validation set is used during development to compare configurations and make decisions such as selecting hyperparameters. It is reserved for final evaluation after the model has been tested on the test set.  

Question 5: What helps reduce overfitting in machine learning models?  

A. Using more training data.  
B. Applying regularization techniques.  
C. Collecting more representative training data.  
D. Using data augmentation.  

Correct Answer: B  
Explanation: Regularization discourages overly complex model behavior, and early stopping ends training when validation performance stops improving. Collecting more representative training data or using suitable data augmentation can also help reduce overfitting.
```

### Reference fact evaluation

**Fact 1:** Training adjusts model parameters to improve predictions for a task.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** A loss function measures prediction error, and an optimization algorithm uses the loss to update model parameters.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** An epoch is one complete pass through the training dataset.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** The training set is used to fit the model.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** The validation set is used during development to compare configurations and make decisions such as hyperparameter selection.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** The test set is held out to estimate performance on data not seen during development.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Overfitting occurs when a model fits training-specific details or noise and generalizes poorly to new examples.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** Underfitting occurs when a model has not learned the patterns needed to perform well, including on training data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 9:** Regularization and early stopping are approaches that can help reduce overfitting.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 10:** The test set should remain reserved for final evaluation rather than repeated model-development decisions.

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

# ML-002 - Model Training, Validation, and Overfitting

## Task: FLASHCARD

### Generated output

```text
1. **Question:**  
   What is the purpose of a loss function in machine learning?  

   **Answer:**  
   The loss function measures the prediction error and guides the model to improve its performance during training.  

2. **Question:**  
   What is an epoch in machine learning?  

   **Answer:**  
   An epoch is one complete pass through the training dataset.  

3. **Question:**  
   How does the validation set help during development?  

   **Answer:**  
   The validation set is used to compare configurations and make decisions such as selecting hyperparameters.  

4. **Question:**  
   What is overfitting?  

   **Answer:**  
   Overfitting occurs when a model learns details or noise specific to its training data and does not generalize well to new examples.  

5. **Question:**  
   How can overfitting be reduced?  

   **Answer:**  
   Regularization, early stopping, and data augmentation can help reduce overfitting.
```

### Reference fact evaluation

**Fact 1:** Training adjusts model parameters to improve predictions for a task.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 2:** A loss function measures prediction error, and an optimization algorithm uses the loss to update model parameters.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 3:** An epoch is one complete pass through the training dataset.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 4:** The training set is used to fit the model.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 5:** The validation set is used during development to compare configurations and make decisions such as hyperparameter selection.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 6:** The test set is held out to estimate performance on data not seen during development.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 7:** Overfitting occurs when a model fits training-specific details or noise and generalizes poorly to new examples.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 8:** Underfitting occurs when a model has not learned the patterns needed to perform well, including on training data.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 9:** Regularization and early stopping are approaches that can help reduce overfitting.

- [ ] 2 - Correctly covered
- [ ] 1 - Partially covered
- [ ] 0 - Missing
- [ ] Incorrect / contradicted

**Fact 10:** The test set should remain reserved for final evaluation rather than repeated model-development decisions.

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
