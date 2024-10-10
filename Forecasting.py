import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.vector_ar.var_model import VAR
import arch
matplotlib.use('Agg')
# Load the SaaS dataset
saas_data = pd.read_csv('saas_dataset.csv')

# Convert the 'Month' column to datetime format
saas_data['Month'] = pd.to_datetime(saas_data['Month'])
saas_data.set_index('Month', inplace=True)
# Add Total_MRR column by summing MRR_Basic, MRR_Premium, and MRR_Enterprise
saas_data['Total_MRR'] = saas_data['MRR_Basic'] + saas_data['MRR_Premium'] + saas_data['MRR_Enterprise']


# Fit ARIMA model to Total MRR
arima_model = ARIMA(saas_data['Total_MRR'], order=(1,1,1))
arima_result = arima_model.fit()

# Forecast for the next 12 months
forecast_arima = arima_result.forecast(steps=12)
print(forecast_arima)

# Plot the forecast
plt.figure(figsize=(14, 7))
plt.plot(saas_data.index, saas_data['Total_MRR'], label='Observed MRR')
plt.plot(pd.date_range(saas_data.index[-1], periods=12, freq='M'), forecast_arima, label='ARIMA Forecast', color='red')
plt.title('ARIMA Forecast of Total MRR')
plt.xlabel('Month')
plt.ylabel('MRR ($)')
plt.legend()
plt.tight_layout()
plt.savefig('arima_mrr_forecast.png')
print("ARIMA forecast plot saved as 'arima_mrr_forecast.png'.")

# Fit GARCH model to Total MRR
garch_model = arch.arch_model(saas_data['Total_MRR'], vol='Garch', p=1, q=1)
garch_result = garch_model.fit()

# Forecast volatility
garch_forecast = garch_result.forecast(horizon=12)
print(garch_forecast.variance[-1:])

# Plot forecasted volatility
plt.figure(figsize=(14, 7))
plt.plot(pd.date_range(saas_data.index[-1], periods=12, freq='M'), garch_forecast.variance[-1:].T, label='GARCH Forecast')
plt.title('GARCH Forecast of Total MRR Volatility')
plt.xlabel('Month')
plt.ylabel('Volatility ($)')
plt.legend()
plt.tight_layout()
plt.savefig('garch_mrr_volatility.png')
print("GARCH volatility plot saved as 'garch_mrr_volatility.png'.")

# Apply Exponential Smoothing for forecasting
exp_smoothing_model = ExponentialSmoothing(saas_data['Total_MRR'], trend='add', seasonal='add', seasonal_periods=12)
exp_smoothing_result = exp_smoothing_model.fit()

# Forecast for next 12 months
forecast_exp_smoothing = exp_smoothing_result.forecast(12)

# Plot the forecast
plt.figure(figsize=(14, 7))
plt.plot(saas_data.index, saas_data['Total_MRR'], label='Observed MRR')
plt.plot(pd.date_range(saas_data.index[-1], periods=12, freq='M'), forecast_exp_smoothing, label='Exponential Smoothing Forecast', color='red')
plt.title('Exponential Smoothing Forecast of Total MRR')
plt.xlabel('Month')
plt.ylabel('MRR ($)')
plt.legend()
plt.tight_layout()
plt.savefig('exp_smoothing_forecast.png')
print("Exponential Smoothing forecast saved as 'exp_smoothing_forecast.png'.")

# Decompose the Total MRR time series
stl_decompose = seasonal_decompose(saas_data['Total_MRR'], model='additive', period=12)

# Plot the decomposition
plt.figure(figsize=(14, 10))
stl_decompose.plot()
plt.tight_layout()
plt.savefig('stl_mrr_decomposition.png')
print("STL decomposition plot saved as 'stl_mrr_decomposition.png'.")

# Profitability: Forecast profit for next 12 months
# Profit = Total Revenue - Total Costs
profit_forecast = forecast_arima - (saas_data['Fixed_Costs'].iloc[-1] + saas_data['Variable_Costs'].iloc[-1])

