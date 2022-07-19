# BITCOIN PORTFOLIO TRACKER
Bitcoin portfolio tracker is a terminal portfolio that track and documnets all the users Bitcoin purchases and sales.
Aswell as calculates average profits loss, portfolio value etc. Further in this text Bitcoin will be referred to as BTC.
(Link to project)[Link]
---

## How to use portfolio
---
The first time the user opens the program the user will be prompted to name their BTC protfolio.
Afterwards the user will get navigation options to visit other features of the program.
Live BTC price is updated every 20 minutes from a google sheet to calculate the current value of the portfolio.
More usevul values can be found in the dashboard section. More trades can be added from the add trade section.
All added trades are added uploaded to the same google sheet. A list of trades can be generated from the trades list section.

### Link to google sheet
- (Click here to open google sheet)()

## Features

### Existing Featurees

- Give portfolio a name
    - Name your portfoli the first time the program opens.
    - After opening the program the nex time a text will say that the users portfolio is loaded


- Dashboard
    - In the dashboard the user can see multible values and calculatins:
        - Btc balance
        - Current BTC value in USD$
        - Average buy/sell price in USD$
        - Portfolio value based on average buy price
        - Average percentage profit/loss

- Add trade
    - In the add trade section the user can add trades
        1. The user will be promted to enter purchase/sale date
            - Date must have format DD-MM-YY and will give a message to retry if the format is not valid
        2. The user will be promted to enter purchase or sold BTC amount.
            -  The input will be compared in a function to a list of allowed characters and alse checks that the input is not empty.
            - Alloed characters are (-, 0-9 and .) An error message will be shown to try again if input is empty or if an forbidden  character is used
            - The validation function will also check sell amount that it is not greater than the BTC balance
            - An error message will promt to try again if that happens
        3. The user will be promted to enter the buy/sell price in USD$
            - The validation function will check that the input is not empty or if a forbidden character is used
            - Allowed charcters are (0-9 and .) An error message will be shown to try again if input is empty or if an forbidden  character is used
- Trades list
    - A List of trades will be generated via the trade class in trade.py
    - The data is collected from the google sheet
        - The list will show:
            - Number of the trade
            - Date bought/sold
            - Type of trade bought/sold
            - BTC amount
            - BTC price
    
- Navigation
    - All sections will run the nav function so the user easily can go between sections
    - The the curretn section is shown above the nav function so the user must scroll upp when visiting a new section 
    - The menu options are:
        - Dashboard
        - Add trade
        - Trade list
        - Exit program
### Future features


## Data Model
---

## Testing
---
### Bugs

#### Solved bugs

#### Remaining bugs

### Validator testing

## Deployment
---

## Credits
---

