from src.data_preprocessing import load_data, preprocess_customer_usage
from src.model import train_model
from src.dynamic_pricing import adjust_pricing
import pandas as pd

# Your database connection string
db_connection_string = 'postgresql://postgres:admin%40123@localhost:5432/telecom_pricing'

# Load and preprocess data
customer_data, pricing_data, competitor_data = load_data(db_connection_string)
processed_customer_data = preprocess_customer_usage(customer_data)

# Train the model
features = processed_customer_data[['data_usage']]
target = pricing_data['price']
model = train_model(features, target)

# Adjust pricing
new_data_usage = 8  # Example new data usage
customer_id = 6  # Example customer ID

# Use a DataFrame to ensure valid feature names for prediction
features_for_prediction = pd.DataFrame([[new_data_usage]], columns=['data_usage'])
new_price = model.predict(features_for_prediction)[0]  # Get the predicted price

# Optionally, update the pricing in the database or perform additional logic
adjusted_price = adjust_pricing(customer_id, new_data_usage, model, db_connection_string)

print(f'New Price for Customer {customer_id}: {new_price}')
# print(f'Adjusted Price for Customer {customer_id}: {adjusted_price}')
