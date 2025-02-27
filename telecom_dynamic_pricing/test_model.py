import pytest
from src.model import train_model
import pandas as pd

def test_train_model():
    features = pd.DataFrame({'data_usage': [1.0, 1.5], 'call_usage': [100, 150]})
    target = pd.Series([10, 15])
    model = train_model(features, target)
    assert model is not None
