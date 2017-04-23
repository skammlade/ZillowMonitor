# connect to database
# get a list of listings
# for each listing
	# scrape zillow page of listing
	# add contents of scrape to database

import pyodbc
import re
import requests
import time

dbConn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\MSSQLSERVER,1433;DATABASE=Zillow;Trusted_Connection=True', autocommit=True)

cursor = dbConn.cursor()

sql = 'SELECT top 15 URL, ListingID FROM Listing WHERE active=1'

cursor.execute(sql)

for row in cursor.fetchall():
	# print row
	#access the first element of a list
	r = requests.get(row[0])
	# print(r.encoding)
	# print(r.content)
	# currentListingStatus = re.findall('class=\"zsg-icon-for-sale for-sale\"></span> *(.*?) *<span', r.content)[0]
	#(?<=class=\".*status-icon-row )(.*)(?=\-row )
	currentListingStatus = re.findall('(?<=status-icon-row )(.*?)(?=\-row )', r.content)[0]
	# currentListingPrice = re.findall('data-property-value="(.*?)"', r.content)[0]
	currentListingPriceMatches = re.findall('data-property-value="(.*?)"', r.content)
	
	if len(currentListingPriceMatches)>0:
		currentListingPrice = currentListingPriceMatches[0]
		noPriceFound = False
	else:
		currentListingPrice = 0
		noPriceFound = True
		
	if noPriceFound or currentListingStatus == 'off-market':
		sqlActiveUpdate = 'UPDATE Listing SET active=0 WHERE ListingID = ' + str(row[1])
		print(sqlActiveUpdate)
		cursor.execute(sqlActiveUpdate)
		
	
	sqlStatusUpdate = 'INSERT INTO dbo.StatusHistory(listingID, [date], status, price)  VALUES ('+ str(row[1])+', getdate(), \'' + currentListingStatus + '\',' + str(currentListingPrice) + ')'
	print(sqlStatusUpdate)
	cursor.execute(sqlStatusUpdate)
	
	# for status in statusMatches:
		# print(status+','+str(row[1]))
	
	
	time.sleep(5)
	
	
	# data-property-value="(.*?)"
	# data-property-value="([^"]*)"
	# [^aA]*
	# a A aAAAaAAaaaaA

	# cursor.execute("INSERT into dbo.StatusHistory(listingID, [date], status, price) VALUES(row[1], getdate(), status, price) ")
		
# insert into dbo.StatusHistory (listingID, [date], status, price) values (row[1], getdate(), status, price)
# pyodbc execute insert statement

	
		# class=\"zsg-icon-for-sale for-sale\"></span> *(.*?) *<span
	




	
	
	
	#r.text or print r.text encoding
	
#print requests.get(row)
	
#r=requests.get(row)
#r=requests.get(row)

#print(r.text)


#matches = re.findall('gml:pos>(.*?) (.*)</gml', r.text)

#for match in matches:
    #print(match[1]+','+match[0])

	
	