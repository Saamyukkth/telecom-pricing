-- Insert customer usage data
INSERT INTO customer_usage (plan_id, data_usage, call_usage, month) VALUES
(1, 5.2, 120.5, '2025-01-01'),
(2, 3.8, 98.3, '2025-01-01'),
...

-- Insert pricing history data
INSERT INTO pricing_history (plan_id, price, effective_date) VALUES
(1, 29.99, '2025-01-01'),
(2, 24.99, '2025-01-01'),
...

-- Insert competitor pricing data
INSERT INTO competitor_pricing (plan_id, price, effective_date) VALUES
(1, 27.49, '2025-01-01'),
(2, 22.49, '2025-01-01'),
...
