import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('portfolio_tracker')

btc_price = SHEET.worksheet("price").get_all_values()
#print(test)

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
    print("Your BTC balance is: ")
    print("Currrent USD value is: ")
    print("Average pofit and loss: ")
    print("""================================
    Available menue commands: 
    'Trades' = Takes you to a list of your trades 
    'Add trade' = Add a purchase or sale of Btc
    """)
    menu_choice = input(str("type menue command here: "))
    

dashboard()