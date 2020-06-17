from matplotlib import pyplot as plt
# Comparing plots of software developers

# To see the different styles available in matplotlib
print(plt.style.available) # This is not a method, hence no need for parenthesis
# plt.style.use('fivethirtyeight') # Styles have their own unique line and colour preferences
plt.xkcd() # Make it look like comic book. A method

ages_x= [25,26,27,28,29,30,31,32,33,34,35]

# Python developers
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# another way of denoting colour and linestyle
plt.plot(ages_x, py_dev_y, color= '#000024', linestyle= ':', label= 'python devs')

# Java developers
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, 'g', linewidth= 3, label='java devs') # default linewidth is 1

# All developers
dev_y= [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x,dev_y, 'p--', label= 'All devs', marker=5) # colour, k= black. linestyle,-- = dash

# Labelling
plt.title('Median salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend()

# Formatting
plt.grid(True)
plt.tight_layout()

# Save
# plt.savefig('firstplot.png')
plt.show()