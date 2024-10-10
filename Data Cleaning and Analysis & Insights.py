import pandas as pd

# Load the dataset
saas_data = pd.read_csv('saas_dataset.csv')

# Check for missing values
missing_values = saas_data.isnull().sum()

# Display missing values
print("Missing Values in Each Column:\n", missing_values)

# Calculate total subscribers and churn rates
saas_data['Total_Subscribers'] = (
    saas_data['New_Subscribers_Basic'] +
    saas_data['New_Subscribers_Premium'] +
    saas_data['New_Subscribers_Enterprise'] -
    (saas_data['Cancellations_Basic'] +
     saas_data['Cancellations_Premium'] +
     saas_data['Cancellations_Enterprise'])
)

# Calculate total MRR (Monthly Recurring Revenue)
saas_data['Total_MRR'] = (
    saas_data['MRR_Basic'] +
    saas_data['MRR_Premium'] +
    saas_data['MRR_Enterprise']
)

# Calculate Customer Lifetime Value (CLV)
# Assuming an average gross margin of 70%
saas_data['CLV'] = saas_data['Total_MRR'] / saas_data['Churn_Rate_Basic'].replace(0, 0.001)

# Analyze churn rates
avg_churn_basic = saas_data['Churn_Rate_Basic'].mean()
avg_churn_premium = saas_data['Churn_Rate_Premium'].mean()
avg_churn_enterprise = saas_data['Churn_Rate_Enterprise'].mean()

# Display churn rate analysis
print(f"Average Churn Rate for Basic: {avg_churn_basic:.2%}")
print(f"Average Churn Rate for Premium: {avg_churn_premium:.2%}")
print(f"Average Churn Rate for Enterprise: {avg_churn_enterprise:.2%}")

# Analyze new subscribers and cancellations
saas_data['Net_New_Subscribers'] = (
    saas_data['New_Subscribers_Basic'] +
    saas_data['New_Subscribers_Premium'] +
    saas_data['New_Subscribers_Enterprise'] -
    (saas_data['Cancellations_Basic'] +
     saas_data['Cancellations_Premium'] +
     saas_data['Cancellations_Enterprise'])
)

import matplotlib
import matplotlib.pyplot as plt

# Use the Agg backend for non-GUI plotting
matplotlib.use('Agg')

