# positive test case with sub and LIGHT even number qty
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

Order_Number = " "
Text = " "
qty = " "

def login(username, password):

    browser.find_element(By.XPATH, '//*[@id="PU"]').send_keys(username)
    browser.find_element(By.XPATH, '//*[@id="PS"]').send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="login-btn"]').click()

def selectProduct(selectText):
    # selecting product
    select_product = Select(browser.find_element(By.XPATH, '//*[@id="P12_PRODUCT"]'))
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

           qty = row.find_element(By.XPATH, 'td[2]').text
           qty = int(qty)
           print(ingredient,qty)
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
    flag = False
    card_list = browser.find_elements(By.XPATH, '//*[starts-with(@id, "card")]')
    print("total orders are:", len(card_list))
    # verifying order created's name in order queue:
    for card in card_list:

        if Customer_Name in card.text:
            flag = True
            print("order name verified")
            Order_Number = card.find_element(By.XPATH, 'div[2]/div[2]').text

    if flag == False:
        raise Exception("order name not in order queue")

def scanCode():
    # scanning order in station1
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="P2_SCAN_CODE"]'))).send_keys("i")
    browser.find_element(By.XPATH,'//*[@id="P2_SCAN_CODE"]').send_keys(Keys.ENTER)

def getText():
    global Text
    Text = browser.find_element(By.XPATH, '//*[@id="t_PageBody"]').text
    print(Text)
    time.sleep(3)
    text = Text.split("\n")
    return text

def GetQtyOnStation(ingredient, text):
    global Qty
    for i in range(0, len(text)):
        if ingredient == text[i]:

           Qty = text[i-1]
    return Qty


def select_order(product,size,Customer_Name):

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="P12_CUSTOMER_NAME"]'))).send_keys(Customer_Name)
    selectProduct(product)
    selectSize(size)
    browser.find_element(By.XPATH, '//*[@id="createOrderBtn"]').click()
    time.sleep(3)

def logout():

    browser.find_element(By.XPATH, '//*[@id="headerCont"]/span[3]').click()
    time.sleep(4)
    browser.find_element(By.XPATH, '//*[@id="logoutBtnSAT"]').click()

login("pos","pos")
Customer_Name = "Sagan"
time.sleep(4)
product = "Banana Split"
size = "Small"
Size = size.upper()
select_order(product, size, Customer_Name)

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

ingredient_one = "Soymilk"
ingredient_two = "2% Milk"
ingredient_three = "Chocolate Powder"

# get ingredient qty from table
qty_one = getIngredientQty(ingredient_one)
qty_two = getIngredientQty(ingredient_two)
qty_three = getIngredientQty(ingredient_three)
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
select_Modif_Type("STANDARD")
clickaddButton()

# clicking cross button
browser.find_element(By.XPATH, '//*[@id="wwvFlowForm"]/div[3]/div[1]/button').click()

# create button
browser.find_element(By.XPATH, '//*[@id="B65102658859193523"]').click()
time.sleep(8)

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
browser.get("http://jamfast20.local:8080/ords/jamfast/r/jamfast")
browser.maximize_window()

# logging into order queue
login("order_queue","qq")
time.sleep(18)
verifyName(Customer_Name)

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
assert JarImage.is_displayed() == True
list = re.findall(r'#\d+',orderNo)
orderNo = "".join(list)

text = getText()
qty_Light = GetQtyOnStation(ingredient_one, text)
qty_sub = GetQtyOnStation(ingredient_two, text)
qty_Standard = GetQtyOnStation(ingredient_three, text)
time.sleep(3)
# verifying station1 display data
assert station_Name == "LIQUID"
assert product == ProductNameOnScreen
assert size == OrderSizeOnScreen
assert Order_Number == orderNo

assert Customer_Name == CustomerNameOnScreen

# asserting whether ingredient chosen earlier and modified to "light" has correct qty:
assert int(qty_Light) == int(qty_one/2)

assert int(qty_sub) == int(qty_one/2) + int(qty_two)

assert int(qty_Standard) == int(qty_three)

logout()
browser.refresh()

# logging into station 5
login("station5","s5")
scanCode()
time.sleep(6)
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
logout()
browser.refresh()

# logging into order queue again to verify if the scanned out order disappears or not
login("order_queue","qq")
time.sleep(25)
BodyText = browser.find_element(By.XPATH, '//*[@id="main"]/div[2]').text
if Order_Number in BodyText:
   print("order queue verification failed after completing order")

else:
    print("order queue verification passed after completing order")

browser.close()
