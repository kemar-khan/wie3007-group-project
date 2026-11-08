"""Shared evaluation harness so all models are compared fairly."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, confusion_matrix)

RANDOM_STATE = 42
TEST_SIZE = 0.2


def split_data(df: pd.DataFrame, target: str):
    """Stratified train/test split used by every model."""
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=TEST_SIZE,
                            stratify=y, random_state=RANDOM_STATE)


def evaluate(model, X_test, y_test, name: str) -> dict:
    """Return a metrics dict for a fitted binary classifier."""
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
    return {
        "model": name,
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, proba) if proba is not None else None,
    }


def confusion(model, X_test, y_test):
    return confusion_matrix(y_test, model.predict(X_test))
