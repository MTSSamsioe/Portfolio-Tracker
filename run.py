import gspread
from google.oauth2.service_account import Credentials
import datetime

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
        if char not in allowed_char :
            forbidden_char.append(char)
    return forbidden_char  







# global variables
btc_price = float(SHEET.worksheet("price").get_values("A1")[0][0])
btc_amount = sum_sheet('trades', 'c2:c')


def start():
    """
    Function checks if the portfolio has a name. If not you can add one that is then added to the google sheet
    """
    print("Welcome to your bitcoin portfoliotracker")
    if SHEET.worksheet("name").get_values() == []:
        print("Please pick a name for your portfolio")
        portfolio_name_input = [input("Please enter your portfolio name:")]
        SHEET.worksheet("name").append_row(portfolio_name_input)
    else:
        portfolio_name = SHEET.worksheet("name").get_values()
        print(...)
        print(f"your portfolio {str(portfolio_name[0][0])} Is now loaded!")



def dashboard():
    """
    Function that shows dashboard with current value of portfolio, profit/loss and a menu
    """
    
    btc_value = round(btc_amount * btc_price, 2)
    # Average buy price
    avg_buy_price = sum_sheet("trades", "D2:D") / len(SHEET.worksheet("trades").get_values("D2:D"))
    # The average buy price value of all btc
    avg_buy_price_value = (sum_sheet("trades", "D2:D") / len(SHEET.worksheet("trades").get_values("D2:D"))) * btc_amount
    
    percent_profit_or_loss = (avg_buy_price_value - btc_value) / avg_buy_price_value * 100
    # Gives a negative value if the average buy pricee is more than current btc_value
    ternary_plus_minus_percent = round(percent_profit_or_loss, 2) if avg_buy_price_value < btc_value else round(percent_profit_or_loss * -1, 2)
    
    


    print(f"Your BTC balance is: {btc_amount} BTC")
    print(f"Currrent BTC value in USD$ is: {btc_value} $")
    print(f"Your BTC value based on average buy price is {avg_buy_price_value} $")
    print(f"Average pofit and loss is: {ternary_plus_minus_percent} %")
    print("""================================
    Available menue commands: 
    'Trades' = Takes you to a list of your trades 
    'Add trade' = Add a purchase or sale of Btc
    """)
    menu_choice = input(str("type menue command here: "))
    

#print(dashboard())

def add_date():
    trade = []
    print("Hi what date did you buy your bitcoin? (The format has to be DD-MM-2022) ")
    
    while True:
        try:
            date_input = input("Enter your date here: ")
            datetime.datetime.strptime(date_input, '%d-%m-%Y')
            print(f"The date you entered is {date_input} ")
            trade.append(date_input)
            return False
        except:
            print(ValueError("Your date has the wrong format"))
            print(ValueError("The format should be DD-MM-YY"))
            print("Please try again")
    
    # BTC AMOUNT INPUT
       
    print(trade)


def add_amount():
    amount_test = []
    allowed_char = ["1","2","3","4","5","6","7","8","9","0",".","-"]
    print("What amount of BTC did you purchase and sell?")
    print("Enter a (-)negative amount if you sold BTC")
    print("Alloweed input characters are ('0 - 9', '-', '.')")
    
    
    while True:
        amount_input = input("Enter amount here : ")
        
        check_char = validate_char(amount_input, allowed_char)
        print(check_char)
        if check_char == [] and len(amount_input) > 0:
            print("Chars ok and input not empty")
            
            if (float(amount_input) < 0 and (btc_amount + float(amount_input)) > 0) or (float(amount_input) > 0 and (btc_amount + float(amount_input)) > 0):
                print(btc_amount + float(amount_input))
                print("Amount ok")
                
            else:
                print(btc_amount + float(amount_input))
                print(ValueError("Btc amount sold can not be greater than portfolio balance"))
                return False

        else:
            print(ValueError(" Input empty or Forbidden characters used please try again"))
            return False

        return False 
        
            
            
         
    

add_amount()

