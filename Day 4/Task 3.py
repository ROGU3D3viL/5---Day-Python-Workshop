import pandas as pd
df = pd.DataFrame({'Category' : ['Rent', 'Food', 'Utilities', 'Transport'],
                   'Amount' : [15000, 8000, 2000, 3000]})
print(df)
print(df['Amount'].agg(['sum', 'mean', 'max', 'min'])) # Sum, mean, max, min of the Amount column