with open("CurrencyData.txt") as c:
    a = c.readlines()

currencyDict = {}

for line in a:
    parse = line.split("\t")
    currencyDict[parse[0]] = parse[1]

amount = float(input("Enter the amount:\n"))
print("Which currency you want to convert this amount to? Available options are:\n")
[print(item)for item in currencyDict.keys()]

currency = input("Please enter name of one of these currency:\n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")