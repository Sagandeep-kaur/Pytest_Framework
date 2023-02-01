# positive test case with sub and LIGHT odd number qty
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

options = Options()
options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)


browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
wait = WebDriverWait(browser, 35)
browser.get("http://jamfast20.local:8080/ords/jamfast/r/jamfast")
browser.maximize_window()


def login(username, password):
    # logging in pos

    browser.find_element(By.XPATH, '//*[@id="PU"]').send_keys(username)
    browser.find_element(By.XPATH, '//*[@id="PS"]').send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="login-btn"]').click()


def selectProduct(selectText):
    # selecting product
    select_product = Select(browser.find_element(By.XPATH,'//*[@id="P12_PRODUCT"]'))
    select_product.select_by_visible_text(selectText)
    time.sleep(6)

def selectSize(selectText):
    # selecting size
    select_size = Select(browser.find_element(By.XPATH,'//*[@id="P12_SIZE"]'))
    select_size.select_by_visible_text(selectText)
    time.sleep(6)


def getIngredientQty(ingredient):
    global row, ing_name, qtty
    # accessing ingredients and qty from the table:
    rows = browser.find_elements(By.XPATH, '//*[@id="143415628672286350_orig"]/tbody/tr')
    for row in rows[1:]:
        ing_name = row.find_element(By.XPATH, 'td[1]').text

        if ingredient == ing_name:

           print("ingredient is", ing_name)
           qtty = row.find_element(By.XPATH, 'td[2]').text
           qtty = int(qtty)
           break
    return qtty


def select_Modif_Ingredient(ingredient):
    # adding modification ingredient
    select = Select(browser.find_element(By.XPATH, '//*[@id="P12_ADD_REMOVE"]'))
    select.select_by_visible_text(ingredient)
    time.sleep(4)
    return ingredient

def select_Modif_Type(type):
    select = Select(browser.find_element(By.XPATH, '//*[@id="P12_MOD_TYPE"]'))
    select.select_by_visible_text(type)

def clickaddButton():
    # clicking add button
    browser.find_element(By.XPATH,'//*[@id="B145107395380706807"]').click()
    time.sleep(6)

def verifyName(Customer_Name):
    global Order_Number
    card_list = browser.find_elements(By.XPATH, '//*[starts-with(@id, "card")]')
    print("total orders are:", len(card_list))
    # verifying order created's name in order queue:
    for card in card_list:

        if Customer_Name in card.text:
            print("order name verified")
            Order_Number = card.find_element(By.XPATH, 'div[2]/div[2]').text
            break


def scanCode():
    # scanning order in station
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="P2_SCAN_CODE"]'))).send_keys("w")
    #wabrowser.find_element(By.XPATH,'//*[@id="P2_SCAN_CODE"]').send_keys("w")
    browser.find_element(By.XPATH,'//*[@id="P2_SCAN_CODE"]').send_keys(Keys.ENTER)

def getText():
    global Text
    Text = browser.find_element(By.XPATH, '//*[@id="t_PageBody"]').text
    print(Text)
    time.sleep(3)
    text = Text.split("\n")
    return text

def GetQtyOnStation(ingredient, text):
    global qty
    for i in range(0, len(text)):
        if ingredient == text[i]:
            qty = text[i-1]
            qty = int(qty)

    return qty

def logout():

    browser.find_element(By.XPATH, '//*[@id="headerCont"]/span[3]').click()
    time.sleep(4)
    browser.find_element(By.XPATH, '//*[@id="logoutBtnSAT"]').click()

def select_order(product,size,Customer_Name):

    browser.find_element(By.XPATH, '//*[@id="P12_CUSTOMER_NAME"]').send_keys(Customer_Name)
    selectProduct(product)
    selectSize(size)
    browser.find_element(By.XPATH, '//*[@id="createOrderBtn"]').click()
    time.sleep(3)

qty = " "
qtty = " "
Order_Number = " "
Text = " "

login("pos","pos")
time.sleep(15)
Customer_Name = "Sagandeepka"
product = "Amazing Greens"
size = "Small"
Size = size.upper()
select_order(product,size,Customer_Name)

j = 0
# clicking on order
while j<5:

 try:
   browser.find_element(By.XPATH, '//*[@id="65000878301180902_orig"]/tbody/tr[2]/td[1]/span').click()
   break

 except:
   browser.refresh()
   select_order(product,size,Customer_Name)
 j = j+1

time.sleep(2)
ingredient_one = "Lemonade"
ingredient_two = "Peach Juice"
# get ingredient qty from table
qty_one = getIngredientQty(ingredient_one)
print("qty one is", qty_one)

