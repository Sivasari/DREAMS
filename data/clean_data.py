import pandas as pd

# Load the dataset
data = pd.read_csv('data/synthetic_career_data.csv')  # Adjust the path if necessary

# Drop unnecessary columns
columns_to_drop = ['Name', 'Email', 'Current Job Role']
data = data.drop(columns=columns_to_drop, errors='ignore')  # Avoid errors if any column doesn't exist

# Handle missing values
data = data.fillna('Unknown')  # Replace NaN with 'Unknown'

# Print cleaned data
print("Cleaned Dataset (First 5 Rows):")
print(data.head())

# Save the cleaned dataset
data.to_csv('data/cleaned_career_data.csv', index=False)  # Save to the same folder
print("Cleaned data saved to 'data/cleaned_career_data.csv'")