# Create the plot for Total Monthly Recurring Revenue (MRR)
plt.figure(figsize=(14, 7))
plt.plot(saas_data['Month'], saas_data['Total_MRR'], label='Total MRR', marker='o')
plt.title('Total Monthly Recurring Revenue Over Time')
plt.xlabel('Month')
plt.ylabel('Total MRR ($)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the plot to a file
plt.savefig('total_mrr_plot.png')
print("Plot saved as 'total_mrr_plot.png'.")
# Displaying first few rows of the cleaned dataset

# Plot Churn Rates over Time
plt.figure(figsize=(14, 7))
plt.plot(saas_data['Month'], saas_data['Churn_Rate_Basic'], label='Basic', marker='o')
plt.plot(saas_data['Month'], saas_data['Churn_Rate_Premium'], label='Premium', marker='o')
plt.plot(saas_data['Month'], saas_data['Churn_Rate_Enterprise'], label='Enterprise', marker='o')
plt.title('Churn Rate by Subscription Tier Over Time')
plt.xlabel('Month')
plt.ylabel('Churn Rate (%)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
# Save the plot
plt.savefig('churn_rate_analysis.png')
print("Churn Rate plot saved as 'churn_rate_analysis.png'.")

# Plot Net New Subscribers
plt.figure(figsize=(14, 7))
plt.plot(saas_data['Month'], saas_data['Net_New_Subscribers'], label='Net New Subscribers', marker='o')
plt.title('Net New Subscribers Over Time')
plt.xlabel('Month')
plt.ylabel('Net New Subscribers')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig('net_new_subscribers_plot.png')
print("Net New Subscribers plot saved as 'net_new_subscribers_plot.png'.")

# Plot Revenue vs Operating Costs
plt.figure(figsize=(14, 7))
plt.plot(saas_data['Month'], saas_data['Total_MRR'], label='Total Revenue', marker='o')
plt.plot(saas_data['Month'], saas_data['Fixed_Costs'] + saas_data['Variable_Costs'], label='Total Costs', marker='o')
plt.title('Revenue vs Operating Costs Over Time')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig('revenue_vs_costs.png')
print("Revenue vs Costs plot saved as 'revenue_vs_costs.png'.")






# Plot Marketing Spend vs New Customers Acquired
plt.figure(figsize=(14, 7))
plt.plot(saas_data['Month'], saas_data['Marketing_Spend'], label='Marketing Spend', marker='o')
plt.plot(saas_data['Month'], saas_data['New_Customers'], label='New Customers', marker='o')
plt.title('Marketing Spend vs New Customers Acquired Over Time')
plt.xlabel('Month')
plt.ylabel('Amount ($) / Customers')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig('marketing_vs_customers.png')
print("Marketing Spend vs Customers plot saved as 'marketing_vs_customers.png'.")

# Plot Customer Lifetime Value (CLV)
plt.figure(figsize=(14, 7))
plt.plot(saas_data['Month'], saas_data['CLV'], label='Customer Lifetime Value', marker='o')
plt.title('Customer Lifetime Value (CLV) Over Time')
plt.xlabel('Month')
plt.ylabel('CLV ($)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig('clv_plot.png')
print("Customer Lifetime Value (CLV) plot saved as 'clv_plot.png'.")

# Calculate churn rates by customer segment
churn_rates = {
    'Basic': saas_data['Cancellations_Basic'].sum() / saas_data['New_Subscribers_Basic'].sum(),
    'Premium': saas_data['Cancellations_Premium'].sum() / saas_data['New_Subscribers_Premium'].sum(),
    'Enterprise': saas_data['Cancellations_Enterprise'].sum() / saas_data['New_Subscribers_Enterprise'].sum()
}

print("Churn Rates by Segment:", churn_rates)
# Analyze variable costs in relation to new customers
variable_costs_per_customer = saas_data['Variable_Costs'] / saas_data['New_Customers']
plt.figure(figsize=(28, 7))
plt.plot(saas_data['Month'], variable_costs_per_customer, label='Variable Costs per Customer')
plt.title('Variable Costs per New Customer Over Time')
plt.xlabel('Month')
plt.ylabel('Variable Costs ($)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("Cost Analysis")

# Analyze upsell rates
upsell_success_rate = saas_data['Upsell_Completed'].sum() / saas_data['New_Customers'].sum()
print("Upsell Success Rate:", upsell_success_rate)

# Customer willingness to pay analysis (hypothetical, based on customer feedback)
customer_feedback = saas_data[['NPS_Score', 'Upsell_Rate']]

# Visualize NPS scores against upsell rates and save as an image
plt.figure(figsize=(14, 7))
plt.scatter(customer_feedback['NPS_Score'], customer_feedback['Upsell_Rate'], alpha=0.5)
plt.title('NPS Score vs. Upsell Rate')
plt.xlabel('NPS Score')
plt.ylabel('Upsell Rate')
plt.grid()
plt.tight_layout()

# Save the plot as an image
plt.savefig('nps_vs_upsell_rate.png')
print("Plot saved as 'nps_vs_upsell_rate.png'.")

import matplotlib.pyplot as plt

# Calculate churn rates by customer segment
churn_rates = {
    'Basic': saas_data['Cancellations_Basic'].sum() / saas_data['New_Subscribers_Basic'].sum(),
    'Premium': saas_data['Cancellations_Premium'].sum() / saas_data['New_Subscribers_Premium'].sum(),
    'Enterprise': saas_data['Cancellations_Enterprise'].sum() / saas_data['New_Subscribers_Enterprise'].sum()
}

# Plot churn rates
plt.figure(figsize=(10, 6))
plt.bar(churn_rates.keys(), churn_rates.values(), color=['blue', 'green', 'red'])
plt.title('Churn Rates by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Churn Rate')
plt.tight_layout()
plt.savefig('churn_rates_by_segment.png')
print("Churn Rates by Segment plot saved as 'churn_rates_by_segment.png'.")

# Analyze variable costs in relation to new customers
variable_costs_per_customer = saas_data['Variable_Costs'] / saas_data['New_Customers']

plt.figure(figsize=(14, 7))
plt.plot(saas_data['Month'], variable_costs_per_customer, label='Variable Costs per Customer', color='purple')
plt.title('Variable Costs per New Customer Over Time')
plt.xlabel('Month')
plt.ylabel('Variable Costs ($)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('variable_costs_per_customer.png')
print("Variable Costs per Customer plot saved as 'variable_costs_per_customer.png'.")





print(saas_data.head())
