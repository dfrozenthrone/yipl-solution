# -*- coding: utf-8 -*-
"""

author: Manish Maharjan
email: dfrozenthrone@gmail.com
"""

import csv

ifile_contracts = open('contracts.csv','rU')
ifile_awards = open('awards.csv','rU')        
ofile = open('result.csv','wb')
reader_contracts = csv.reader(ifile_contracts)
reader_awards = csv.reader(ifile_awards)
writer = csv.writer(ofile)

rownum=1    # Used to track header.

for row in reader_contracts:
    #print row
    if rownum==1:   # Check if line is header
        writer.writerow ('contractname,status,bidPurchaseDeadline,bidSubmissionDeadline,bidOpeningDate,tenderid,publicationDate,publishedIn,contractDate,completionDate,awardee,awardeeLocation,Amount'.split(','))
        rownum+=1
    else:
        # Check if contract has been awarded        
        contractawarded=0
        for i in reader_awards:
            if i[0] == row[0]:
                contractawarded=1
                break
        ifile_awards.seek(0)    # reset the csv iterator
        
                
        # If contract has been awarded        
        if contractawarded==1:
            #row=row+['awarded']
            row = row+i[1:]
            writer.writerow( (row) )
        # If contract has not been awarded print blank
        else:
            row=row+['','','','','']
            writer.writerow( (row) )
            

ifile_contracts.close()
ifile_awards.close()
ofile.close()
