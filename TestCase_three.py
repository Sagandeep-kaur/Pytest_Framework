# add soymilk and light qty - odd number
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
counter = 0
def login(username, password):
    # logging in pos

    browser.find_element(By.XPATH, '//*[@id="PU"]').send_keys(username)
    browser.find_element(By.XPATH, '//*[@id="PS"]').send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="login-btn"]').click()
    time.sleep(15)


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
           #print(qty)
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
    global Order_Number,list
    flag = False
    card_list = browser.find_elements(By.XPATH, '//*[starts-with(@id, "card")]')
    print("total orders are:", len(card_list))
    # verifying order created's name in order queue:
    for card in card_list:

        if Customer_Name in card.text:
           flag = True
           print("order name verified")
           Order_Number = card.find_element(By.XPATH, 'div[2]/div[2]').text
           break

    if flag != True:
        raise Exception("order name not in order queue")

def scanCode():
    # scanning order in station1
    browser.find_element(By.XPATH,'//*[@id="P2_SCAN_CODE"]').send_keys("o")
    browser.find_element(By.XPATH,'//*[@id="P2_SCAN_CODE"]').send_keys(Keys.ENTER)
    #time.sleep(4)

def getText():
    global Text
    Text = browser.find_element(By.XPATH, '//*[@id="orderAllDetMainCont"]').text
    print(Text)
    time.sleep(3)
    text = Text.split("\n")
    #print(text)
    return text

def GetQtyOnStation(ingredient, text):
    global Qty, Qty_prev, counter
    counter = 0
    for i in range(0, len(text)):
        if ingredient == text[i]:
           Qty = text[i-1]
           if Qty == "½" and text[i-2].isnumeric():
              counter = 1
              Qty_prev = int(text[i-2])

    return Qty

def VerifyADDQtyOnStation(ingredient, text, AddCountINg_one):
    global qty_one
    LoopCount = 0

    for i in range(0, len(text)):
        if ingredient == text[i]:
            LoopCount = LoopCount + 1
            Qty = text[i - 1]
            if LoopCount == 1:
               assert int(Qty) == 2 * int(AddCountINg_one)
            else:
               assert int(Qty) == int(qty_one)

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

login("pos","pos")
Customer_Name = "Sagandeepk"
product = "Acai Primo Bowl"
size = "Bowl"
Size = size.upper()
select_order(product,size,Customer_Name)
j = 0
# trying again and agin to click on order as apex doesnt refresh sometimes
while j<5:

 try:
   browser.find_element(By.XPATH, '//*[@id="65000878301180902_orig"]/tbody/tr[2]/td[1]/span').click()
   break

 except:
   browser.refresh()
   select_order(product,size,Customer_Name)
 j = j+1
time.sleep(2)

Qty_prev = 0
AddCountINg_one = 0
ingredient_one = "Soymilk"
ingredient_two = "Strawberries"
# get ingredient qty from table
qty_one = getIngredientQty(ingredient_one)
qty_two = getIngredientQty(ingredient_two)
# select modification for ingredient1
select_Modif_Ingredient(ingredient_one)
select_Modif_Type("ADD")
AddCountINg_one = AddCountINg_one + 1
clickaddButton()
select_Modif_Ingredient(ingredient_one)
select_Modif_Type("ADD")
AddCountINg_one = AddCountINg_one + 1
clickaddButton()
# select modification for ingredient2
select_Modif_Ingredient(ingredient_two)
select_Modif_Type("LIGHT")
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
verifyName(Customer_Name)

# logging into station1 now
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#wait = WebDriverWait(browser, 20)
browser.get("http://jamfast20.local:8080/ords/jamfast/r/jamfast")
browser.maximize_window()
login("station1", "s1")
scanCode()
time.sleep(10)
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
Qty = GetQtyOnStation(ingredient_one, text)

# verify qty added on station 1
VerifyADDQtyOnStation(ingredient_one, text, AddCountINg_one)
time.sleep(4)

# verifying station1 display data
assert station_Name == "LIQUID"
assert product == ProductNameOnScreen
assert size == OrderSizeOnScreen
assert Order_Number == orderNo
assert Customer_Name == CustomerNameOnScreen
#assert int(qty) == int(qty_one)
logout()
time.sleep(2)
browser.refresh()

# logging into station 3

login("station3","s3")
scanCode()
time.sleep(6)
text_two = getText()
Qty_LIGHT = GetQtyOnStation(ingredient_two, text_two)
assert Qty_LIGHT == "½"
if counter == 1:
   assert Qty_prev == (qty_two/2 - 0.5)
time.sleep(6)
logout()
browser.close()


