## 2. Introduction to the Data ##

'''
## 这节讲 pd.read_csv()读取两个文件，并显示前五行，非常简单。

'''

import pandas as pd

all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')
#print(all_ages[:5])
print(recent_grads[:5])



## 3. Summarizing Major Categories ##

'''
## 这节讲 pandas.Series.unique()

'''

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())
'''
Output:
['Agriculture & Natural Resources' 'Biology & Life Science' 'Engineering'
 'Humanities & Liberal Arts' 'Communications & Journalism'
 'Computers & Mathematics' 'Industrial Arts & Consumer Services'
 'Education' 'Law & Public Policy' 'Interdisciplinary' 'Health'
 'Social Science' 'Physical Sciences' 'Psychology & Social Work' 'Arts'
 'Business']
'''


aa_cat_counts = dict()
rg_cat_counts = dict()


for row in all_ages['Major_category'].unique():
    major_row = all_ages[all_ages['Major_category'] == row]
    row_ages = major_row['Total']
    aa_cat_counts[row] = row_ages.sum()

print(aa_cat_counts)

for row in recent_grads['Major_category'].unique():
    major_row = recent_grads[recent_grads['Major_category'] == row]
    rg_row = major_row['Total']
    rg_cat_counts[row] = rg_row.sum()
    
print(rg_cat_counts) 
    