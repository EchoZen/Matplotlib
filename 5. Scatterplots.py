import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')
df= pd.read_csv(r'C:\Users\zchen\OneDrive\Documents\Python stuff\Matplotlib\2019-05-31-youtubedata.csv')
views= df['view_count']
likes= df['likes']
ratio= df['ratio']

plt.scatter(views, likes, s=20, # size of marker
            c= 'purple', edgecolors='orange', linewidth=1, alpha=0.85)
plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Age')
plt.ylabel('Number of respondents')
plt.show()