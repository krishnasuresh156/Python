string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")

print('"Hello " * 5: ' + "Hello " * 5)
print('"Hello " * (5 + 4): ' + "Hello " * (5 + 4))
print('"Hello " * 5 + "4": ' + "Hello " * 5 + "4")

today = "Sunday"
print('today = "Sunday"')
print('"day" in today :' + str("day" in today))              #True
print('"Sun" in today :' + str("Sun" in today))              #True
print('"fri" in today :' + str("fri" in today))              #False
print('"parrot" in "fjord":' + str("parrot" in "fjord"))     #False
