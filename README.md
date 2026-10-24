# 🎬 Movie Review Sentiment Analysis

A machine learning project that classifies movie reviews as **positive or negative** using Natural Language Processing (NLP). The project includes exploratory data analysis, text preprocessing, feature extraction, model evaluation, and an interactive Streamlit web application.

## 📌 Project Overview

This project explores how machine learning can identify sentiment in movie reviews using the IMDb dataset. The data was explored and visualized, duplicate reviews were removed, and text was converted into numerical features using TF-IDF. Multiple classification models were trained and compared, and the best-performing model was integrated into a Streamlit application for interactive predictions.

## 📊 Dataset

- **Dataset:** IMDb Movie Reviews
- **Original size:** 50,000 reviews
- **After removing duplicates:** 49,582 reviews
- **Target variable:** Sentiment
- **Classes:** Positive and Negative

The dataset contains movie reviews labeled as positive or negative. Duplicate reviews were removed before model training.

**Dataset source:** [IMDb Movie Reviews Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

## 🔍 Workflow

1. **Data Loading and Exploration** — Loaded the dataset and examined its structure, columns, and data types.
2. **Exploratory Data Analysis (EDA)** — Analyzed the dataset and visualized relevant patterns and sentiment distribution using data visualization libraries.
3. **Data Cleaning and Preprocessing** — Removed duplicate reviews and cleaned HTML tags from the review text.
4. **Train-Test Split** — Divided the dataset into training and testing sets using stratified sampling.
5. **Feature Extraction** — Converted text reviews into numerical feature vectors using TF-IDF (Term Frequency–Inverse Document Frequency).
6. **Model Training** — Trained six machine learning classification models.
7. **Model Evaluation and Comparison** — Compared model performance using test accuracy and classification metrics.
8. **Model Selection** — Selected Logistic Regression based on its performance on the test set.
9. **Web Application** — Built an interactive Streamlit app to predict the sentiment of user-provided reviews.

## 🤖 Models Compared

- Logistic Regression
- Linear Support Vector Machine (SVM)
- Multinomial Naive Bayes
- Random Forest
- K-Nearest Neighbors (KNN)
- Decision Tree

## 📈 Model Performance

| Model | Test Accuracy |
|---|---:|
| Logistic Regression | 89.36% |
| Linear SVM | 89.30% |
| Multinomial Naive Bayes | 85.57% |
| Random Forest | 84.58% |
| K-Nearest Neighbors (KNN) | 74.72% |
| Decision Tree | 70.84% |

**Selected model:** Logistic Regression, with a test accuracy of approximately **89.36%**.

These results are based on the train-test split used in this project.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas and NumPy** — Data manipulation and numerical operations
- **Matplotlib and Seaborn** — Data visualization
- **Scikit-learn** — Text vectorization, model training, and evaluation
- **TF-IDF** — Text feature extraction
- **Joblib** — Saving and loading trained model artifacts
- **Streamlit** — Interactive web application
- **Jupyter Notebook** — Development and experimentation

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd movie-review-sentiment-analysis
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## 📁 Project Structure

```text
movie-review-sentiment-analysis/
├── app.py
├── requirements.txt
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── Movie_Review_Sentiment_Analysis.ipynb
└── README.md
```

The notebook filename shown above is an example. Replace it with the actual filename used in the repository.

## 🔮 Future Improvements

- Deploy the Streamlit application online.
- Improve predictions for mixed-sentiment and sarcastic reviews.
- Experiment with additional text preprocessing and feature extraction techniques.
- Explore more advanced NLP models.

## 👩‍💻 Author

Created as a machine learning project to practice exploratory data analysis, NLP, feature extraction, classification, model evaluation, and application development.
