#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:05:35 2020

@author: rezvan
"""

from os import walk
import csv

csvfilelist = []
#csvfilelistwithoutabstract = []

papertitlelist = []
#papertitlelistwithoutabstract = []

##############
#for (dirpath, dirnames, filenames) in walk('/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv'):
#    csvfilelist.extend(filenames)
#    break

# for (dirpath, dirnames, filenames) in walk('/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/csv files'):
#     csvfilelistwithoutabstract.extend(filenames)
#     break

############## csv files with abstract
count = 0


csv_file = open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/list-without-duplicates.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count == 0:
        # print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        # print(f'{row[0]}')
        papertitlelist.append(row[0].strip().lower())
        line_count += 1
count += line_count

uniquePaperTitleList = set(papertitlelist)

uniques = dict((keys,0) for keys in uniquePaperTitleList)

f_file = open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/missed.csv', mode='w')
file_writer = csv.writer(f_file) #, delimiter=','
file_writer.writerow(['Document Title'])


csv_file = open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/CTI_SLR.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
#line_count = 0
next(csv_reader)
for row in csv_reader:
    if((row[0].strip().lower() in uniques.keys()) and uniques[row[0].strip().lower()] == 0):
        #if(row[1] != "Nothing"):
        uniques[row[0].strip().lower()] = 1
        #file_writer.writerow(row)
        # else:
        #     file_writer.writerow([row[0], " " ,row[2], row[3] ,row[4]])
        #uniques[row[0].strip().lower()] = 1

for key, value in uniques.items():
    if(value == 0): 
        file_writer.writerow([str(key)])            
f_file.close()