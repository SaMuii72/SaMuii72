import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

df = pd.read_csv("F1.2021.csv")
NumberofChangeaTire = df['Sum']=df.iloc[:,2:21].sum(axis=1)
Name = df['Name']
plt.plot(NumberofChangeaTire,Name,color="#f06292",marker='.')

plt.xlabel('The number of Pit Stops')
plt.ylabel('Name of Grand Prix')
plt.title("How many tires did F1 change?")
plt.grid()
plt.show()

from collections import Counter
df = pd.read_csv("F1.2021.csv")
AllofEachDrivers = df.drop('Number of Laps', axis=1).sum(numeric_only=True)
DriversName = ['Verstappen','Hamilton','Bottas','Perez','Sainz','Norris','Leclerc','Ricciardo','Gasly','Alonso','Ocon','Vettel','Stroll','Tsunoda','Russell','Räikkönen','Latifi','Giovinazzi','Schumacher','Mazepin'] 
plt.plot(AllofEachDrivers,DriversName ,color="#4dd0e1",marker='.')
plt.xlabel('The number of Pit Stops')
plt.ylabel('DriversName')
plt.title("How many tires did F1 change?")
plt.grid()
plt.show()

df = pd.read_csv("F1.2021.csv")
NumberofChangeaTire = df['Sum']=df.iloc[:,2:21].sum(axis=1)
NumberofLaps = df['Number of Laps']
Name = df['Name']
plt.plot(NumberofChangeaTire,Name,color="#9575cd",marker='.',label="Number of Pit Stops")
plt.plot(NumberofLaps,Name,color="#91a7ff",marker='.',linestyle='dotted',label="Number of Laps")

plt.xlabel('the number of Pit Stops and the number of Laps')
plt.ylabel('Name of Grand Prix')
plt.title("the number of Pit Stops VS the number of Laps ")
plt.grid()
plt.legend()
plt.show()

df = pd.read_csv("F1.2021.csv")
NumberofChangeaTire = df['Sum']=df.iloc[:,2:21].sum(axis=1)
NumberofLaps = df['Number of Laps']
Name = df['Name']
plt.plot(NumberofLaps,Name,color="#91a7ff",marker='.',linestyle='dotted')
plt.xlabel('Number of Laps')
plt.ylabel('Name of Grand Prix')
plt.title("Number of Laps for each circuit")
plt.grid()
plt.show()

df = pd.read_csv("F1coner.csv")
corner = df['corner']
Name = df['Name']
plt.plot(corner,Name,color="#ffd54f",marker='.',linestyle='dotted')
plt.xlabel('Number of corners')
plt.ylabel('Name of Grand Prix')
plt.title("Number of corners for each circuit")
plt.grid()
plt.show()

df = pd.read_csv("F1coner.csv")
corner = df['corner']
Name = df['Name']
NumberofChangeaTire = df['Sum']=df.iloc[:,2:21].sum(axis=1)
plt.plot(NumberofChangeaTire,Name,color="#9ccc65",marker='.',label="Number of Pit Stops")
plt.plot(corner,Name,color="#ffd54f",marker='.',linestyle='dotted',label="Number of corners")
plt.xlabel('number of corners and the number of Pit Stops')
plt.ylabel('Name of Grand Prix')
plt.title("the number of Pit Stops VS number of corners for each circuit ")
plt.grid()
plt.legend()
plt.show()

