annual_salary = int(input("What is your annual salary? "))
portion_saved = float(input("What percent of your annual salary will be saved? "))
total_cost = int(input("How much does your dream home cost? "))
portion_down_payment = total_cost * float(input("What percentage of the total cost of the house do you need for the down payment? "))
current_savings = 0
r = float(input("What is your expected annual rate of return? "))
num_months = 0


while current_savings < portion_down_payment:
    current_savings = (current_savings + (current_savings * (r/12))) + ((annual_salary / 12) * portion_saved)
    num_months = num_months + 1
    if current_savings >= portion_down_payment:
            print("It will take you " + str(num_months) + " months to save up for the down payment for your house.")