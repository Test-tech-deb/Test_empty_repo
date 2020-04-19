#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:34:57 2020

@author: Rezvan
"""
import csv

# For IEEE
for index in range(1,9):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/ieee/{index}.csv', mode='r') as original_file:
        csv_reader = csv.DictReader(original_file)        
        
        with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/ieee-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for row in csv_reader:
                file_writer.writerow([row["Document Title"], row["Abstract"] ,row["Publication Year"], row["DOI"] ,'no'])
                
        file.close(); 


# For ACM
for index in range(1,3):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/acm/{index}.csv', mode='r') as original_file:
        csv_reader = csv.DictReader(original_file)        
        
        with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/acm-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for row in csv_reader:
                file_writer.writerow([row["Title"], row["Abstract Note"] ,row["Publication Year"], row["Url"] ,'no'])
                
        file.close(); 
        