# negative test case with light, sub and NO
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
wait = WebDriverWait(browser, 20)
browser.get("http://jamfast20.local:8080/ords/jamfast/r/jamfast")
browser.maximize_window()


Order_Number = " "
Text = " "
qty = " "
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
    global row, ing_name, qty
    # accessing ingredients and qty from the table:
    rows = browser.find_elements(By.XPATH, '//*[@id="143415628672286350_orig"]/tbody/tr')
    for row in rows[1:]:
        ing_name = row.find_element(By.XPATH, 'td[1]').text

        if ingredient == ing_name:
           print("ingredient is", ing_name)
           qty = row.find_element(By.XPATH, 'td[2]').text
           qty = int(qty)
           break
    return qty


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
            print("order name verified in order queue")
            Order_Number = card.find_element(By.XPATH, 'div[2]/div[2]').text
            break

def scanCode():
    # scanning order in station1
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="P2_SCAN_CODE"]'))).send_keys("r")
    browser.find_element(By.XPATH,'//*[@id="P2_SCAN_CODE"]').send_keys(Keys.ENTER)


def getText():
    global Text
    Text = browser.find_element(By.XPATH, '//*[@id="orderAllDetMainCont"]').text
    print(Text)
    text = Text.split("\n")
    return text

def GetQtyOnStation(ingredient, text):
    global Qty
    for i in range(0, len(text)):
        if ingredient == text[i]:
           Qty = text[i-1]
    return Qty

def logout():

    browser.find_element(By.XPATH, '//*[@id="headerCont"]/span[3]').click()
    time.sleep(4)
    browser.find_element(By.XPATH, '//*[@id="logoutBtnSAT"]').click()

def select_order(product,size,Customer_Name):

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="P12_CUSTOMER_NAME"]'))).send_keys(Customer_Name)
    selectProduct(product)
    selectSize(size)
    browser.find_element(By.XPATH, '//*[@id="createOrderBtn"]').click()
    time.sleep(3)

# login to pos
login("pos","pos")

Customer_Name = "Sagane"
product = "Acai Primo Bowl"
size = "Bowl"
Size = size.upper()

# select order details
select_order(product, size,Customer_Name)
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

ingredient_one = "Blueberries"
ingredient_two = "Soymilk"
ingredient_three = "Honey"

# get ingredient qty from table
qty_one = getIngredientQty(ingredient_one)
qty_two = getIngredientQty(ingredient_two)

# select modification ingredient 1
select_Modif_Ingredient(ingredient_one)
select_Modif_Type("LIGHT")
clickaddButton()

# select modification ingredient 2
select_Modif_Ingredient(ingredient_two)
select_Modif_Type("SUB")
clickaddButton()
# select modification ingredient 3
select_Modif_Ingredient(ingredient_three)
select_Modif_Type("NO")
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
time.sleep(20)
verifyName(Customer_Name)

# logging into station1 now
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
wait = WebDriverWait(browser, 25)
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

list = re.findall(r'#\d+',orderNo)
orderNo = "".join(list)
text = getText()

qty_sub = GetQtyOnStation(ingredient_two, text)
time.sleep(3)
# verifying station1 display data
assert station_Name == "LIQUID"
assert product == ProductNameOnScreen
assert size == OrderSizeOnScreen
assert Order_Number == orderNo
assert Customer_Name == CustomerNameOnScreen
assert int(qty_sub) == int(qty_two)

# logout
logout()
browser.refresh()

# logging into station 2
login("station2","s2")
scanCode()
#time.sleep(6)
i = 0
popup = browser.find_element(By.XPATH, '//*[@id="goToTermMsgPopup"]')

# verifying popup message
while i<11:
      try:
         boolean = popup.is_displayed()
         assert boolean == True
         print(boolean)
         message_one = browser.find_element(By.XPATH, '//*[@id="P2_GO_TO_TXT"]').text
         assert message_one  == "Go to"
         message_two = browser.find_element(By.XPATH, '//*[@id = "P2_MESSAGE_1"]').text
         assert message_two == "Fruit - Dip 2"
         break
      except:
         time.sleep(1)
      i = i+ 1

# logout
time.sleep(6)
browser.find_element(By.XPATH, '//*[@id="splashMainCont"]/div[2]/div[2]/span').click()
time.sleep(4)
browser.find_element(By.XPATH, '//*[@id="logoutBtnSAT"]').click()
time.sleep(2)
browser.refresh()

# logging into station 3
login("station3","s3")
#time.sleep(5)
scanCode()
time.sleep(5)
text_two = getText()
qty_Light = GetQtyOnStation(ingredient_one, text_two)
assert int(qty_Light) == int(qty_one/2)

# logout
logout()
browser.refresh()

# logging into station 4
login("station4","s4")
#time.sleep(6)
scanCode()
time.sleep(5)
img = browser.find_element(By.XPATH, '//*[@id="bowlImage"]/img')
boolean = img.is_displayed()

# verifying image of bowl is present or not
assert boolean == True

text = getText()

# verifying that ingredient of NO  should not be displayed
if ingredient_three not in text:
   print("test for NO operation passed")
else:
    print("test for NO operation failed")

logout()
browser.refresh()

# logging into station 5
login("station5","s5")
#time.sleep(6)
scanCode()
time.sleep(6)
station_Name = browser.find_element(By.XPATH, '//*[@id="currTermName"]').text
station5_Text = getText()
Endtime = browser.find_element(By.XPATH, '//*[@id="timer"]').text
print("end time", Endtime)
assert station_Name == "POUR"
assert Endtime != Starttime

EndMessage = Customer_Name + "," +  "\n" + "your" + "\n" + Size + "\n" + product + "\n" + "is ready!"
print(EndMessage)
if EndMessage in Text:
   print("end message verified successfully")
else:
    print("end message verification failed")

logout()
browser.refresh()

login("order_queue","qq")
BodyText = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]'))).text
time.sleep(20)
if Order_Number in BodyText:
   print("order queue verification failed after completing order")

else:
    print("order queue verification passed after completing order")
browser.close()
