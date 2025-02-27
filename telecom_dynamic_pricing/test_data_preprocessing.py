import pytest
from src.data_preprocessing import preprocess_customer_usage
import pandas as pd

def test_preprocess_customer_usage():
    sample_data = pd.DataFrame({
        'customer_id': [1, 1, 2, 2],
        'data_usage': [1.0, 1.5, 2.0, 1.5],
        'call_usage': [100, 150, 200, 250],
        'month': ['2025-01-01', '2025-01-01', '2025-01-01', '2025-01-01']
    })
    processed_data = preprocess_customer_usage(sample_data)
    assert processed_data['total_usage'].iloc[0] == 101.0  # 1.0 + 100
