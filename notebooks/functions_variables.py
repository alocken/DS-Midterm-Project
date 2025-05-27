"""#def encode_tags(df):

    Use this function to manually encode tags from each sale.
    You could also provide another argument to filter out low 
    counts of tags to keep cardinality to a minimum.
       
    Args:
        pandas.DataFrame

    Returns:
        pandas.DataFrame: modified with encoded tags
#tags = df["tags"].tolist()
# create a unique list of tags and then create a new column for each tag
        
#return df"""

import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class JSONLoader(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        if isinstance(X, str):
            return pd.read_json(X)
        elif isinstance(X, list):
            return pd.DataFrame(X)
        else:
            return X

class TargetEncoder(BaseEstimator, TransformerMixin):
    def init(self, columns):
        self.columns = columns
        self.encodings = {}

    def fit(self, X, y):
        for col in self.columns:
            means = X.groupby(col)[y.name].mean()
            self.encodings[col] = means
        return self

    def transform(self, X):
        X_trans = X.copy()
        for col in self.columns:
            X_trans[col] = X_trans[col].map(self.encodings[col]).fillna(0)
        return X_trans[self.columns]

class TagEncoder(BaseEstimator, TransformerMixin):
    def init(self):
        self.mapping = {}

    def fit(self, X, y=None):
        all_tags = set(tag for tags in X for tag in tags)
        self.mapping = {tag: i for i, tag in enumerate(sorted(all_tags))}
        return self

    def transform(self, X):
        encoded = np.zeros((len(X), len(self.mapping)))
        for i, tags in enumerate(X):
            for tag in tags:
                if tag in self.mapping:
                    encoded[i, self.mapping[tag]] = 1
        return encoded
