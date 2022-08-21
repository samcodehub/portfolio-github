# get your inputs
initial_balance = int(input("Enter your initial balance: "))
rate = int(input("Enter the rate of interest: "))
num_years = int(input("Enter number of years:"))

# initial investment
balance = initial_balance

# going through loop  
for i in range(1,num_years+1):
    # calculate interest
    interest = balance * rate/100
    balance = balance + interest
    # final result
    print(f"your return per year {i}, is {round(balance,2)}")