import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix

def train_and_evaluate_recall(model, X, y):
    """
    Standardized training and evaluation pipeline.
    Handles scaling, cross-validation, and performance metrics.
    """
    # Split data into 80% training and 20% testing [cite: 738, 1125]
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Apply feature scaling to prevent data leakage [cite: 739, 744]
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train_raw)
    X_test = scaler.transform(X_test_raw)
    
    # Perform 5-fold cross-validation on scaled training data [cite: 745, 746]
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    
    # Fit the model and generate predictions [cite: 749, 752]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Calculate performance metrics [cite: 753, 758]
    metrics = {
        "cv_accuracy": np.mean(cv_scores),
        "test_accuracy": accuracy_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred)
    }
    
    return model, metrics, y_test, y_pred