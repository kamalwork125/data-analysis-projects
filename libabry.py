import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
df=pd.read_csv("aa.csv")
#data cleaning
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df=df.fillna(df.mean(numeric_only=True))
#quantile
numeric_df = df.select_dtypes(include=['int64','float64'])
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).sum()
print("Outliers count:\n", outliers)


# Step 5: Correlation
numeric_df = df.select_dtypes(include=['int64','float64'])

plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# Step 6: Pairplot
sns.pairplot(df)
plt.show()
#scatterplot 
sns.scatterplot(data=df, x="AQI", y="Happiness", hue="City")
plt.title("AQI vs Happiness")
plt.show()
#regraession plot
sns.regplot(data=df, x="Salary", y="Happiness")
plt.title("Salary vs Happiness")
plt.show()
#boxplot
sns.boxplot(data=df, y="Crime_Rate")
plt.title("Crime Rate Distribution")
plt.show()
# Scatter: Salary vs Happiness
px.scatter(df, x="Salary", y="Happiness", color="City",
           hover_data=df.columns,
           title="Interactive — Salary vs Happiness").show()

# Bubble: AQI vs Crime vs Happiness
px.scatter(df, x="AQI", y="Crime_Rate", size="Happiness", color="City",
           title="City Bubble Plot").show()

# Bar: Top Happiness
px.bar(df.sort_values("Happiness", ascending=False),
       x="City", y="Happiness",
       title="Top Happy Cities").show()

# Step 1: X and y
X = df.drop("Happiness", axis=1)
y = df["Happiness"]

# Step 2: Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 4: Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict
pred = model.predict(X_test)

# Step 6: Scores
print("R2 Score:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
# Encoding categorical columns
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])






