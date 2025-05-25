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
- Scaled and save data to preprocessing (.csv)

### Model Selection and Hyperparameter Tuning (Cross-validation)
- Tested three supervised learning models on preprocessed data
- Identified best performing models
- Completed hyperparameter tuning (cross-validation)

## Results
### Linear Regressin Model
Trained to predict log-transformed home sale prices to normalize skewed data, reduce outlier impact, and improve model performance. R² score of 0.28 (training and test sets) explains 28% data variance. Root Mean Squared Error (RMSE) 0.82 indicating predictions fall within 2.3× of the actual prices. Model shows low overfitting and consistent performance between training and testing but, R² indicates opportunity for further improvements through feature engineering or use of a more complex model (e.g., Gradient Boosting - XGBoost, Random Forest Regressor).

### Random Forest
The Random Forest Regressor achieved a Mean Squared Error (MSE) of 0.05 and an R² Score of 0.95, meaning it explains 95% of the variance in the target variable (sold_price). These metrics indicate that the model performs very well on the test data, with minimal prediction error. The model appears to generalize well without overfitting, striking a good balance between bias and variance. This strong performance makes it the best model in this comparison. 

### XGBoost Regressor
XGBoost returned a MSE of 0.08 and an R² Score of 0.91, also indicating strong performance. While it explains 91% of the variance, it was slightly outperformed by Random Forest in both RMSE and R². Notably, XGBoost’s top-ranked feature (price_reduced_amount) showed only weak correlation with sold_price, suggesting the model is effectively capturing non-linear patterns and feature interactions. Despite these strengths, its marginally lower accuracy and higher error rate made Random Forest the preferred model in this case.

### Final Performance: Best Models Hyperparameter Tuning (cross-validation) Outputs
Best performing models completed Hyperparameter tuning on were Random Forest and XGBoost. Random Forest output a lower RMSE (0.2337 vs. 0.2702), indicating better accuracy, and an R² Score that explained more variance (94.17%) than XGBoost (92.20%). Random Forest performed better in both accuracy (lower RMSE) and explanatory power (higher R²). XGBoost was also strong but Random Forest provided precise and consistent dataset predictions.

## Challenges 
- Dealing with fragmented and nested JSON fields
- Managing a large number of unique tags and cities 
- Converting stringified dict, then dict to individual columns to remove and address problematic columns/features
- Identifying and resolving data leakage variables in columns and nested features 

## Future Goals
If more time were available, future steps could include:
- Building a full scikit-learn pipeline for preprocessing and inference
- Incorporating geospatial features (e.g., proximity to amenities)
- Using feature selection techniques to reduce noise
- Deploying the final model via Flask or FastAPI for predictions on new data
- Exploring ensemble stacking of models for improved accuracy