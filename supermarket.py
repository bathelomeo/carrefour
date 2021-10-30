print('Welcome to Carrefour')
Give = input('You can only buy the things in this categories, Agree?:')
if Give == 'Ok':
    print('Lets Continue')
Question = input('Do you want to buy something in Vegetables , Fruits , Snacks , Bisquits and only that.')
if Question == 'Yes':
    print('Great')
elif Question == 'No':
    print('Sorry i cant help you')
price = 0
Vegetables =input('Do you want to know what is in Vegetables')

if Vegetables == 'Yes':
    print('In Vegetables There is: Tomatoes , Onion , Brocoli , Cauliflower')
else:
    print('Fine')
vegies = input ('So what do you want to buy in Vegetables')

if vegies == 'Tomatoes':
    price = 0.7
elif vegies == 'Onion':
    price = 0.5
elif vegies == 'Brocoli':
    price = 0.25
elif vegies == 'Cauliflower':
    price = 0.30
print(price)

Fruits =input('Do you want to know what is in fruits')

if Fruits == 'Yes':
    print('In Fruits There is: Grapes , Orange , Banana , Kiwi')
else:
    print('Fine')
Frouts = input ('So what do you want to buy in Fruits')

if Frouts == 'Grapes':
    price = 0.300
elif Frouts == 'Orange':
    price = 0.30
elif Frouts == 'Banana':
    price = 0.10
elif Frouts == 'Kiwi':
    price = 0.100
print(price)

Snacks =input('Do you want to know what is in Snack')

if Snacks == 'Yes':
    print('In Fruits There is: Stix , Kra curls , Tamu Tamu , Crakles ')
elif Snacks == 'No':
    print('Fine')
Snocks = input ('So what do you want to buy in Snacks')

if Snocks == 'Stix':
    price = 0.30
elif Snocks == 'Kra curls':
    price = 0.45
elif Snocks == 'Tamu Tamu':
    price = 0.20
elif Snocks == 'Kracles':
    price = 0.50
print(price)

Bisquits =input('Do you want to know what is in Bisquits')

if Bisquits == 'Yes':
    print('In Fruits There is: Oreo , Mary land , Nice , Wafers')
elif Bisquits == 'No':
    print('Fine')

Bosquits = input ('So what do you want to buy in Bisquits')

if Bosquits == 'Oreo':
    price = 0.60
elif Bosquits == 'Mary land':
    price = 0.150
elif Bosquits== 'Nice':
    price = 0.56
elif Bosquits == 'Wafers':
    price = 0.70
print(price)
print('Everything that is one number or is mary land cookies price is actually a 0 in there')