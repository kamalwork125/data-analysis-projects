import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from collections import Counter
df = pd.read_csv("netflix_titles.csv",sep='|', engine='python')

df.columns = df.columns.str.strip()
df = df.dropna(how='all')  
df = df.iloc[1:]  
df.columns.tolist()
print(tabulate(df,headers='keys',tablefmt='psql'))
# 1)line chart(How has the number of Netflix releases changed over the years?)
year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o')
plt.title("Number of Netflix Releases Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles Released")
plt.grid(True)
plt.tight_layout()
plt.show()
#2)What is the ratio of Movies vs TV Shows on Netflix?
plt.figure(figsize=(6, 4))
sns.countplot(x='type', data=df, palette='pastel')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
#3)Which are the top 10 countries producing Netflix content?
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_countries.index, y=top_countries.values, palette='pastel')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#4) What are the top 10 most common genres on Netflix?
genre_list = df['listed_in'].dropna().str.split(', ')
flat_genres = [genre for sublist in genre_list for genre in sublist]
top_genres = pd.Series(Counter(flat_genres)).sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='pastel')
plt.title("Top 10 Most Common Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
#5)What is the distribution of movie durations?
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace(' min', '', regex=False).astype(float)
plt.figure(figsize=(10, 5))
sns.histplot(movie_df['duration'], bins=10, kde=True, color='skyblue')
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
