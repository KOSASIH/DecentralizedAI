import numpy as np
import pandas as pd

def preprocess_data(data: pd.DataFrame, categorical_features: list, numerical_features: list) -> tuple:
    """
    Preprocess the given dataframe by performing feature engineering, data cleaning, and data normalization.

    Args:
    data (pd.DataFrame): The input dataframe.
    categorical_features (list): A list of categorical feature names.
    numerical_features (list): A list of numerical feature names.

    Returns:
    tuple: A tuple containing the preprocessed dataframe, and the encoded categorical features.
    """

    # Perform feature engineering
    for feature in categorical_features:
        data[feature] = pd.Categorical(data[feature])

    # Perform data cleaning
    data.dropna(inplace=True)

    # Perform data normalization
    numerical_data = data[numerical_features]
    min_values = numerical_data.min()
    max_values = numerical_data.max()
    data[numerical_features] = (numerical_data - min_values) / (max_values - min_values)

    return data, numerical_data

def train_model(X: pd.DataFrame, y: pd.Series, model_type: str) -> object:
    """
    Train a machine learning model based on the given input data and model type.

    Args:
    X (pd.DataFrame): The input data for training the model.
    y (pd.Series): The target variable for training the model.
    model_type (str): The type of machine learning model to train.

    Returns:
    object: A trained machine learning model.
    """

    if model_type == "logistic_regression":
        model = LogisticRegression()
        model.fit(X, y)

    elif model_type == "decision_tree":
        model = DecisionTreeClassifier()
        model.fit(X, y)

    elif model_type == "random_forest":
        model = RandomForestClassifier()
        model.fit(X, y)

    return model

def evaluate_model(model: object, X: pd.DataFrame, y: pd.Series) -> float:
    """
    Evaluate the given machine learning model based on the given input data.

    Args:
    model (object): A trained machine learning model.
    X (pd.DataFrame): The input data for evaluating the model.
    y (pd.Series): The target variable for evaluating the model.

    Returns:
    float: The evaluation metric score for the given machine learning model.
    """

    if hasattr(model, "predict_proba"):
        y_pred = model.predict_proba(X)[:, 1]
        score = roc_auc_score(y, y_pred)
    else:
        y_pred = model.predict(X)
        score = accuracy_score(y, y_pred)

    return score
