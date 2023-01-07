import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv('physionet_A_N.csv')
print(df)

profile = ProfileReport(df, minimal=True)
profile.to_file(output_file = "physionet_minimal.html")
