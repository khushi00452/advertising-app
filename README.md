# 📊 Advertising Budget → Sales Prediction App

This Streamlit web application predicts product sales based on the amount of money spent on different advertising channels — specifically, **TV**, **Radio**, and **Newspaper**. It uses a **Polynomial Ridge Regression** model trained on the well-known Advertising dataset from the book *An Introduction to Statistical Learning (ISLR)*.

Users can interact with the app through sliders that represent the ad spend on each channel. As the values are adjusted, the app displays a real-time prediction of expected sales, along with a dynamic chart showing the top model coefficients to help explain which features are most influential in the prediction.

---

## 🧠 About the Dataset

The Advertising dataset contains **200 observations** and **4 columns**, representing real-world ad budget allocations and resulting product sales. It is widely used in marketing analytics, statistics, and machine learning courses for understanding linear modeling.

- `TV`: Advertising budget spent on TV (in thousands of dollars)
- `Radio`: Advertising budget spent on Radio (in thousands of dollars)
- `Newspaper`: Advertising budget spent on Newspaper (in thousands of dollars)
- `Sales`: Actual product sales (in thousands of units)

This dataset is simple yet powerful in demonstrating how multi-variable regression models can be applied to real business problems like forecasting and resource allocation.

📥 Dataset download:[https://www.kaggle.com/datasets/sparsht554/sales](https://www.kaggle.com/datasets/sparsht554/sales)

---

## 💻 What the App Does

- Accepts user input for TV, Radio, and Newspaper advertising budgets
- Displays predicted product sales in real time
- Shows the top features affecting the model’s prediction
- Uses a trained **Polynomial Ridge Regression** model for enhanced performance over simple linear models
- Offers an intuitive and interactive experience using **Streamlit**

---

## 🌐 Hosted Application

The app is deployed and accessible via **Streamlit Cloud**.

🔗 Live URL: [https://your-username-advertising-app.streamlit.app](https://advertising-to-sales-predictor.streamlit.app/)  

---

## 🛠️ Built With

- **Python** – programming language
- **Streamlit** – frontend and UI
- **scikit-learn** – model training and evaluation
- **pandas** – data manipulation
- **matplotlib** – data visualization

---

## 🙌 Acknowledgements

This project is built for educational purposes, combining basic regression modeling with a clean and interactive frontend. The dataset comes from the freely available resources accompanying the book.

Built with ❤️ using [Streamlit](https://streamlit.io/)
