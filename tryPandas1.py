import pandas as pd
df = pd.read_csv('vaccinations.txt')
for i in df['location']:
    print(i)