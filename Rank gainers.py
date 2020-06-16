import pandas as pd
import time
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Google Sheets API setup
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Credentials.json', scope)
client = gspread.authorize(credentials)


# Find Rank gainers for IOS Free
ios_free = pd.read_csv('IOS Free.csv')
ios_free_old = pd.read_csv('IOS Free Old.csv')
sheet = client.open('Jobs Scraper').worksheet('IOS Report')

for key, value in ios_free.iterrows():
    if value['Name'] in ios_free_old['Name'].to_list():
        old_rank = int(ios_free_old['Rank'][ios_free_old.Name == value['Name']])
        if old_rank-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('IOS Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)


# Find Rank gainers for IOS Paid
ios_paid = pd.read_csv('IOS Paid.csv')
ios_paid_old = pd.read_csv('IOS Paid Old.csv')

for key, value in ios_paid.iterrows():
    if value['Name'] in ios_paid_old['Name'].to_list():
        old_rank = int(ios_paid_old['Rank'][ios_paid_old.Name == value['Name']])
        if old_rank-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('IOS Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)


# Find Rank gainers for IOS Grossing
ios_grossing = pd.read_csv('IOS Grossing.csv')
ios_grossing_old = pd.read_csv('IOS Grossing Old.csv')

for key, value in ios_grossing.iterrows():
    if value['Name'] in ios_grossing_old['Name'].to_list():
        old_rank = int(ios_grossing_old['Rank'][ios_grossing_old.Name == value['Name']])
        if old_rank-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('IOS Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)


# Find Rank gainers for Google play free
google_free = pd.read_csv('Google Play Free.csv')
google_free_old = pd.read_csv('Google Play Free Old.csv')
sheet = client.open('Jobs Scraper').worksheet('Google Play Report')

for key, value in google_free.iterrows():
    if value['Name'] in google_free_old['Name'].to_list():
        old_rank = google_free_old['Rank'][google_free_old.Name == value['Name']].index[0]+1
        if int(old_rank)-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)


# Find Rank gainers for Google play paid
google_paid = pd.read_csv('Google Play Paid.csv')
google_paid_old = pd.read_csv('Google Play Paid Old.csv')

for key, value in google_paid.iterrows():
    if value['Name'] in google_paid_old['Name'].to_list():
        old_rank = int(google_paid_old['Rank'][google_paid_old.Name == value['Name']])
        if old_rank-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)


# Find Rank gainers for Google play grossing
google_grossing = pd.read_csv('Google Play Grossing.csv')
google_grossing_old = pd.read_csv('Google Play Grossing Old.csv')

for key, value in google_grossing.iterrows():
    if value['Name'] in google_grossing_old['Name'].to_list():
        old_rank = int(google_grossing_old['Rank'][google_grossing_old.Name == value['Name']])
        if old_rank-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)


# Find Rank gainers for Google play new free
google_new_free = pd.read_csv('Google Play New Free.csv')
google_new_free_old = pd.read_csv('Google Play New Free Old.csv')

for key, value in google_new_free.iterrows():
    if value['Name'] in google_new_free_old['Name'].to_list():
        old_rank = google_new_free_old['Rank'][google_new_free_old.Name == value['Name']].index[0]+1
        if old_rank-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)


# Find Rank gainers for Google play new paid
google_new_paid = pd.read_csv('Google Play New Paid.csv')
google_new_paid_old = pd.read_csv('Google Play New Paid Old.csv')

for key, value in google_new_paid.iterrows():
    if value['Name'] in google_new_paid_old['Name'].to_list():
        old_rank = int(google_new_paid_old['Rank'][google_new_paid_old.Name == value['Name']])
        if old_rank-int(value['Rank']) >= 10:
            data = [value['Rank'], value['Name'], value['Company'], value['Link'], 'Rank gainer']
            sheet.append_row(data)
            time.sleep(1)
            with open('Google Play Report.csv', 'a', newline='', encoding="utf-8") as f:
                writer2 = csv.writer(f)
                writer2.writerow(data)