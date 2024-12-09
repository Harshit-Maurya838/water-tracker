import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('sampledata.xls')
y = df['Liters']
print(y[2].split(','))