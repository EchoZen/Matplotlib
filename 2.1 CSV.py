import csv
from collections import Counter
from matplotlib import pyplot as plt

with open(r'C:\Users\zchen\OneDrive\Documents\Python\Matplotlib\dev_languages.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file) # Grabbing using key value pairs is easier
    row= next(csv_reader)
    # print(row)
    # print(row['LanguagesWorkedWith'].split(';'))

    language_counter= Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

# print(language_counter)
# print(language_counter.most_common(10)) # returns a list of tuples of top 10

languages=[]
popularity=[]
for i in language_counter.most_common(15):
    languages.append(i[0])
    popularity.append(i[1])

languages.reverse()
popularity.reverse()
# print(languages)
# print(popularity)
plt.barh(languages,popularity) # Bar chart is horizontal
plt.xlabel('Popularity')
plt.title('Most popular languages')
plt.show()

