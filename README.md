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
(fill in how your model performed)

## Challenges 
- Dealing with fragmented and nested JSON fields
- Managing a large number of unique tags and cities 

## Future Goals
(what would you do if you had more time?)
