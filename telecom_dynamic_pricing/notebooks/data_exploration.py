import pandas as pd

# Load raw data
customer_usage = pd.read_csv('data/raw/customer_usage.csv')
pricing_history = pd.read_csv('data/raw/pricing_history.csv')
competitor_pricing = pd.read_csv('data/raw/competitor_pricing.csv')

# Process customer usage data
def process_customer_usage(df):
    # Example: Convert month to datetime
    df['month'] = pd.to_datetime(df['month'])
    
    # Example: Handle missing values (if any)
    df.fillna(0, inplace=True)  # Replace NaNs with 0

    # Example: Calculate any additional metrics or transformations here
    df['total_usage'] = df['data_usage'] + df['call_usage']  # Example metric
    return df

# Process pricing history data
def process_pricing_history(df):
    # Example: Convert effective_date to datetime
    df['effective_date'] = pd.to_datetime(df['effective_date'])
    
    # Example: Handle missing values (if any)
    df.fillna(df['price'].mean(), inplace=True)  # Replace NaNs with the average price
    
    return df

# Process competitor pricing data
def process_competitor_pricing(df):
    # Example: Convert effective_date to datetime
    df['effective_date'] = pd.to_datetime(df['effective_date'])
    
    # Example: Handle missing values (if any)
    df.fillna(df['price'].mean(), inplace=True)  # Replace NaNs with the average price
    
    return df

# Process the data
processed_customer_usage = process_customer_usage(customer_usage)
processed_pricing_history = process_pricing_history(pricing_history)
processed_competitor_pricing = process_competitor_pricing(competitor_pricing)

# Save processed data to CSV
processed_customer_usage.to_csv('data/processed/processed_customer_usage.csv', index=False)
processed_pricing_history.to_csv('data/processed/processed_pricing_history.csv', index=False)
processed_competitor_pricing.to_csv('data/processed/processed_competitor_pricing.csv', index=False)

print("Processed files saved successfully!")