qty_one = int(qty_one)
qty_two = getIngredientQty(ingredient_two)
print("qty two is", qty_two)

# select modification ingredient1
select_Modif_Ingredient(ingredient_one)
select_Modif_Type("LIGHT")
clickaddButton()
# select modification ingredient2
select_Modif_Ingredient(ingredient_two)
select_Modif_Type("SUB")
clickaddButton()


# clicking cross button
browser.find_element(By.XPATH, '//*[@id="wwvFlowForm"]/div[3]/div[1]/button').click()

# create button
browser.find_element(By.XPATH, '//*[@id="B65102658859193523"]').click()
time.sleep(2)

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
browser.get("http://jamfast20.local:8080/ords/jamfast/r/jamfast")
browser.maximize_window()

# logging into order queue
login("order_queue","qq")
time.sleep(18)
verifyName(Customer_Name)
browser.close()

# logging into station1 now
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
wait = WebDriverWait(browser, 35)
browser.get("http://jamfast20.local:8080/ords/jamfast/r/jamfast")
browser.maximize_window()
login("station1", "s1")
scanCode()
time.sleep(6)
Starttime = browser.find_element(By.XPATH, '//*[@id="timer"]').text
print("starting time", Starttime)


station_Name = browser.find_element(By.XPATH, '//*[@id="currTermName"]').text
ProductNameOnScreen = browser.find_element(By.XPATH, '//*[@id="productName"]').text
OrderSizeOnScreen = browser.find_element(By.XPATH, '//*[@id="orderSizeCont"]').text
CustomerNameOnScreen = browser.find_element(By.XPATH, '//*[@id="custName"]').text
orderNo = browser.find_element(By.XPATH, '//*[@id="orderNoCont"]/span').text

JarImage= browser.find_element(By.XPATH, '//*[@id="jarImg"]')
# verifying jar image is displayed on station 1
assert JarImage.is_displayed() == True

list = re.findall(r'#\d+',orderNo)
orderNo = "".join(list)

text = getText()
print(text)
print(len(text))

qty_Light = GetQtyOnStation(ingredient_one, text)
qty_sub = GetQtyOnStation(ingredient_two, text)
time.sleep(3)


# verifying station1 display data
assert station_Name == "LIQUID"
assert product == ProductNameOnScreen
assert size == OrderSizeOnScreen
assert Order_Number == orderNo
assert Customer_Name == CustomerNameOnScreen

# asserting whether ingredient chosen earlier and modified to "light" has correct qty:

assert int(qty_Light) == int(qty_one/2)
print("qty after Light modification verified successfully on station")

# asserting whether ingredient chosen earlier and modified to "SUB" has correct qty:
assert int(qty_sub) == int(qty_two) + (int(qty_one) - int(qty_one/2))
print("qty after sub modification verified successfully on station")
# logout
logout()
time.sleep(3)
browser.refresh()
# logging into station 5
login("station5","s5")
time.sleep(15)
scanCode()
time.sleep(5)
"""
station_Name = browser.find_element(By.XPATH, '//*[@id="currTermName"]').text
station5_Text = getText()
#print("station5 text is", station5_Text)
Endtime = browser.find_element(By.XPATH, '//*[@id="timer"]').text
print("end time", Endtime)
assert station_Name == "POUR"
assert Endtime != Starttime
str2 = Customer_Name + "," +  "\n" + "your" + "\n" + Size + "\n" + product + "\n" + "is ready!"
print(str2)
if str2 in Text:
   print("end message verified successfully")
else:
    print("end message verification failed")
"""
# logout
logout()
browser.refresh()

# logging into station1 again to verify the "jar unavailable popup" after scan out on station 5
login("station1", "s1")
scanCode()
i = 0
while i<12:
      try:
         popup = browser.find_element(By.XPATH, '//*[@id="wrongTermMsgPopup"]')
         boolean = popup.is_displayed()
         #print(boolean)
         assert boolean == True
         message = browser.find_element(By.XPATH, '//*[@id = "P2_MESSAGE"]').text
         print(message)
         assert message == "Jar unavailable for 30 sec"
         break

      except:
         time.sleep(1)
      i = i+ 1

"""
# loggin into order queue again to verify order disappears after order gets completed
login("order_queue","qq")
BodyText = browser.find_element(By.XPATH, '//*[@id="main"]/div[2]').text
if Order_Number in BodyText:
   print("order queue verification failed after completing order")

else:
    print("order queue verification passed after completing order")
"""