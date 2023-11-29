import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Get the directory of the script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the leaderboard.csv file
leaderboard_file = os.path.join(script_directory, "leaderboard.csv")

# Load data
data = pd.read_csv(leaderboard_file)

# Encode categorical variables
le = LabelEncoder()
data['Username'] = le.fit_transform(data['Username'])

# Split data into features and target variable
X = data[['Username', 'Difficulty', 'Numbers_Missing', 'Numbers_Array', 'Mistake_Count']]
y = data['Time']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Construct the path to the leaderboard_missing_time.csv file
model_file = os.path.join(script_directory, "leaderboard_predicting_time.csv")

# Now, you can use the trained model to predict for individuals with missing values
missing_data = pd.read_csv(model_file)
# missing_data = missing_data.drop(columns=['Time'])
# missing_data.to_csv(missing_data, index=False)

# Encode 'Username' in the missing data using the same LabelEncoder
missing_data['Username'] = le.transform(missing_data['Username'])

# Select the columns used for prediction
prediction_columns = ['Username', 'Difficulty', 'Numbers_Missing', 'Numbers_Array', 'Mistake_Count']

# Use the trained model to predict the 'Time' values for the missing data
predictions = model.predict(missing_data[prediction_columns])

# The 'predictions' variable now contains the predicted 'Time' values for the missing data
print(predictions)
