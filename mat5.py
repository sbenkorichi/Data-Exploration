import matplotlib.pyplot as plt 
import pandas as pd

# set directory
df =   pd.read_excel('file1.xlsx', 'Sheet1' )
df1 =  pd.read_excel('file1.xlsx', 'Sheet2' )
df2 =  pd.read_excel('file2.xlsx', 'data' )

# set plot
plt.plot(df['time'], df['person1'], ls='--')
plt.plot(df['time'], df1['person2'], ls=':')
plt.plot(df['time'], df2['person3'])

# set label
plt.xlabel('time(days)')
plt.ylabel('project')
plt.title('Finished projects')
plt.legend()

plt.show()

# File 1 and 2 are attached with the same title.