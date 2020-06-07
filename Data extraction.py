import csv
import time
from os import path
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException, TimeoutException, WebDriverException


def parse_category(platform, category, filename, limit):

    try:
        # Click the platform to get data from (IOS or Google play)
        current_platform = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//li[@class="' + platform + '"]')))
        current_platform.click()
        time.sleep(1)

        # Click on the category to get the data from
        current_category = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//li[@data-id="' + category + '"]')))
        current_category.click()
        time.sleep(1)

        # Get to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Click on 500 to get all 500 records on the table
        rows = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//select/option[text()='500']")))
        rows.click()
        time.sleep(1)

        # Get to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")

        # Fetch all the app ranks
        app_ranks = driver.find_elements_by_xpath(
            '//tr[@class="main-row table-row"]/td[@class=" number tbl-col-sort-number"]/span')[0:limit]

        # Fetch all the app names
        app_names = driver.find_elements_by_xpath(
            '//tr[@class="main-row table-row"]/td[@class="app-v2  tbl-col-app-v2"]//descendant::div[@class="app-link-container"]//span')[
                    0:limit]

        # Fetch all the company names
        comp_names = driver.find_elements_by_xpath(
            '//tr[@class="main-row table-row"]/td[@class="app-v2  tbl-col-app-v2"]//descendant::div[@class="company-info"]//span')[
                     0:limit]

        # Fetch all the urls
        urls = driver.find_elements_by_xpath(
            '//tr[@class="main-row table-row"]/td[@class="app-v2  tbl-col-app-v2"]//descendant::div[@class="app-link-container"]/a')[
               0:limit]

        # Transfer current data to yesterday's file
        filename_complete = filename + '.csv'
        if path.exists(filename_complete):
            print('File exists previously')
            old_file = filename
            old_file = old_file + ' Old'
            with open('%s.csv' % filename, 'r', encoding="utf8") as f:
                with open('%s.csv' % old_file, 'w', encoding="utf8") as f1:
                    for line in f:
                        print('Old data')
                        print(line)
                        f1.write(line)

        # Create a new file
        with open('%s.csv' % filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Rank', 'Name', 'Company', 'Link'])

        # Loop through all apps and store in the file
        for app_rank, app_name, comp_name, url in zip(app_ranks, app_names, comp_names, urls):
            print(app_rank.text, app_name.text, comp_name.text, url.get_attribute('href'))
            data = [app_rank.text, app_name.text, comp_name.text, url.get_attribute('href')]
            with open('%s.csv' % filename, 'a', newline='', encoding="utf-8") as f2:
                writer2 = csv.writer(f2)
                writer2.writerow(data)

            time.sleep(0.1)

    except NoSuchElementException:
        print('One of the elements was not found')
    except ElementNotVisibleException:
        print('One of the elements was visible found')
    except TimeoutException:
        print('Timeout! It took too long to load.')
    except StaleElementReferenceException:
        pass
    finally:
        print(traceback.format_exc())


# Initialize driver and go to the web page
try:
    driver = webdriver.Chrome(r'C:\Users\Lenovo\Downloads\chromedriver_win32\chromedriver')
except WebDriverException:
    print('Webdriver not found!')

driver.maximize_window()
url = 'https://www.appannie.com/en/'
driver.get(url)


# Click on login button
login = driver.find_element_by_xpath('//a[@class="square_1vlycxf-o_O-n_1jv8115-o_O-Small_7u8o3i-o_O-Small_1kr48mh-o_O-primary_wyybpq-o_O-white_1qdkg78-o_O-button_d9moc2-o_O-margin_1cxx2lc"]')
login.click()
time.sleep(2)


# Enter credentials and hit submit
username = driver.find_element_by_xpath('//input[@name="username"]')
username.clear()
username.send_keys('timur.asif@techsiders.com')

password = driver.find_element_by_xpath('//input[@type="password"]')
password.clear()
password.send_keys('Test@1234')

submit = driver.find_element_by_xpath('//button[@class="Button__ButtonBlank-sc-1wnez5l-2 Button__UCButton-sc-1wnez5l-9 lcBtUr"]')
submit.click()
time.sleep(2)


# Click Top Charts button
top_charts = driver.find_element_by_xpath('//div[@class="Text-wvugs1-0 platform__GroupItem-sc-4mrpcf-0 fRenhb"][@title="Top Charts"]')
top_charts.click()
time.sleep(2)


# Get IOS data
parse_category('top_ios current', 'Free', 'IOS Free', 500)
parse_category('top_ios current', 'Paid', 'IOS Paid', 500)
parse_category('top_ios current', 'Grossing', 'IOS Grossing', 500)

# Get Google play data
parse_category('top_gp', 'Free', 'Google Play Free', 200)
parse_category('top_gp current', 'Paid', 'Google Play Paid', 200)
parse_category('top_gp current', 'Grossing', 'Google Play Grossing', 200)
parse_category('top_gp current', 'New-Free', 'Google Play New Free', 200)
parse_category('top_gp current', 'New-Paid', 'Google Play New Paid', 200)


time.sleep(5)
driver.close()