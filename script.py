# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:43:26 2020

@author: KathanVakharia
"""

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

#extracting data-frame from csv
student_data = pd.read_csv('student_data.csv', index_col=0)


#Making city_count dict from City column
#city_count = {name_of_city:n(students),...}
city_count = Counter(student_data.City)

#setting up the bar plot
plt.figure(figsize=(16,9))
plt.bar(city_count.keys(), city_count.values(), color="Orange")

plt.title("Student distribution", size=25)
plt.xlabel("Name Of the City", size=20)
plt.ylabel("Number of students", size=20)
plt.xticks(size=16)
plt.yticks(size=16)

#Adding text inside bars
offset = 20 
for index, val in enumerate(city_count.values()):
    plt.text(index, val-offset, str(val), size=16, 
             horizontalalignment='center')
    


plt.show()