# Plot Profit Forecast
plt.figure(figsize=(14, 7))
plt.plot(pd.date_range(saas_data.index[-1], periods=12, freq='M'), profit_forecast, label='Profit Forecast', color='orange')
plt.title('Profit Forecast for the Next 12 Months')
plt.xlabel('Month')
plt.ylabel('Profit ($)')
plt.legend()
plt.tight_layout()
plt.savefig('profit_forecast.png')
print("Profit forecast saved as 'profit_forecast.png'.")

# Cash Flow Forecast
# Cash Flow = Operating Cash Inflows - Operating Cash Outflows
cash_inflows = forecast_arima
cash_outflows = saas_data['Fixed_Costs'].iloc[-1] + saas_data['Variable_Costs'].iloc[-1] + saas_data['Marketing_Spend'].iloc[-1]
cash_flow_forecast = cash_inflows - cash_outflows

# Plot Cash Flow Forecast
plt.figure(figsize=(14, 7))
plt.plot(pd.date_range(saas_data.index[-1], periods=12, freq='M'), cash_flow_forecast, label='Cash Flow Forecast', color='purple')
plt.title('Cash Flow Forecast for the Next 12 Months')
plt.xlabel('Month')
plt.ylabel('Cash Flow ($)')
plt.legend()
plt.tight_layout()
plt.savefig('cash_flow_forecast.png')
print("Cash Flow forecast saved as 'cash_flow_forecast.png'.")

# Sensitivity Analysis: Impact of Churn Rate and Marketing Spend on Profitability

# Define churn and marketing spend scenarios
# Example initialization for current_mrr
current_mrr = saas_data['Total_MRR'].iloc[-1]  # Get the latest Total MRR value

# Define scenarios for marketing spend and churn rate
marketing_spend_scenarios = [0.9, 1.0, 1.1]  # 10% decrease, baseline, and 10% increase
churn_rate_scenarios = [0.02, 0.03, 0.05]  # 2%, 3%, and 5% churn rates

# Initialize a DataFrame to store results
sensitivity_results = pd.DataFrame()

# Iterate through the marketing and churn rate scenarios
for marketing_multiplier in marketing_spend_scenarios:
    for churn_rate in churn_rate_scenarios:
        future_profit = []
        future_mrr = current_mrr
        future_marketing_spend = saas_data['Marketing_Spend'].iloc[-1] * marketing_multiplier

        for month in range(12):  # Forecast for 12 months
            # Calculate profit for the month
            future_mrr = future_mrr * (1 - churn_rate)  # Adjust MRR for churn
            monthly_profit = future_mrr - future_marketing_spend - \
                             saas_data['Fixed_Costs'].iloc[-1] - \
                             saas_data['Variable_Costs'].iloc[-1]
            future_profit.append(monthly_profit)

        # Name for the scenario based on parameters
        scenario_name = f'Marketing_{int(marketing_multiplier * 100)}_Churn_{int(churn_rate * 100)}'
        sensitivity_results[scenario_name] = future_profit

# Prepare the time index for plotting
months = pd.date_range(saas_data.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')

# Plotting Sensitivity Analysis
plt.figure(figsize=(14, 7))
for scenario_name in sensitivity_results.columns:
    plt.plot(months, sensitivity_results[scenario_name], label=scenario_name)

plt.title('Sensitivity Analysis of Profit Forecast (Churn vs Marketing Spend)')
plt.xlabel('Month')
plt.ylabel('Profit ($)')
plt.axhline(0, color='red', linestyle='--', label='Break-even Point')
plt.legend()
plt.grid()
plt.tight_layout()

# Save the plot
plt.savefig('sensitivity_analysis_profit_forecast.png')
print("Sensitivity Analysis plot saved as 'sensitivity_analysis_profit_forecast.png'.")


