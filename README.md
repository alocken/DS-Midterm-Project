# Data Science Midterm Project

## Project/Goals

The goal of this project is to predict house sold prices using property data including city, state, physical features, and property tags. A secondary objective of this project is to implement learnings of supervised machine learning in a practical example. 

## Process
### Data Loading & Cleaning
-  Loaded the dataset containing property listings including nested JSON fields
-  Determined sold price as the target variable
-  Dropped irrelevant columns
-  Handled missing values by replacing NA/None cells with alternatives
-  Extracted relevant features
-  Cleaned the tags column and ensured consistent formatting for future use
### Exploratory Data Analysis
- Visualized distributions of numeric features
- Plotted scatterplots of key features vs. sold price to see if there was a relationship
- Concatenated relevant OHE tags with target variable
- Created heat maps to identify feature correlations
- Investigated the effect of location and tags on sold house prices
### Scaling and Finishing
- Scaled data and save to preprocessing (.csv)

## Results
### Linear Regressin Model
Trained to predict log-transformed home sale prices to normalize skewed data, reudct outlier impact, and improve model performance. R² score of 0.28 on both the training and test sets indicating it explains about 28% of data variance. Root Mean Squared Error (RMSE) 0.82 indicating predictions fall within 2.3× of the actual prices. Model shows low overfitting and consistent performance between training and testing but R² indicates opportunity for further improvements through feature engineering or using of more complex models (e.g., Gradient Boosting - XGBoost, Random Forest Regressor).

### Random Forest
The Random Forest Regressor results have a mean squared error of 0.18 and a R² Score value of 0.88. This model performs well and predicts 88% of the variance in the target variable of sold_price. This model is generalizing well and not overfitting. 

### XGBoost Regressor
The XGBoost Regressor results have a MSE of 0.04 and a R² Score value of 0.98. The squared differences between predicted and actual values are very small and 98% of the variance in house sale prices is explained by this model. This is a strong performing model. The top feature of price_reduced_amount is showing only weak to moderate correlation with sold_price which suggests that XGBoost is likely capturing non-linear interactions or combinations of features. XGBoost is outperforming Random Forest because it sequentially corrects previous errors and is effective at capturing complex patterns in structured data.

## Challenges 
- Dealing with fragmented and nested JSON fields
- Managing a large number of unique tags and cities 
- Identifying and resolving data leakage variables including within nested features
- 

## Future Goals
(what would you do if you had more time?)
