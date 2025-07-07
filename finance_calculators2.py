#Ngwane Fanelukubongwa
#FN25050018269

import math

#Prompting user to choose which calculation they want do. 
# and making sure the string is all lower case to handle errors
print("Investment - to calculate the amount of interest you'll earn on your" \
      " investment")
print("Bond - to calculate the amount you'll have to pay on a home loan.\n")
calculator = input("Enter either “investment” or “bond” to proceed: ")
calculator = calculator.lower()

#Caculations depending on the user choice

#INVESTMENT... getting required data from user to calculate final investment
#  using relevent method
if calculator == "investment":
    principal_amount = float(input("Enter the amount to deposit: R"))
    interest_rate1 = float(input("enter the interest rate (%): "))
    interest_rate = interest_rate1/100
    num_years = int(input("Enter duration of investment in years: "))
    interest = input("Choose “simple” or “compound” interest:  ")
    interest = interest.lower() #error handling
   

    #SIMPLE INTEREST... calculaating final investemnt value
    if interest == "simple":
        final_amount = principal_amount * (
            1 + interest_rate * float(num_years))
        print(f"The total investment value is: R{final_amount:.2f}")

    #COMPOUND INTEREST... calculating final investement value
    elif interest == "compound":
        final_amount = principal_amount * (
            1 + interest_rate)**float(num_years)
        print(f"The total investment value is: R{final_amount:.2f}")

#BOND... getting required data from user to calculate and 
# display monthly instalments
elif calculator == "bond":
    present_value = float(input("Enter the present value of the house: R"))

    interest_rate1 = float(input("Enter the interest rate (%): "))
    interest_rate = (interest_rate1 / 100) / 12

    num_months = float(input("Enter number of repayment months: "))

    #BOND... Calculating monthly instalments using collected data
    monthly_instalment = (present_value * interest_rate) / (
        1 - (1 + interest_rate)**(num_months * (-1)))
    print(f"Your monthly installment will be: R{monthly_instalment:.2f}")

#Error massage if neither Investment nor bond is chosen from the menu
else:
    print("ERROR: Please ensure that the selection from the menu is" \
          " correctly spelt!")
