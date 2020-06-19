month_input = input("Month:")

months_and_days ={"Janurary": 31, "Feburary": "28 or 29", "March": 31, "April": 30, "May": 31, "June": 30, "July": 30, "August": 31, "September": 30, "October": 31, "November": 30,"December": 31}

for i in months_and_days:
    if i == month_input:
        print(months_and_days[i])