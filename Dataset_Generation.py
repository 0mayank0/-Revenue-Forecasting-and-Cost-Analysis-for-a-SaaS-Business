import pandas as pd
import numpy as np

# Update the date range to start from 2019 and include 60 months
dates = pd.date_range(start='2019-01-01', periods=60, freq='M')

# Adjusted Subscription Data reflecting growth over the years
data = {
    'Month': dates,

    # Growth in subscribers - reflecting a realistic scenario
    'New_Subscribers_Basic': np.concatenate([
        np.random.randint(500, 1000, size=12),  # 2019
        np.random.randint(800, 1500, size=12),  # 2020 (COVID-19 boost)
        np.random.randint(700, 1200, size=12),  # 2021
        np.random.randint(600, 1100, size=12),  # 2022
        np.random.randint(500, 1000, size=12)  # 2023
    ]),

    'New_Subscribers_Premium': np.concatenate([
        np.random.randint(300, 700, size=12),  # 2019
        np.random.randint(500, 1000, size=12),  # 2020
        np.random.randint(400, 900, size=12),  # 2021
        np.random.randint(350, 800, size=12),  # 2022
        np.random.randint(300, 700, size=12)  # 2023
    ]),

    'New_Subscribers_Enterprise': np.concatenate([
        np.random.randint(50, 200, size=12),  # 2019
        np.random.randint(80, 250, size=12),  # 2020
        np.random.randint(70, 220, size=12),  # 2021
        np.random.randint(60, 200, size=12),  # 2022
        np.random.randint(50, 180, size=12)  # 2023
    ]),

    # Cancellations
    'Cancellations_Basic': np.random.randint(100, 500, size=60),
    'Cancellations_Premium': np.random.randint(50, 300, size=60),
    'Cancellations_Enterprise': np.random.randint(10, 100, size=60),

    # MRR: Average Monthly Recurring Revenue for each segment
    'MRR_Basic': np.concatenate([
        np.random.randint(8000, 20000, size=12),  # 2019
        np.random.randint(10000, 22000, size=12),  # 2020
        np.random.randint(12000, 24000, size=12),  # 2021
        np.random.randint(11000, 23000, size=12),  # 2022
        np.random.randint(10000, 22000, size=12)  # 2023
    ]),

    'MRR_Premium': np.concatenate([
        np.random.randint(20000, 40000, size=12),  # 2019
        np.random.randint(25000, 45000, size=12),  # 2020
        np.random.randint(27000, 47000, size=12),  # 2021
        np.random.randint(26000, 46000, size=12),  # 2022
        np.random.randint(25000, 45000, size=12)  # 2023
    ]),

    'MRR_Enterprise': np.concatenate([
        np.random.randint(50000, 80000, size=12),  # 2019
        np.random.randint(55000, 85000, size=12),  # 2020
        np.random.randint(60000, 90000, size=12),  # 2021
        np.random.randint(58000, 88000, size=12),  # 2022
        np.random.randint(55000, 85000, size=12)  # 2023
    ]),

    # Marketing Spend, higher in 2020 due to competition
    'Marketing_Spend': np.concatenate([
        np.random.randint(10000, 25000, size=12),  # 2019
        np.random.randint(15000, 30000, size=12),  # 2020 (higher spend due to competition)
        np.random.randint(12000, 25000, size=12),  # 2021
        np.random.randint(10000, 20000, size=12),  # 2022
        np.random.randint(9000, 18000, size=12)  # 2023
    ]),

    'New_Customers': np.concatenate([
        np.random.randint(600, 1200, size=12),  # 2019
        np.random.randint(800, 1500, size=12),  # 2020
        np.random.randint(700, 1400, size=12),  # 2021
        np.random.randint(650, 1300, size=12),  # 2022
        np.random.randint(600, 1200, size=12)  # 2023
    ]),

    # Operating Expenses
    'Fixed_Costs': np.random.randint(15000, 30000, size=60),
    'Variable_Costs': np.random.randint(10000, 25000, size=60),

    # Churn Rates
    'Churn_Rate_Basic': np.concatenate([
        np.random.uniform(0.03, 0.06, size=12),  # 2019
        np.random.uniform(0.02, 0.05, size=12),  # 2020
        np.random.uniform(0.03, 0.06, size=12),  # 2021
        np.random.uniform(0.03, 0.06, size=12),  # 2022
        np.random.uniform(0.03, 0.06, size=12)  # 2023
    ]),

    'Churn_Rate_Premium': np.concatenate([
        np.random.uniform(0.01, 0.03, size=12),  # 2019
        np.random.uniform(0.01, 0.02, size=12),  # 2020
        np.random.uniform(0.01, 0.03, size=12),  # 2021
        np.random.uniform(0.01, 0.03, size=12),  # 2022
        np.random.uniform(0.01, 0.03, size=12)  # 2023
    ]),

    'Churn_Rate_Enterprise': np.concatenate([
        np.random.uniform(0.005, 0.02, size=12),  # 2019
        np.random.uniform(0.004, 0.015, size=12),  # 2020
        np.random.uniform(0.005, 0.02, size=12),  # 2021
        np.random.uniform(0.005, 0.02, size=12),  # 2022
        np.random.uniform(0.005, 0.02, size=12)  # 2023
    ]),
}

# Create DataFrame
saas_data = pd.DataFrame(data)

# Adding customer segments and other business metrics
customer_types = ['Small Business', 'Medium Business', 'Enterprise']
regions = ['North America', 'Europe', 'Asia']

saas_data['Customer_Type'] = np.random.choice(customer_types, size=60)
saas_data['Region'] = np.random.choice(regions, size=60)
saas_data['One_Time_Fees'] = np.random.randint(0, 5000, size=60)
saas_data['Discounts_Given'] = np.random.randint(0, 2000, size=60)
saas_data['Churn_Reason'] = np.random.choice(['Price', 'Lack of Features', 'Competitor Product', 'Customer Support'],
                                             size=60)
saas_data['Upsell_Completed'] = np.random.choice([0, 1], size=60)
saas_data['NPS_Score'] = np.random.randint(0, 10, size=60)
saas_data['Monthly_Active_Users'] = (saas_data['New_Subscribers_Basic'] + saas_data['New_Subscribers_Premium'] +
                                     saas_data['New_Subscribers_Enterprise'] - saas_data['Cancellations_Basic'] -
                                     saas_data['Cancellations_Premium'] - saas_data['Cancellations_Enterprise'])

# Refining churn and upsell insights
saas_data['Churn_Recovery_Rate'] = np.random.uniform(0.1, 0.3, size=60)
saas_data['Upsell_Rate'] = np.random.uniform(0.05, 0.15, size=60)
saas_data['Additional_Features_Purchased'] = np.random.randint(0, 5, size=60)

# Save to CSV
saas_data.to_csv('saas_dataset.csv', index=False)

print("SaaS dataset generated and saved to 'saas_dataset.csv'.")
