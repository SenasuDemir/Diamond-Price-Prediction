# 💎 Diamond Price Prediction 💵

## 📜 Project Overview

This project aims to develop a predictive model to estimate the price of diamonds based on various physical and qualitative attributes. By utilizing machine learning techniques, the goal is to achieve a high level of accuracy in predicting diamond prices and provide insights into the factors that influence pricing decisions.

## 🧑‍💻 Dataset Description

The dataset consists of detailed information about 53,940 diamonds, including their prices and various physical and qualitative attributes. Below is a summary of the features:

- **price**: 💰 Price of the diamond in US dollars (ranging from 18,823).
- **carat**: ⚖️ Weight of the diamond (ranging from 0.2 to 5.01).
- **cut**: 💎 Quality of the diamond cut, categorized into five levels: Fair, Good, Very Good, Premium, and Ideal.
- **color**: 🌈 Color grade of the diamond, ranging from J (worst) to D (best).
- **clarity**: 🔍 Measure of diamond clarity, with eight levels from I1 (worst) to IF (best).
- **x**: 📏 Length of the diamond in millimeters (ranging from 0 to 10.74).
- **y**: 📐 Width of the diamond in millimeters (ranging from 0 to 58.9).
- **z**: 📏 Depth of the diamond in millimeters (ranging from 0 to 31.8).
- **depth**: 📊 Total depth percentage calculated as 
  \[
  \text{depth} = \frac{2 \cdot z}{x + y}
  \]
  (ranging from 43% to 79%).
- **table**: 🏷️ Width of the top of the diamond relative to its widest point (ranging from 43% to 95%).

This dataset provides a combination of numerical and categorical features, making it suitable for exploratory data analysis, feature engineering, and predictive modeling.

## 🔧 Key Techniques

- **Feature Engineering**: Derived features such as depth percentage.
- **Modeling**: Various regression models were evaluated, including Linear Regression, Ridge, Lasso, Random Forest, and XGBRegressor.
- **Evaluation Metrics**: The performance was evaluated using R², RMSE (Root Mean Squared Error), and MAE (Mean Absolute Error).

## 📈 Results

The performance of different models in predicting diamond prices was assessed, with the following results:

- **XGBRegressor**: Best-performing model with an R² score of **0.9792**, RMSE of **575.19**, and MAE of **293.74**, indicating a high level of accuracy and low error.
- **Random Forest Regressor**: R² score of **0.9747**.
- **Ridge, Linear Regression, Lasso**: These models performed reasonably well but exhibited higher error metrics.

Overall, ensemble methods like XGBRegressor and Random Forest demonstrated superior predictive capabilities for this dataset.

## 🚀 Hugging Face Space

You can try the interactive model for diamond price prediction at the following link:
[Diamond Price Prediction on Hugging Face](https://huggingface.co/spaces/Senasu/Diamond_Price_Prediction)
