import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.arima.model import ARIMA
import xgboost as xgb

# Loading the meat production dataset
production_df = pd.read_csv('meat_production.csv')

# Converting the Date column to datetime format
production_df['Date'] = pd.to_datetime(production_df['Date'], format='%b-%Y')

# Filling missing data in the Production column using suitable mechanisms
imputer = SimpleImputer(strategy='mean')
production_df['Production'] = imputer.fit_transform(production_df[['Production']])

# Converting the Date column to period with monthly frequency
production_df['Date'] = production_df['Date'].dt.to_period('M')

# Loading the stock price dataset
stock_df = pd.read_csv('stock_prices.csv')

# Converting the Date-Time column to datetime format
stock_df['Date-Time'] = pd.to_datetime(stock_df['Date-Time'], format='%Y-%m-%d')

# Converting the Date-Time column to period with monthly frequency
stock_df['Date'] = stock_df['Date-Time'].dt.to_period('M')

# Merging the datasets on the Date column
merged_df = pd.merge(stock_df, production_df, on='Date', how='inner')

# Selecting relevant columns for analysis
relevant_columns = ['Date', 'Ticker_Symbol', 'Close', 'Production', 'Animal']
merged_df = merged_df[relevant_columns]

# Filling missing data in the Production column using suitable mechanisms
imputer = SimpleImputer(strategy='mean')
merged_df['Production'] = imputer.fit_transform(merged_df[['Production']])

# Ensuring 'Production' and 'Close' columns are numeric
merged_df['Production'] = pd.to_numeric(merged_df['Production'], errors='coerce')
merged_df['Close'] = pd.to_numeric(merged_df['Close'], errors='coerce')

# Dropping rows with any remaining NaN values
merged_df = merged_df.dropna(subset=['Production', 'Close'])

# Splitting the data into training and testing sets
X = merged_df[['Production']]
y = merged_df['Close']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Scatter Plot
plt.figure(figsize=(14, 7))
plt.scatter(merged_df['Production'], merged_df['Close'], alpha=0.5)
plt.xlabel('Meat Production (Million Pounds)')
plt.ylabel('Stock Price')
plt.title('Scatter Plot of Meat Production vs Stock Price')
plt.show()

# Time Series Plot
plt.figure(figsize=(14, 7))
plt.plot(merged_df['Date'].dt.to_timestamp(), merged_df['Production'], label='Meat Production')
plt.plot(merged_df['Date'].dt.to_timestamp(), merged_df['Close'], label='Stock Price')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.title('Time Series Plot of Meat Production and Stock Price')
plt.show()

# Box Plot
plt.figure(figsize=(14, 7))
plt.boxplot([merged_df[merged_df['Production'] < merged_df['Production'].median()]['Close'],
             merged_df[merged_df['Production'] >= merged_df['Production'].median()]['Close']],
            labels=['Low Production', 'High Production'])
plt.xlabel('Meat Production Level')
plt.ylabel('Stock Price')
plt.title('Box Plot of Stock Prices by Meat Production Level')
plt.show()

# Correlation Analysis
correlation = merged_df[['Production', 'Close']].corr()
print(correlation)

# Lagged Analysis
merged_df['Lagged_Production'] = merged_df['Production'].shift(1)
merged_df = merged_df.dropna()

# Performing linear regression with lagged production
X_lagged = merged_df[['Lagged_Production']]
y_lagged = merged_df['Close']
X_train_lagged, X_test_lagged, y_train_lagged, y_test_lagged = train_test_split(X_lagged, y_lagged, test_size=0.2, random_state=42)

model_lagged = LinearRegression()
model_lagged.fit(X_train_lagged, y_train_lagged)
y_pred_lagged = model_lagged.predict(X_test_lagged)

mse_lagged = mean_squared_error(y_test_lagged, y_pred_lagged)
r2_lagged = r2_score(y_test_lagged, y_pred_lagged)

print(f'Lagged Mean Squared Error: {mse_lagged}')
print(f'Lagged R-squared: {r2_lagged}')

# Grouped Analysis
grouped_df = merged_df.groupby('Animal').apply(lambda x: x[['Production', 'Close']].corr().iloc[0, 1])
print(grouped_df)

# Seasonal Analysis
merged_df['Month'] = merged_df['Date'].dt.month

# Ensuring 'Production' and 'Close' columns are numeric
merged_df['Production'] = pd.to_numeric(merged_df['Production'], errors='coerce')
merged_df['Close'] = pd.to_numeric(merged_df['Close'], errors='coerce')

# Dropping rows with any remaining NaN values
merged_df = merged_df.dropna(subset=['Production', 'Close'])

# Aggregating by month and calculating the mean
seasonal_df = merged_df.groupby('Month').agg({'Production': 'mean', 'Close': 'mean'})

plt.figure(figsize=(14, 7))
plt.plot(seasonal_df.index, seasonal_df['Production'], label='Meat Production')
plt.plot(seasonal_df.index, seasonal_df['Close'], label='Stock Price')
plt.xlabel('Month')
plt.ylabel('Values')
plt.legend()
plt.title('Seasonal Trends in Meat Production and Stock Price')
plt.show()

# Random Forest Regressor
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train_lagged, y_train_lagged)
y_pred_rf = model_rf.predict(X_test_lagged)
mse_rf = mean_squared_error(y_test_lagged, y_pred_rf)
r2_rf = r2_score(y_test_lagged, y_pred_rf)
print(f'Random Forest Mean Squared Error: {mse_rf}')
print(f'Random Forest R-squared: {r2_rf}')

# Gradient Boosting Regressor
model_gbm = GradientBoostingRegressor(n_estimators=100, random_state=42)
model_gbm.fit(X_train_lagged, y_train_lagged)
y_pred_gbm = model_gbm.predict(X_test_lagged)
mse_gbm = mean_squared_error(y_test_lagged, y_pred_gbm)
r2_gbm = r2_score(y_test_lagged, y_pred_gbm)
print(f'Gradient Boosting Mean Squared Error: {mse_gbm}')
print(f'Gradient Boosting R-squared: {r2_gbm}')
