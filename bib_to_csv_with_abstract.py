#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:14:09 2020

@author: rayhan, rezvan
"""

import csv
import bibtexparser
from bibtexparser.bparser import BibTexParser


# For Springerlink
parser = BibTexParser(common_strings=True,
                      ignore_nonstandard_types=True,
                      interpolate_strings=True)
parser.homogenise_fields = True

for index in range(1,22):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/springerlink/{index}.bib') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    
        with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/springer-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for item in bib_database.entries:
                title = item["title"].replace('{','').replace('}','')
                abstract = item["abstract"] if ('abstract' in item.keys() and item["abstract"] != "***") else ""
                year = item["year"] if 'year' in item.keys() else 0000
                url = item["url"] if 'url' in item.keys() else ""
                             
                file_writer.writerow([title, abstract , year, url,'no'])
        
        file.close()
        
# For dblp
parser_dblp = BibTexParser(common_strings=True,
                      ignore_nonstandard_types=True,
                      interpolate_strings=True)
parser_dblp.homogenise_fields = True

#for index in range(1,22):
with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/updated dblp and sciencedirect/dblp.bib') as bibtex_file_dblp:
    bib_database_dblp = bibtexparser.load(bibtex_file_dblp, parser=parser_dblp)

    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/dblp.csv', mode='a') as file:
        file_writer = csv.writer(file, delimiter=',')
        file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
        
        for item in bib_database_dblp.entries:
            title = item["title"].replace('{','').replace('}','')
            abstract = item["abstract"] if ('abstract' in item.keys() and item["abstract"] != "***") else ""
            year = item["year"] if 'year' in item.keys() else 0000
            url = item["url"] if 'url' in item.keys() else ""
            
            file_writer.writerow([title, abstract , year, url,'no'])

    file.close()
    
# For sciencedirect
parser_sd = BibTexParser(common_strings=True,
                      ignore_nonstandard_types=True,
                      interpolate_strings=True)
parser_sd.homogenise_fields = True

#for index in range(1,22):
with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/updated dblp and sciencedirect/sciencedirect.bib') as bibtex_file:
    bib_database_sd = bibtexparser.load(bibtex_file, parser=parser_sd)

    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/sciencedirect.csv', mode='a') as file:
        file_writer = csv.writer(file, delimiter=',')
        file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
        
        for item in bib_database_sd.entries:
            title = item["title"].replace('{','').replace('}','')
            abstract = item["abstract"] if ('abstract' in item.keys() and item["abstract"] != "***") else ""
            year = item["year"] if 'year' in item.keys() else 0000
            url = item["url"] if 'url' in item.keys() else ""
            
            file_writer.writerow([title, abstract , year, url,'no'])

    file.close()
    
#For wiley
parser_wiley = BibTexParser(common_strings=True,
                      ignore_nonstandard_types=True,
                      interpolate_strings=True)
parser_wiley.homogenise_fields = True

for index in range(1,44):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/wiley/computer science/{index}.bib') as bibtex_file:
        bib_database_wiley = bibtexparser.load(bibtex_file, parser=parser_wiley)
    
        with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/wiley-cs-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for item in bib_database_wiley.entries:
                title = item["title"].replace('{','').replace('}','')
                abstract = item["abstract"].replace("Abstract:",'').replace("Abstract",'').replace("ABSTRACT",'').replace("Summary",'').replace("SUMMARY",'') if ('abstract' in item.keys() and item["abstract"] != "***" and item["abstract"] != "No abstract is available for this article.") else ""
                year = item["year"] if 'year' in item.keys() else 0000
                url = item["url"] if 'url' in item.keys() else ""
                
                file_writer.writerow([title, abstract , year, url,'no'])
    
        file.close()
        
for index in range(1,13):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/wiley/general computing/{index}.bib') as bibtex_file:
        bib_database_wiley = bibtexparser.load(bibtex_file, parser=parser_wiley)
    
        with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/wiley-gc-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for item in bib_database_wiley.entries:
                title = item["title"].replace('{','').replace('}','')
                abstract = item["abstract"].replace("Abstract:",'').replace("Abstract",'').replace("ABSTRACT",'').replace("Summary",'').replace("SUMMARY",'') if ('abstract' in item.keys() and item["abstract"] != "***" and item["abstract"] != "No abstract is available for this article.") else ""
                year = item["year"] if 'year' in item.keys() else 0000
                url = item["url"] if 'url' in item.keys() else ""
                
                file_writer.writerow([title, abstract , year, url,'no'])
    
        file.close()
        
for index in range(1,18):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/wiley/others/{index}.bib') as bibtex_file:
        bib_database_wiley = bibtexparser.load(bibtex_file, parser=parser_wiley)
    
        with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/wiley-o-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for item in bib_database_wiley.entries:
                title = item["title"].replace('{','').replace('}','')
                abstract = item["abstract"].replace("Abstract:",'').replace("Abstract",'').replace("ABSTRACT",'').replace("Summary",'').replace("SUMMARY",'') if ('abstract' in item.keys() and item["abstract"] != "***" and item["abstract"] != "No abstract is available for this article.") else ""
                year = item["year"] if 'year' in item.keys() else 0000
                url = item["url"] if 'url' in item.keys() else ""
                
                file_writer.writerow([title, abstract , year, url,'no'])
    
        file.close()


for index in range(1,6):
    with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/wiley/security management/{index}.bib') as bibtex_file:
        bib_database_wiley = bibtexparser.load(bibtex_file, parser=parser_wiley)
    
        with open(f'/Volumes/GoogleDrive/My Drive/Research/Structured data from text/tools/data/for rezvan/csv/wiley-sm-{index}.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Document Title', 'Abstract', 'year', 'pdf Link' ,'label'])
            
            for item in bib_database_wiley.entries:
                title = item["title"].replace('{','').replace('}','')
                abstract = item["abstract"].replace("Abstract:",'').replace("Abstract",'').replace("ABSTRACT",'').replace("Summary",'').replace("SUMMARY",'') if ('abstract' in item.keys() and item["abstract"] != "***" and item["abstract"] != "No abstract is available for this article.") else ""
                year = item["year"] if 'year' in item.keys() else 0000
                url = item["url"] if 'url' in item.keys() else ""
                
                file_writer.writerow([title, abstract , year, url,'no'])
    
        file.close()