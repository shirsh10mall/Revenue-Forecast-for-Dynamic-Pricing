# Revenue Forecasting for Dynamic Pricing Optimization

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

  The core of this project involves crafting a predictive model using historical data. Leveraging tree-based algorithms, we construct a model that effectively captures the complex relationships between various factors. By integrating information from "items.csv" and "train.csv," we aim to create an accurate mathematical representation for revenue prediction.

Among the tree-based algorithms explored, XGBoost emerged as the most proficient performer, exhibiting superior predictive capabilities. Its ability to handle non-linear relationships and feature interactions significantly contributed to its success in accurately forecasting revenue.

Following model selection and tuning, we transition to the deployment phase. To make the model accessible and user-friendly, we chose to deploy it using a Streamlit app setup. Streamlit's interactive and intuitive nature enables users to effortlessly input data and obtain revenue forecasts. This deployment approach ensures that the predictive power of the model can be harnessed by stakeholders without technical barriers.

