CREATE DATABASE telecom_pricing;

CREATE TABLE customer_usage (
    customer_id SERIAL PRIMARY KEY,
    plan_id INT,
    data_usage FLOAT,
    call_usage FLOAT,
    month DATE
);

CREATE TABLE pricing_history (
    id SERIAL PRIMARY KEY,
    plan_id INT,
    price FLOAT,
    effective_date DATE
);

CREATE TABLE competitor_pricing (
    competitor_id SERIAL PRIMARY KEY,
    plan_id INT,
    price FLOAT,
    effective_date DATE
);
