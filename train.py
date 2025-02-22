import os
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Ensure 'models' directory exists
os.makedirs("models", exist_ok=True)

# Generate Dummy Data
np.random.seed(42)
data = pd.DataFrame({
    'area': np.random.randint(800, 5000, 100),
    'bedrooms': np.random.randint(1, 5, 100),
    'bathrooms': np.random.randint(1, 4, 100),
    'price': np.random.randint(50000, 500000, 100)
})

# Split Data
X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate Model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Model Trained! Mean Absolute Error: {mae:.2f}")

# Save Model
with open('models/house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model Saved as 'models/house_price_model.pkl'")
