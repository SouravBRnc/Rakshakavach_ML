from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from matplotlib import  pyplot as plt
import seaborn as sns

dataset = pd.read_excel('data/ACCIDENT_Data.xlsx')

dataset['weather'] = dataset['weather'].astype(float)
dataset['junction'] = dataset['junction'].astype(float)
dataset['location'] = dataset['location'].astype(float)
dataset['time'] = dataset['time'].astype(float)
dataset['control'] = dataset['control'].astype(float)
dataset['accident'] = dataset['accident'].astype(float)

x = dataset.iloc[1:5001, :-1].values
y = dataset.iloc[1:5001, -1].values

# from sklearn.model_selection import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.25)

classifier =  MLPRegressor()
classifier.fit(x, y)


df = dataset

df['time'] = df['time'].map({
    1:'0600-0900',
    2:'0900-1200',
    3:'1200-1500',
    4:'1500-1800',
    5:'1800-2100',
    6:'2100-0000',
    7:'0000-0300',
    8:'0300-0600',
})

df['weather'] = df['weather'].map({
    1:'Fine',
    2:'Misty/Foggy',
    3:'Cloudy',
    4:'Light rain',
    5:'Heavy rain',
    6:'Flooding',
    7:'Strong wind',
    8:'hot',
    9:'cold'
})

ax = sns.countplot(x="time", data=df, hue="accident", palette="Set2")
ax.set(title="time vs accident", xlabel="time", ylabel="accident")
plt.show()

ax = sns.countplot(x="weather", data=df, hue="accident", palette="Set3")
ax.set(title="weather vs accident", xlabel="weather", ylabel="accident")
plt.show()


def prediction(arr):
    test=arr
    y_pred = classifier.predict(test)
    return (y_pred)
