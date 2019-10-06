# Data Science Methodology

**Task:** Which topic did you choose to apply the data science methodology to? (2 marks)

**Answer:** I would like to choose topic "Emails".

---

**Task:** Next, you will play the role of the client and the data scientist.

Using the topic that you selected, complete the Business Understanding stage by coming up with a problem that you would like to solve and phrasing it in the form of a question that you will use data to answer. (3 marks)

You are required to:

1. Describe the problem, related to the topic you selected.
2. Phrase the problem as a question to be answered using data.

For example, using the food recipes use case discussed in the labs, the question that we defined was, "Can we automatically determine the cuisine of a given dish based on its ingredients?".

**Answer:**

1. We wanna classify the spam email based on keywords given in its content, title, sender,....
2. Can we automatically determine a spam email based on its contents, title, senders?

---

**Task:** Briefly explain how you would complete each of the following stages for the problem that you described in the Business Understanding stage, so that you are ultimately able to answer the question that you came up with. (5 marks):

1. Analytic Approach
2. Data Requirements
3. Data Collection
4. Data Understanding and Preparation
5. Modeling and Evaluation

You can always refer to the labs as a reference with describing how you would complete each stage for your problem.

**Answer:**

1. Analytic Approach: Beacause we want to classify recieved emails as "yes/no" spam emails where "yes" stands for "it's a spam email" and "no" stands for "it's not a spam email", we need to construct a classification model.

2. Data Requirements: The ingredients we need is the email's components: contents (words, link,...), title, senders, receivers,... We can extract them from the list of given emails.

3. Data Collection: In the cooperation with stage "data requirement", we need to clarify what we obtain are good enougn? For example, which language is considered, encoding/character set, standard format of email address/urls, the already-known info about the email (it's spam or not) to be used in the training/test set,...

4. Data Understanding and Preparation: dealing with missing or invalid values, eliminating duplicates, formatting properly. For example, consider to check if there is urls, photo, script,... in the email. Formatting the contents (there is no wide space or many continuous line breaks), words in uppercase and lowercase are considered the same,... We also consider to choose the useful keywords (not all words indicate the spam),... 

5. Modeling and Evaluation: using algorithms, training set to predict an email to be a spam one or not. Using test set to verify the model and algorithms. We can also use visualisation tools to verify the model.




