### 🎓 **Infosys Springboard Virtual Internship 6.0 Project**

# 🚚 ShipmentSure: Predicting On-Time Delivery Using Supplier Data

Welcome to the official repository for **ShipmentSure**! 🌟 This project is designed to eliminate logistics uncertainty by using Machine Learning to predict whether a shipment will reach its destination on time based on supplier and order-level data.

---

## 🎯 The Mission

The objective of this project is to develop a classification model that predicts delivery delays. By identifying the factors that influence shipping speed, this tool helps firms:

* 
**Evaluate Reliability:** Measure how dependable suppliers actually are in procurement and delivery systems.


* 
**Identify Key Features:** See which factors most influence on-time delivery.


* 
**Real-time Predictions:** Use a **Streamlit** dashboard for instant delivery insights.



---

## 🏗️ System Architecture

The project follows a structured modular pipeline:

1. 
**Data Layer:** Raw data ingestion from the **Kaggle Supply Chain Logistics** dataset followed by cleaning and feature engineering.


2. 
**Model Training Phase:** Splitting data into train-test sets and training algorithms like **Random Forest** and **XGBoost**.


3. 
**Deployment Layer:** A **Streamlit** web interface that processes user inputs to deliver a final prediction: **On-Time** or **Delayed**.



---

## 🛠️ Tech Stack

This project utilizes a modern data science stack:

* **Programming:** Python 🐍
* **Data Handling:** Pandas & NumPy 🐼
* **Visualization:** Seaborn & Matplotlib 📊
* **Modeling:** scikit-learn & XGBoost 🤖
* **Interface:** Streamlit ⚡

---

## 🛤️ Internship Journey (Milestones)

The implementation was divided into four major milestones during the internship period:

| Phase | Module | Key Tasks 📋 |
| --- | --- | --- |
| **Week 1-2** | 🔍 **Data Exploration** | Analyzing schema, handling class imbalances, and performing EDA.

 |
| **Week 3-4** | ⚙️ **Preprocessing** | Encoding categorical variables and scaling numerical features.

 |
| **Week 5-6** | 🧠 **Model Building** | Training Logistic Regression, Random Forest, and XGBoost with GridSearchCV.

 |
| **Week 7-8** | 🚀 **Deployment** | Building the **Streamlit** web app and finalizing documentation.

 |

---

## 📊 Evaluation Metrics

The model's performance is measured using the following standards:

* 
**Accuracy & F1-Score:** To measure overall correctness.


* 
**Precision & Recall:** To understand the balance between false positives and false negatives.


* 
**Confusion Matrix & ROC-AUC:** To visualize classification performance and model discrimination.



---

## 💻 How to Run This Project

1. **Clone the Repo:** `git clone https://github.com/your-username/ShipmentSure.git`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Launch the Dashboard:** `streamlit run app.py` 🎈

---

**This project was successfully completed as part of the Infosys Springboard Virtual Internship 6.0.** 🎓🏢
