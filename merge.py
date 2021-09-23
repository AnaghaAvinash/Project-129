#Importing necessary modules
import csv
import pandas as pd

#Naming
file1 = 'bright_stars.csv'
file2 = 'dwarf_stars.csv'

#Making lists
d1 = []
d2 = []


#Adding headers
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)

#Merging and making new list
p_d =[]
h1 = d1[0]
h2 = d2[0]
p_d1 = d1[1:]
p_d2 = d2[1:]
h = h1+h2
p_d =[]

#Making a new CSV
for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
#Finalising
df = pd.read_csv('total_stars.csv')
df.tail(8)