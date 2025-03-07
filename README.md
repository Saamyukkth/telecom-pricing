# Telecom Dynamic Pricing

## Overview

This project aims to develop a dynamic pricing model for telecom services using machine learning techniques. The objective is to predict customer usage and optimize pricing strategies based on historical data. The project leverages various regression algorithms to analyze customer behavior and provide competitive pricing recommendations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telecom_dynamic_pricing.git
   cd telecom_dynamic_pricing
   ```

2.Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```
   
3.Activate the virtual environment:

   On Windows:
   ```bash
   .\venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   
4.Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5.Usage
To run the data preprocessing scripts and train the models, use the following commands:

Preprocess the data:

python src/data_preprocessing.py

Train the models:

python src/train_models.py
Evaluate the models:

python tests/test_data_preprocessing.py
Models
This project implements several regression models to predict pricing, including:

Linear Regression
Decision Tree Regressor
Random Forest Regressor
Gradient Boosting Regressor
Support Vector Regressor
Each model's performance is evaluated based on Mean Squared Error (MSE) to determine the best approach for dynamic pricing.

Directory Structure
telecom_dynamic_pricing/
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── train_models.py
├── tests/
│   ├── __init__.py
│   └── test_data_preprocessing.py
├── requirements.txt
└── README.md


