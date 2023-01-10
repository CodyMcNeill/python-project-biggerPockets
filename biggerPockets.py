class biggerPockets():
    def __init__(self):
        self.isRunning = True
        self.totalMonthlyIncome = None
        self.totalMonthlyExpenses = None
        self.totalMonthlyCashFlow = None

    def income(self):
        print('Welcome to the Income calculator!')
        self.rent = input('Please input the amount of rental income earned each month ')
        self.laundry = input('Please input the amount of laundry income earned each month ')
        self.storage = input('Please input the amount of storage income earned each month ')
        self.misc = input('Please input the amount of misc income earned each month ')
        self.totalMonthlyIncome = float(self.rent) + float(self.laundry) + float(self.storage) + float(self.misc)
        print(f'Your total Monthly Income is ${self.totalMonthlyIncome}')
        return self.totalMonthlyIncome
    
    def expenses(self):
        print('Welcome to the expenses calculator!')
        self.tax = input('Please input the amount of taxes for the property each month ')
        self.insurance = input('Please input the amount of insurance cost for the property each month ')
        self.utilities = input('Please input the amount of utilities cost for the property each month ')
        self.hoa = input('Please input the amount of hoa cost for the property each month ')
        self.lawnSnow = input('Please input the amount of lawn/snow services cost for the property each month ')
        self.vacancy = input('Please input the amount of vacancy cost for the property each month ')
        self.repairs = input('Please input the amount of repair cost for the property each month ')
        self.capex = input('Please input the amount of capital expenditure cost for the property each month ')
        self.propertyManager = input('Please input the amount of property management cost for the property each month ')
        self.mortgage = input('Please input the amount of mortgage cost for the property each month ')
        self.totalMonthlyExpenses = float(self.tax) + float(self.insurance) + float(self.utilities) + float(self.hoa) + float(self.lawnSnow) + float(self.vacancy) + float(self.repairs) + float(self.capex) + float(self.propertyManager) + float(self.mortgage)
        print(f'Your total Monthly Expenses is ${self.totalMonthlyExpenses}')
        return self.totalMonthlyExpenses
    
    def cashFlow(self):
        print('Welcome to the Cash Flow calculator!')
        if (self.totalMonthlyIncome and self.totalMonthlyExpenses) == None:
            print('-- ERROR -- \nPlease go through both the Income and Expenses calculators!')
        else:
            self.totalMonthlyCashFlow = self.totalMonthlyIncome - self.totalMonthlyExpenses
            print(f'Your total monthly Cash Flow is ${self.totalMonthlyCashFlow}')
            return self.totalMonthlyCashFlow

    def ROI(self):
        print('Welcome to the ROI calculator!')
        if self.totalMonthlyCashFlow == None:
            print('-- ERROR -- \nPlease go through the Cash Flow calculator!')
        else:
            self.downPayment = input('Please input the amount of your Down Payment ')
            self.closingCosts = input('Please input the amount of Closing Costs ')
            self.rehabBudget = input('Please input the amount of Rehab Budget ')
            self.miscCost = input('Please input the amount of Miscellaneous cost ')
            self.totalInvestment = float(self.downPayment) + float(self.closingCosts) + float(self.rehabBudget) + float(self.miscCost)
            print(f'Your Total Investment is ${self.totalInvestment}')
            self.annualCashFlow = self.totalMonthlyCashFlow * 12
            print(f'Your Annual Cash Flow is ${self.annualCashFlow}')
            self.cashOnCashROI = (self.annualCashFlow / self.totalInvestment) * 100
            print(f'Your Cash on Cash ROI is {self.cashOnCashROI} %')
        
    def runner(self):
        while self.isRunning == True:
            userInput = input('---\nWelcome to the Bigger Pockets Calculator!\nPlease enter one of the following commands:\nincome - Prompts the Bigger Pockets Income Calculator\nexpenses - Prompts the Bigger Pockets Expenses Calculator\ncashflow - Prompts the Bigger Pockets Cash Flow Calculator\nroi - Prompts the Bigger Pockets ROI Calculator\nq - Quits the application\n---')
            if userInput.lower() == 'q':
                print('Thanks for using the Bigger Pockets python app!')
                self.isRunning = False
                break
            elif userInput.lower() == 'income':
                self.income()
            elif userInput.lower() == 'expenses':
                self.expenses()
            elif userInput.lower() == 'cashflow':
                self.cashFlow()
            elif userInput.lower() == 'roi':
                self.ROI()
            else:
                print('Invalid input! Please try again.')

biggerPockets().runner()


# wanted to add the option to see your currently stored total calculated values, but ran out of time