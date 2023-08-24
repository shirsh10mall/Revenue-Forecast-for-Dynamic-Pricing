# Revenue Forecasting for Dynamic Pricing Optimization


Kaggle Notebook:
1. ML DNN Notebook: https://www.kaggle.com/code/shirshmall/revenue-forecast-for-dynamic-pricing-ml-dnn 
2. AutoML H2O Notebook: https://www.kaggle.com/code/shirshmall/revenue-forecast-for-dynamic-pricing-automl-h2o

## Description

Dynamic pricing has emerged as a pivotal strategy in the realm of online commerce, especially for extensive e-commerce platforms that offer diverse product ranges. This approach entails automated adjustments of product prices to optimize parameters like revenue and gross margin, ultimately aligning with market dynamics. In this project, we delve into the intricate interplay between product attributes and prices to establish an effective foundation for dynamic pricing.

## Objective

The primary objective of this project is to develop a robust revenue forecasting model to facilitate dynamic pricing optimization. By analyzing historical data encompassing user interactions, product attributes, and prices, the model aims to predict revenue per user action during the upcoming month. The goal is to provide insights that enable the e-commerce platform to adjust prices dynamically and maximize revenue.

## Scenario

A fictional mail-order pharmacy employs a dynamic pricing strategy, executing daily automatic price adjustments for its online shop. This project is centered around evaluating the efficacy of this strategy by leveraging data on prices, revenue figures, product attributes, and user behaviors such as clicks, shopping cart assignments, and purchases.

## Data

The project employs real anonymized shop data provided in structured text files. The data sets are organized as follows:

1. Each data set occupies a single line, terminated by "CR" (carriage return), "LF" (line feed), or both.
2. The top line mirrors the structure of the data sets and contains column names.
3. Fields within each data set are separated by the "|" symbol.
4. Floating-point numbers are rounded to two decimal places, with the "." symbol as the decimal separator.
5. The character set employed is ASCII.

The "features.pdf" document offers a comprehensive list of column names in their correct order, along with concise descriptions and value ranges of the associated fields.

## Data Files

- **items.csv:** Lists unchanging product attributes for the learning/classification time periods.
- **train.csv:** Contains evolving information for the learning time period, including user actions and dynamic product attributes.
- **class.csv:** Provides product attributes and prices for the classification time period.

## Model Development

In this comprehensive data science project, I embarked on the task of creating a predictive model tailored to forecast revenue accurately using historical data. The core of the project involved leveraging tree-based algorithms to craft a model that adeptly captures the intricate relationships among diverse factors. By synergizing information sourced from "items.csv" and "train.csv," the objective was to construct a robust mathematical representation capable of predicting revenue with precision.

**Project Steps:**

**1. Data Preprocessing and Exploration:**
The project began with an in-depth exploration of the provided datasets, "items.csv" and "train.csv." After carefully inspecting the data, I meticulously handled missing values by imputing them with the respective mean and mode values. To facilitate the algorithms' input requirements, categorical features underwent encoding, each adhering to the specific needs of the chosen models.

**2. Algorithm Exploration and Selection:**
Multiple tree-based algorithms were thoroughly examined to identify the most proficient performer. The algorithms considered encompassed Decision Trees, Random Forest, LightGBM, CatBoost, and XGBoost. The selection process was driven by the algorithms' abilities to capture non-linear relationships and intricate feature interactions inherent in the data. Among these, XGBoost emerged as the frontrunner due to its exceptional predictive capabilities.

**3. Model Tuning and Hyperparameter Optimization:**
Each algorithm's hyperparameters were systematically tuned using Optuna, a powerful hyperparameter optimization framework. This iterative process ensured that the models' performance was maximized. Additionally, I experimented with a deep neural network for regression and a simple averaging ensemble method for all the algorithms. However, XGBoost consistently outshined the alternatives, displaying superior predictive prowess.

**4. Feature Selection and Insights:**
The selected features' importance for XGBoost was derived using feature importance techniques. This step provided valuable insights into which factors played pivotal roles in revenue prediction. With this knowledge in hand, I proceeded to train the XGBoost model using a cross-validation setup, optimizing its performance further.

**5. Model Deployment via Streamlit:**
To democratize access to the predictive model's insights, a Streamlit app setup was chosen for deployment. Streamlit's interactive and user-friendly nature empowers stakeholders to effortlessly input data and receive revenue forecasts promptly. This deployment strategy ensures that the model's predictive capabilities are harnessed without imposing technical barriers.

**6. H2O's AutoML for Ensemble Models:**
As part of an exploratory effort, I employed H2O's AutoML setup to train a multitude of ensemble models. After rigorous evaluation, a variant of the ensemble model utilizing the Gradient Boosting algorithm exhibited superior performance compared to XGBoost. The incorporation of this ensemble approach provided a comprehensive perspective on revenue prediction.

**7. Model Explainability and Interpretability:**
For enhanced transparency, I employed SHAP (SHapley Additive exPlanations) values to gain insights into the model's predictions and establish its explainability. This step proved pivotal in comprehending the factors driving revenue forecasts.

**8. Evaluation Metrics:**
Throughout the project, the predictive models' performance was evaluated using two key metrics: Root Mean Squared Error (RMSE) and R-squared (R2) scores. These metrics served as quantitative indicators of the models' predictive accuracy and their ability to explain the variance in revenue.

