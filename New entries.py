import pandas as pd
import time
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime


# Google Sheets API setup
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Credentials.json', scope)
client = gspread.authorize(credentials)


# Finding new IOS Free apps
ios_free = pd.read_csv('IOS Free.csv')
ios_free_old = pd.read_csv('IOS Free Old.csv')

with open('IOS Report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['New Rank', 'Previous Rank', 'Name', 'Company', 'Category', 'Link', 'Reason', 'Date stamp'])

sheet = client.open('AppAnnie Scrapper')
sheet.values_clear("'IOS Report'!A1:H1000")
sheet = client.open('AppAnnie Scrapper').worksheet('IOS Report')
sheet.append_row(['New Rank', 'Previous Rank', 'Name', 'Company', 'Category', 'Link', 'Reason', 'Date stamp'])
time.sleep(1)

for index, row in ios_free.iterrows():
    if row['Name'] not in ios_free_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "IOS Free", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('IOS Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)


# Finding new IOS Paid apps
ios_paid = pd.read_csv('IOS Paid.csv')
ios_paid_old = pd.read_csv('IOS Paid Old.csv')

for index, row in ios_paid.iterrows():
    if row['Name'] not in ios_paid_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "IOS Paid", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('IOS Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)


# Finding new IOS Grossing apps
ios_grossing = pd.read_csv('IOS Grossing.csv')
ios_grossing_old = pd.read_csv('IOS Grossing Old.csv')

for index, row in ios_grossing.iterrows():
    if row['Name'] not in ios_grossing_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "IOS Grossing", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('IOS Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)


# Finding new Google play free apps
google_free = pd.read_csv('Google Play Free.csv')
google_free_old = pd.read_csv('Google Play Free Old.csv')

with open('Google Play Report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['New Rank', 'Previous Rank', 'Name', 'Company', 'Category', 'Link', 'Reason', 'Date stamp'])

sheet = client.open('AppAnnie Scrapper')
sheet.values_clear("'Google Play Report'!A1:H1000")
sheet = client.open('AppAnnie Scrapper').worksheet('Google Play Report')
sheet.append_row(['New Rank', 'Previous Rank', 'Name', 'Company', 'Category', 'Link', 'Reason', 'Date stamp'])
time.sleep(1)

for index, row in google_free.iterrows():
    if row['Name'] not in google_free_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "Google Play Free", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)


# Finding new Google play paid apps
google_paid = pd.read_csv('Google Play Paid.csv')
google_paid_old = pd.read_csv('Google Play Paid Old.csv')

for index, row in google_paid.iterrows():
    if row['Name'] not in google_paid_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "Google Play Paid", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)


# Finding new Google play grossing apps
google_grossing = pd.read_csv('Google Play Grossing.csv')
google_grossing_old = pd.read_csv('Google Play Grossing Old.csv')

for index, row in google_grossing.iterrows():
    if row['Name'] not in google_grossing_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "Google Play Grossing", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)


# Finding new Google play new free apps
google_new_free = pd.read_csv('Google Play New Free.csv')
google_new_free_old = pd.read_csv('Google Play New Free Old.csv')

for index, row in google_new_free.iterrows():
    if row['Name'] not in google_new_free_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "Google Play New Free", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)


# Finding new Google play new paid apps
google_new_paid = pd.read_csv('Google Play New Paid.csv')
google_new_paid_old = pd.read_csv('Google Play New Paid Old.csv')

for index, row in google_new_paid.iterrows():
    if row['Name'] not in google_new_paid_old['Name'].to_list():
        x = datetime.datetime.now()
        date = (x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + " " + x.strftime(
            "%H") + ":" + x.strftime("%M") + ":" + x.strftime("%S"))
        data = [row['Rank'], "-", row['Name'], row['Company'], "Google Play New Paid", row['Link'], 'New entry', date]
        sheet.append_row(data)
        time.sleep(1)
        with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f2:
            writer2 = csv.writer(f2)
            writer2.writerow(data)