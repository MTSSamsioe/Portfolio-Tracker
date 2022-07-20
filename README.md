# BITCOIN PORTFOLIO TRACKER
Bitcoin portfolio tracker is a terminal portfolio program that tracks and documnets all the users Bitcoin purchases and sales.
Aswell as calculates average profits and losses, Bitcoin balance, portfolio value etc. Going forward in this text Bitcoin will be referred to as BTC

---

## How to use portfolio
---
The first time the program opens the user will be prompted to name their BTC protfolio.
Afterwards the user will get navigation options to visit other features of the program.
Live BTC price is updated every 20 minutes from a google sheet to calculate the current value of the portfolio.
More useful values can be found in the dashboard section. More trades can be added from the add trade section.
All added trades are uploaded to the same google sheet. A list of trades can be generated from the trades list section.

**The first time the program is started it is recomended that a new user starts to add a couple of trades in the add section to populate the trade list and dashboard with data**

### Link to google sheet
- (Click here to open google sheet that contains data)[https://docs.google.com/spreadsheets/d/15so2cZT1kHRJTjCibZ_gVl5OYUaxSQfogw_qDPIbsZQ/edit?usp=sharing]
- It is only recomended to delete the data under the headings in the sheet "trade" and the first cell in the sheet "name" if the user wants to run the program from the start ad rename the portfolio or delete trades. Deleting other data may cause problemns to the program 

## Features

### Existing Featurees

- Give portfolio a name
    - Name your portfoli the first time the program starts.
    - After opening the program the nex time a text will say that the users portfolio is loaded
![start image choose name](/assets/images/start.png)


- Dashboard
    - In the dashboard the user can see multible values and calculations:
        - Btc balance
        - Current BTC value in USD$
        - Average buy/sell price in USD$
        - Portfolio value based on average buy price
        - Average percentage profit/loss
![Image of dashboard](/assets/images/dashboard.png)


- Add trade
    - In the add trade section the user can add trades
        1. The user will be promted to enter purchase/sale date
            - Date must have format DD-MM-YY and will give a message to retry if the format is not valid
            ![Image of add trade](/assets/images/add_date.png)

        2. The user will be promted to enter purchase/sold BTC amount.
            - If the user sells BTC a (-) should be added before
            -  The input will be compared in a function to a list of allowed characters and also it checks that the input is not empty.
            - Alloed characters are (-, 0-9 and .) An error message will be shown to try again if input is empty or if a forbidden  character is used
            - The validation function will also check sell amount that it is not greater than the curreent BTC balance
            - An error message will promt to try again if that happens
            ![image of add amount ](/assets/images/add_amount.png)

        3. The user will be promted to enter the buy/sell price in USD$
            - The validation function will check that the input is not empty or if a forbidden character is used
            - Allowed charcters are (0-9 and .) An error message will be shown to try again if input is empty or if a forbidden  character is used

        ![Image of add price](/assets/images/add_price.png)
        


- Trades list
    - A List of trades will be generated via the trade class in trade.py
    - The data is collected from the google sheet
        - The list will show:
            - Number of the trade
            - Date bought/sold
            - Type of trade bought/sold
            - BTC amount
            - BTC price
    - If there is no trades a message is show that there is no trades and first go to add section
![Image of trade list](/assets/images/trade_list.png)


- Navigation
    - All sections will run the nav function so the user easily can go between sections
    - The the curretn section is shown above the nav function so the user must scroll up when visiting a new section 
    - The menu options are:
        - Dashboard
        - Add trade
        - Trade list
        - Exit program
![Image of trade list](/assets/images/navigation.png)


### Future features
- Calculate realized profit loss on sold BTC
- Rename portfolio
- Have multiple portfolios
- Support multible currencies
- Password to enter portfolio


## Data Model
---
- I used a class "Trade" in trade.py to generate the list of trades.
- I made two helper funtions that are used multiple times in the code: 
    1. Calculate the sum of a cerrtain cell range in the google sheet. 
    2. Valdidate input characters
- Every section runs its own function and all functions end in running the navigation function


## Testing
---
- I have tested this program with the steps below:
    - Passed the code through the [PEP8](http://pep8online.com/) without any erros
    - Corrected any errors found in the errors list in gitpod
    - Manually tested the program and giving invalid commands to see that the correct error messages are displayed

### Bugs

#### Solved bugs
- I could not figure out how to compare two lists or strings:
    - FIX: I found a solution here [Adam smith](https://www.adamsmith.haus/python/answers/how-to-get-the-difference-between-two-list-in-python)
- The program needed to have two trades entered in the list to be abel to make calculations in dashboard
    - FIX: I added some if statements that prevents values to be 0 since you can´t devide something with 0
- I could not get message to show text that the trades list is empty if no trades has beeen added
    - FIX: The if statemen was previously in a for loop that would iterate the same amount of times as entered trades.
    But since it was empty the loop never started and could not show the else statement. I instead but the for loop in the if statement.

#### Remaining bugs
- It is not really a bug but I uploaded a credentials file to git hub because I forgot to add it to my gitignore file.
I tried librarys bfg and tried "git obliterate" without it working. Code Institute support advised me to leave it in the histroy and previous gits because it cold easily cause problems when deleting git history.
I have deleted and swiched the credentials file since then so no active key saved on github.

### Validator testing
- PEP8
    - No errors found on [PEP8](http://pep8online.com/)


## Deployment
---
- Steps for deployment:
    - Add \n in the end of to all inputs to avoid a bug
    - Write "command pip3 freeze > requirements.txt" to create list in requirements.txt of installed libraries the program needs to run
    - Create account on [Heroku](https://www.heroku.com/home)
    - Create new app on Heroku and name it
    - Go to settings and add two config vars files:
        - CREDS.json contains all content from my credentials file to be able to access the google sheet
        - PORT 8000 as instructed by CI
    - Add buildpacks in this order:
        - Python
        - Nodejs
    - Go to deploy section in Heroku:
        - Connect to Github
        - Search for your program on Github
        - Press deploy
        - Link to deployed project [Here](https://bitcoin-portfolio-tracker.herokuapp.com/)

## Credits
---
- How to get live BTC price to update automatically in google sheets [spreadsheet Class](https://www.spreadsheetclass.com/pulling-cryptocurrency-prices-into-google-sheets-2-methods/)
- How to unpack a list i found [here](https://note.nkmk.me/en/python-tuple-list-unpack/)
- Code how to validate date and time format i found [here](https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python) and was made possible with imported library DateTime
- How to compare two arrays I found [here](https://www.adamsmith.haus/python/answers/how-to-get-the-difference-between-two-list-in-python) the code borrowed from here is marked with comment in run.py
- How to create loop that creates class instances i found on this youtube video made by [Eybar Vasqueez Nevarez](https://www.youtube.com/watch?v=9ciQeqyuiek&t=187s) the method he used is the same as mine and it is marked with comment in trade.py

- Librarys that I instlled are:
    - DateTime [DateTime](https://pypi.org/project/DateTime/)
    - gspread [gspread](https://pypi.org/project/gspread/)
    - googlee auth [Google auth](https://pypi.org/project/google-auth/)
    - Bfg repo cleaner [BFG](https://rtyley.github.io/bfg-repo-cleaner/)