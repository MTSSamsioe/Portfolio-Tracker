import gspread
from google.oauth2.service_account import Credentials
import datetime
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('portfolio_tracker')



def sum_sheet(sheet, range):
    """
    Function that helps sum up cell range in a google sheet
    """
    sum_tot = 0
    for i in SHEET.worksheet(sheet).get_values(range):
        
        sum_tot += float(i[0])
    return sum_tot

def validate_char(input_data, allowed_char):
    """
    Function that compares input_data with list of allowed characters
    """
    forbidden_char = []
    for char in input_data:
        if char not in allowed_char:
            forbidden_char.append(char)
    return forbidden_char  


def nav():

    while True:
        print("\n===================================================================")
        print("\nTo navigate an other section type one of the following commands:")
        print("\n===================================================================")
        print("""\n'dash' --> Go to dashboard 
        \n'add' --> Go to add trade section
        \n'trade' --> Go to trade list section""")
        print("\n================================================")
        nav_input = input("Write navigation command here : ")
        print("\n================================================")
        if nav_input == "dash":
            dashboard()
            break
        elif nav_input == "add":
            update_sheet()
            break
        elif nav_input == "trade":
            trades_list()
            break
        else:
            print("\n================================================")
            print("\nInvalid command please try again")
            print("\n================================================")

# global variables
btc_price = float(SHEET.worksheet("price").get_values("A1")[0][0])
btc_amount = sum_sheet('trades', 'D2:D')


def add_date():
    date = []
    print("Hi what date did you buy your bitcoin? (The format has to be DD-MM-2022) ")
    
    while True:
        try:
            date_input = input("Enter your date here: ")
            datetime.datetime.strptime(date_input, '%d-%m-%Y')
            print(f"The date you entered is {date_input} ")
            date.append(str(date_input))
            break
        except:
            print(ValueError("Your date has the wrong format"))
            print(ValueError("The format should be DD-MM-YY"))
            print("Please try again")   
    return date

#print(add_date())

def add_amount():
    amount_list = []
    allowed_char = ["1","2","3","4","5","6","7","8","9","0",".","-"]
    print("What amount of BTC did you purchase and sell?")
    print("Enter a (-)negative amount if you sold BTC")
    print("Alloweed input characters are ('0 - 9', '-', '.')")
    
    
    while True:
        amount_input = input("Enter amount here : ")
        
        check_char = validate_char(amount_input, allowed_char)
        
        if check_char == [] and len(amount_input) > 0:
            
            
            if (float(amount_input) < 0 and (btc_amount + float(amount_input)) > 0) or (float(amount_input) > 0 and (btc_amount + float(amount_input)) > 0):
                
                amount_list.append(str("Bought")) if float(amount_input) > 0 else amount_list.append(str("Sold"))
                print("Input approved...")
                print(f"New BTC balance is : {(float(amount_input) + btc_amount)}.BTC")
                amount_list.append(float(amount_input))
                break
            else:
                #print(btc_amount + float(amount_input))
                print(ValueError(f"Btc sold sold ({amount_input}.BTC) can not be greater than portfolio balance ({btc_amount}.BTC) please try again"))
                

        else:
            print(ValueError(f" Input empty or Forbidden characters {check_char} were used please try again"))
            
    return amount_list 
        
#print(add_amount())

def add_price():
    price_list = []
    allowed_char = ["1","2","3","4","5","6","7","8","9","0","."]
    print("At what price did you sell or buy your BTC")
    print("Alloweed input characters are ('0 - 9', '.')")
    
    while True:
        price_input = input("Enter price here : ")
        
        check_char = validate_char(price_input, allowed_char)
        
        if check_char == [] and len(price_input) > 0:
            #print(float(price_input))
            print("Input approved...")    
            price_list.append(float(price_input))
            #print(price_list)
            break     

        else:
            print(ValueError(f"Input empty or Forbidden characters {check_char} were used please try again"))
            
    return price_list

#print(add_price())

# ========================== MAIN FUNCTIONS=============================

