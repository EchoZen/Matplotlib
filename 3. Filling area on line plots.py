# Can use fill area to visualise area above or below a certain threshold
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')
data= pd.read_csv(r'C:\Users\zchen\OneDrive\Documents\Python\Matplotlib\dev_salary.csv')
ages= data['Age']
dev_salaries= data['All_Devs']
py_salaries= data['Python']

plt.plot(ages, dev_salaries, linestyle= '--', label= 'All devs')
plt.plot(ages, py_salaries, linestyle= ':', label= 'Python')

# # Fill the entire area under py_salaries
# plt.fill_between(ages, py_salaries, alpha= 0.25) # alpha adjusts the transparency

overall_median= 55700
# Fill area of py_salaries compared to a certain threshold
# plt.fill_between(ages, py_salaries, overall_median, alpha= 0.25)

# # Fill area where py_salaries>overall_median only
# plt.fill_between(ages, py_salaries, overall_median,
#                  where=(py_salaries> overall_median),
#                  interpolate=True, alpha= 0.25)
# # Fill area where py_salaries<overall_median only
# plt.fill_between(ages, py_salaries, overall_median,
#                  where=(py_salaries< overall_median),
#                  interpolate=True, color= 'red', alpha= 0.25)

# Compare python vs all dev salaries visually using fill bytearray
plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries> dev_salaries),
                 interpolate=True, color= 'blue', alpha= 0.25, label='Above avg')
plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries< dev_salaries),
                 interpolate=True, color= 'red', alpha= 0.25, label='Below avg')

plt.legend()
plt.title('Median Salaries (USD) by age')
plt.xlabel('Age')
plt.ylabel('Median Salaries (USD)')
plt.show()