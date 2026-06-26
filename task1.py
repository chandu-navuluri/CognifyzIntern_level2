
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset .csv")

# Percentage calculations
table_booking_pct = (df['Has Table booking'] == 'Yes').mean() * 100
online_delivery_pct = (df['Has Online delivery'] == 'Yes').mean() * 100

print(f"Restaurants with Table Booking: {table_booking_pct:.2f}%")
print(f"Restaurants with Online Delivery: {online_delivery_pct:.2f}%")

#Average Ratings Comparison
booking_rating = df.groupby('Has Table booking')['Aggregate rating'].mean()

print(booking_rating)

booking_rating.plot(
    kind='bar',
    title='Average Rating by Table Booking'
)

plt.ylabel("Average Rating")
plt.show()

#Online Delivery vs Price Range
delivery_price = pd.crosstab(
    df['Price range'],
    df['Has Online delivery']
)

print(delivery_price)

delivery_price.plot(
    kind='bar',
    stacked=True,
    figsize=(8,5)
)

plt.title("Online Delivery Across Price Ranges")
plt.show()
