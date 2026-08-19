import pandas as pd
import sys

print('args:', sys.argv)
month = sys.argv[1]
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(df.head())
print(f'month: {month}')