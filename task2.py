#Price Range Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Most Common Price Range
df = pd.read_csv("Dataset .csv")
common_price = df['Price range'].mode()[0]

print("Most Common Price Range:", common_price)

sns.countplot(
    x='Price range',
    data=df
)

plt.title("Distribution of Price Ranges")
plt.show()

#Average Rating per Price Range
avg_rating_price = df.groupby(
    'Price range'
)['Aggregate rating'].mean()

print(avg_rating_price)

avg_rating_price.plot(
    kind='bar'
)

plt.ylabel("Average Rating")
plt.title("Average Rating by Price Range")
plt.show()

#Highest Rated Color
color_rating = df.groupby(
    'Rating color'
)['Aggregate rating'].mean()

print(color_rating.sort_values(ascending=False))

highest_color = color_rating.idxmax()

print("Highest Rated Color:", highest_color)
