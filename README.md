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
### Scaling & Finishing
- Scaled and save data to preprocessing (.csv)

### Model Selection & Hyperparameter Tuning (Cross-validation)
- Tested three supervised learning models on preprocessed data
- Identified best performing models
- Completed hyperparameter tuning

## Results
### Linear Regressin Model
Trained to predict log-transformed home sale prices to normalize skewed data, reduce outlier impact, and improve model performance. R² score of 0.28 (training and test sets) explains 28% data variance. Root Mean Squared Error (RMSE) 0.82 indicating predictions fall within 2.3× of the actual prices. Model shows low overfitting and consistent performance between training and testing but R² indicates opportunity for further improvements through use of a more complex model (e.g., Gradient Boosting - XGBoost, Random Forest Regressor).

### Random Forest
The Random Forest Regressor achieved a Mean Squared Error (MSE) of 0.05, Root Mean Squared Error (RMSE) of 0.23, and an R² Score of 0.95, meaning it explains 95% of the variance in the target variable (sold_price). These metrics indicate that the model performs very well on the test data, with minimal prediction error. The model appears to generalize well without overfitting, striking a good balance between bias and variance. This strong performance makes it the best model in this comparison. 

### XGBoost Regressor
XGBoost returned a MSE of 0.08, RMSE of 0.29, and an R² Score of 0.91, also indicating strong performance. While it explains 91% of the variance, it was slightly outperformed by Random Forest in both RMSE and R². Notably, XGBoost’s top-ranked feature (baths) showed a moderate positive linear relationship with the target variable sold_price. While some features were moderately correlated with sold_price, no single feature demonstrated a very strong correlation suggesting the model is likely capturing non-linear patterns and feature interactions therfore performing well. Despite these strengths, the marginally lower accuracy and higher error rate observed in Random Forest made it the preferred model.

### Final Performance: Best Models Hyperparameter Tuning Outputs
Best performing models completed Hyperparameter tuning on were Random Forest and XGBoost. Random Forest output a lower RMSE (0.2337 vs. 0.2702), indicating better accuracy, and an R² Score that explained more variance (94.17%) than XGBoost (92.20%). Random Forest performed better in both accuracy (lower RMSE) and explanatory power (higher R²). XGBoost was also strong but Random Forest provided precise and consistent dataset predictions.

### Pipeline

Built a machine learning pipeline to predict house prices using JSON-based real estate data.

The pipeline:
- Loads and preprocesses raw data from multiple JSON files
- Extracts features and the target variable (sold_price)
- Handles missing values, scaling, and custom encodings:
- Categorical variables (city, state) are encoded using a custom TargetEncoder
- List-type features (tags) are encoded using a custom TagEncoder
- Trains a RandomForestRegressor model inside a fully scikit-learn compatible Pipeline
- Saves the trained pipeline as a .joblib file in the models/ directory

This ensures a reusable model that prevents data leakage and supports use on new data.

## Challenges 
- Dealing with fragmented and nested JSON fields
- Managing a large number of unique tags and cities 
- Converting stringified dict, then dict to individual columns to remove and address problematic columns/features
- Identifying and resolving data leakage variables in columns and nested features 

## Future Goals
If more time were available, future steps could include:
- Incorporating geospatial features (e.g., proximity to amenities)
- Using feature selection techniques to reduce noise
- Deploying the final model via Flask or FastAPI for predictions on new data
- Exploring ensemble stacking of models for improved accuracy