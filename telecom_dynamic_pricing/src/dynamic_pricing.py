from sqlalchemy import create_engine, text
import numpy as np

def adjust_pricing(customer_id, new_data_usage, model, db_connection_string):
    engine = create_engine(db_connection_string)
    with engine.connect() as connection:
        # Fetch current pricing
        result = connection.execute(text("SELECT price FROM pricing_history WHERE plan_id = :id"), {"id": customer_id}).fetchone()
        
        if result is None:
            raise ValueError(f"No pricing information found for plan_id {customer_id}")
        
        current_price = result[0]

        # Prepare features for prediction
        features = np.array([[new_data_usage]])  # Add other features as necessary
        
        # Predict new price
        new_price = model.predict(features)[0]  # Assuming model returns a single price value
        
        # Adjust pricing logic
        if new_price < current_price:
            connection.execute(text("UPDATE pricing_history SET price = :new_price WHERE plan_id = :id"), 
                               {"new_price": new_price, "id": customer_id})
    
    return new_price
