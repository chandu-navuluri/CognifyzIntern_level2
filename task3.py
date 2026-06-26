#Feature Creation
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset .csv")


# Restaurant Name Length
df['Restaurant_Name_Length'] = (
    df['Restaurant Name']
    .astype(str)
    .apply(len)
)

# Address Length
df['Address_Length'] = (
    df['Address']
    .astype(str)
    .apply(len)
)

print(df[['Restaurant_Name_Length',
          'Address_Length']].head())

# Encoding Table Booking
df['Has_Table_Booking'] = df[
    'Has Table booking'
].map({
    'Yes':1,
    'No':0
})

print(df['Has_Table_Booking'].head())

# Encoding Online Delivery
df['Has_Online_Delivery'] = df[
    'Has Online delivery'
].map({
    'Yes':1,
    'No':0
})

print(df['Has_Online_Delivery'].head())

#Save New Dataset
df.to_csv(
    "restaurant_feature_engineered.csv",
    index=False
)

print("Feature engineered dataset saved.")