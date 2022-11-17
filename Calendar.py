


all_dates = browser.find_elements(By.XPATH, "//div[@id='monthwrapper']//tbody//td[@class!='inactiveTD']")
for date in all_dates:
    if date.get_attribute("data-date") == departuredate:
       date.click()
       break