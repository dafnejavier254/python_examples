import json

import pandas as pd
from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score
from sklearn.svm import SVR
from sklearn.feature_extraction import DictVectorizer
from feature_extractor import extract_features


def main():

   df = pd.read_csv("fruitfly.tsv", sep"\t")

   # Shuffling data
   df = df.sample(frac=1.0, random_state=1)

   # creating train/test sets
   df_train = df.sample(frac=0.8, random_state=1)
   df_test = df(-df["id"].isin(df_train["id"])]

   # Extract features
   X_train = df_train["text"].apply(extract_features).values
   X_train = vec.fit_transform(X_train)
   X_test = df_test["text"].apply(extract_features.values
   X_test = vec.transform(X_test)
 
 features = [extract_features(text) for text in df["text"]]

