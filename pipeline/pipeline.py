import sys
import pandas as pd
import pyarrow

print('arguements', sys.argv[1])

df = pd.DataFrame({'day': [1, 2], 'num_passengers': [3, 4]})
df['month'] = sys.argv[1]
print(df.head())

df.to_parquet('/workspaces/docker-workshop-data-engineeriing-zoomcamp/pipeline/data.parquet')

print('saved to parquet')





