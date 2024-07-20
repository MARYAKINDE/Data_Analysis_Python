import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate a dataset for a law firm's case settlement prediction
n = 100  # number of observations

# Generate random data
case_type = np.random.choice(['civil', 'criminal', 'family', 'corporate'], n)
lawyer_experience = np.random.randint(1, 30, n)  # years of experience
claim_amount = np.random.randint(5000, 1000000, n)  # claim amount in dollars
settled = np.random.choice([0, 1], n)  # binary outcome: 1 for settled, 0 for not settled

# Create a DataFrame
law_firm_data = pd.DataFrame({
    'case_type': case_type,
    'lawyer_experience': lawyer_experience,
    'claim_amount': claim_amount,
    'settled': settled
})

# Generate a dataset for an IT company's project delivery prediction
project_size = np.random.choice(['small', 'medium', 'large', 'enterprise'], n)
team_experience = np.random.randint(1, 20, n)  # years of experience
resources = np.random.randint(1, 100, n)  # resources allocated
on_time = np.random.choice([0, 1], n)  # binary outcome: 1 for on time, 0 for late

# Create a DataFrame
it_company_data = pd.DataFrame({
    'project_size': project_size,
    'team_experience': team_experience,
    'resources': resources,
    'on_time': on_time
})

# Save the datasets to CSV files
law_firm_data.to_csv('law_firm_data.csv', index=False)
it_company_data.to_csv('it_company_data.csv', index=False)

# Display the first few rows of both datasets
print("Law Firm Data:")
print(law_firm_data.head())
print("\nIT Company Data:")
print(it_company_data.head())

