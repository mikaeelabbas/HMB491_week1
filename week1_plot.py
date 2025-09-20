import pandas as pd
import matplotlib.pyplot as plt

df_teeth = pd.read_csv('mammal_teeth.csv') # import dataset as pandas frame

plt.figure(figsize=(5, 10)) # set figure size
plt.scatter(x=df_teeth['Top incisors'],
y=df_teeth['MAMMAL']) # set figure x, y axis
plt.gca().xaxis.set_visible(False)

plt.title("Plot for mammal_teeth dataset, by Mikaeel Abbas") # now includes name
plt.savefig("mammal_teeth_scatterplot.png", dpi=150) # save the figure