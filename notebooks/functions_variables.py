# functions_variables.py

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
    def __init__(self, columns):
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
    def __init__(self):
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