def start():
    """
    Function checks if the portfolio has a name. If not you can add one that is then added to the google sheet
    """
    print("""
    \n================================================
    \nWelcome to your Bitcoin portfolio tracker
    \n================================================""")
    if SHEET.worksheet("name").get_values() == []:
        print("\n================================================")
        print("Please pick a name for your portfolio")
        print("\n================================================")
        portfolio_name_input = [input("Please enter your portfolio name:")]
        print("\n================================================")
        SHEET.worksheet("name").append_row(portfolio_name_input)
    else:
        portfolio_name = SHEET.worksheet("name").get_values()
        print("\n================================================")
        print("\n...")
        print(f"your portfolio {str(portfolio_name[0][0])} Is now loaded!")
        print("\n================================================")
        

start()

def dashboard():
    """
    Function that shows dashboard with current value of portfolio, profit/loss etc
    """
    
    btc_value = round(btc_amount * btc_price, 2)
    # Average buy price
    avg_buy_price = round(sum_sheet("trades", "E2:E") / len(SHEET.worksheet("trades").get_values("E2:E")), 2)
    # The average buy price value of all btc
    avg_buy_price_value = round((sum_sheet("trades", "E2:E") / len(SHEET.worksheet("trades").get_values("E2:E"))) * btc_amount, 2)
    # Percentage difference between average buy price value and current total BTC value 
    percent_profit_or_loss = (avg_buy_price_value - btc_value) / avg_buy_price_value * 100
    # Gives a negative value if the average buy pricee is more than current btc_value
    ternary_plus_minus_percent = round(percent_profit_or_loss, 2) if avg_buy_price_value < btc_value else round(percent_profit_or_loss * -1, 2)
    print("""
    \n================================================
    \nBITCOIN PORTFOLIO TRACKER - DASHBOARD
    \n================================================""")
    print(f"\nYour BTC balance is: {btc_amount} BTC")
    print("\n================================================")
    print(f"\nCurrrent BTC value in USD$ is: {btc_value} $")
    print("\n================================================")
    print(f"\nYour average BTC buy price in USD is {avg_buy_price} $")
    print("\n================================================")
    print(f"\nYour BTC value based on average buy price is {avg_buy_price_value} $")
    print("\n================================================")
    print(f"\nAverage pofit and loss is: {ternary_plus_minus_percent} %")
    print("\n================================================")
    nav()
    
def update_sheet():
    list = []
    length = len(SHEET.worksheet("trades").get_values("A2:A"))
    list.append(length + 1)
    list.append(add_date()[0])
    two_values_list = add_amount()
    type, amount = two_values_list
    list.append(type)
    list.append(amount) 
    list.append(add_price()[0])
    #print(length)
    #print(list)
    SHEET.worksheet("trades").append_row(list)
    nav()

#update_sheet()


def trades_list():
    """
    Function that creates class instances of trades that has been made.
    """
    class Trade:
        def __init__(self, number, date, type, amount, price):
            self.number = number
            self.date = date
            self.type = type
            self.amount = amount
            self.price = price
        
        def __str__(self):
            return "\nTrade number; " + self.number + "\nTrade date: " + self.date + "\nTrade type: " + self.type + "\nBTC amount: " + self.amount + "\nBTC price: " + self.price

    keys_headings = SHEET.worksheet("trades").get_values("A1:E1")
    values_data = SHEET.worksheet("trades").get_values("A2:E")
    print("""
    \n================================================
    \n*** BITCOIN PORTFOLIO TRACKER - TRADES LIST ***
    \n================================================""")
    print("\nBelow is a list of all your trades")
    print("\n================================================")
    for i in range(len(values_data)):
        if len(values_data) > 0:
            tradei = Trade(values_data[i][0], values_data[i][1], values_data[i][2], values_data[i][3], values_data[i][4] )
            print("\n================================================")
            print(tradei)
        else:
            print("\n========================================================")
            Print("There are no trades in the list please add trades first")
            print("\n========================================================")
    nav()

nav()