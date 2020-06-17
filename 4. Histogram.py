import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')
data= pd.read_csv(r'C:\Users\zchen\OneDrive\Documents\Python\Matplotlib\ages_of_respondents.csv')
ages= data['Age']
responses= data['Responder_id']

# # Python can calculate how many if you specify number of bins
# plt.hist(ages, bins=5, edgecolor= 'black')

# You can also specify your own bin range
bins= [10,20,30,40,50,60,70]
plt.hist(ages, bins, # python doesn't have to guess or give weird cut off for bins
         edgecolor= 'black', log= True) # make it logarithmic so smaller values can be seen
median_age= 29
plt.axvline(median_age, linewidth=2, color='red', label='Age_Median')

plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Age')
plt.ylabel('Number of respondents')
plt.show()