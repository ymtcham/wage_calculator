import math
print("Hi there, let's calculate how much you should charge for a work ")
input("Press Enter key to start")
income_per_annum = float(input("How much do you want to earn in a year? (Do not use separators/commas) \n"))
total_working_hour_in_a_year = ((12-1)*4*6*7)
hourly_rate = income_per_annum / total_working_hour_in_a_year
num_of_hour = float(input("How many hours do you reckon this piece of work will take you? \n"))
cost = hourly_rate * num_of_hour
print(f'Well, you should consider charging Rs {math.floor(cost)} or more.')

# print(600000/((12-1)*4*6*7))