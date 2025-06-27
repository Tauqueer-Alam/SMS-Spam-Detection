🚫📩 SMS Spam Detection Using NLP and Machine Learning — A Complete Project Overview
By Tauqueer Alam | June 27, 2025

With the increasing use of messaging platforms, spam messages have become a daily nuisance for users. From fake lottery wins to phishing links, spam SMS poses both annoyance and threat. To address this, I developed a Spam SMS Detection System using Natural Language Processing (NLP) and Machine Learning, integrated into a user-friendly web interface using Flask.

In this blog post, I’ll walk you through the motivation, tools, approach, and deployment of this project.

✅ Project Objective
The primary goal of this project is to classify an input SMS message as either "Spam" or "Ham" (not spam). It works by analyzing the content of the text using machine learning models trained on real-world SMS data.

🧠 Tools & Technologies Used
Python – The core programming language

Pandas, NumPy – For data preprocessing

Scikit-learn – For building ML models and vectorization

NLTK – For natural language preprocessing (stopwords, stemming, etc.)

Flask – To build a lightweight web application

HTML/CSS – For the front-end interface

Pickle – For saving and loading the trained model and vectorizer

📊 Dataset Used
I used the SMS Spam Collection Dataset, a popular dataset containing over 5,000 labeled messages (ham or spam). It provided a reliable foundation to train and evaluate the model effectively.

🛠️ Steps Involved
1. Data Preprocessing
Lowercased all text

Removed punctuation and special characters

Tokenized the text

Removed stopwords

Applied stemming using PorterStemmer

2. Feature Extraction
Used TF-IDF Vectorization to convert text into numerical features suitable for ML models.

3. Model Training
Trained multiple models like:

Multinomial Naive Bayes

Logistic Regression

Support Vector Machine

Evaluated using accuracy, precision, recall, and F1-score.

Multinomial Naive Bayes performed best with high accuracy and fast processing.

4. Web App with Flask
Built a user interface where users can enter SMS messages.

On form submission, the message is sent to the Flask backend via a POST request.

The model processes the input and returns whether the message is "Spam" or "Ham".

5. Model Deployment
The trained model and vectorizer were serialized using pickle.

Deployed the complete Flask app on Hugging Face Spaces, making it available online for use.

🌐 User Interface Preview
The interface is clean, responsive, and easy to use. Users can input a message and get real-time feedback on its classification.


🚀 What's Next?
Improve model performance with deep learning approaches like RNNs.

Add language detection for multilingual spam classification.

Deploy the app as a mobile-friendly PWA.

📌 Final Thoughts
This project not only strengthened my understanding of machine learning and NLP, but also gave me hands-on experience with Flask app deployment. I believe such systems can significantly reduce the spread of spam and phishing attempts, especially when embedded in messaging platforms.

If you’re interested in machine learning, this is a great beginner project to explore text classification!
