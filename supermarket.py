print('hi')
greeting = input('May i ask What time of day is it ')
if greeting =='Afternoon':
    print('Good Afternoon')

if greeting == 'Evening':
    print('Good Evening')

if greeting== 'Morning':
    print('Good morning')
else:
    print('shish mean')
Name = input('May I ask what is you name ?')
print('Hello' ' '+ Name)

print("Let's go with a security check"'' + Name)

security = input('hey other guard can you see any guns or bombs')

if security== 'Yes':
    print('Put your hands in the Air')
else:
    print('go through')

corona = input('May we please check your temprature and please sanitize Mr or Mrs' ' '+ Name)
if corona== 'Yes':
    print('You may go in Mrs or Mr' ' ' + Name)
else:
    print('Sorry we cant let you in' ' ' + Name)

Troley = input('Here is your Troley' ' '+Name)
if Troley== 'Thank you':
    print('Your Welcome' ' '+Name)
else:
    print('Ahhhhh Ok')

pay = input('What Will you be paying with' ' ' + Name)
if pay=='Mpesa':
    print('Ahhh Ok')
elif pay=='safaricom':
    print('Ahhhh Ok')
elif pay=='cash':
    print('Ahhhh Ok')
else:
    print('Mrs or Mr sorry but you will have to return all this things Mr or Mrs ' ' ' + Name)
parking = input('What Will you be paying parking with Mr or Mrs' ' '+ Name)
if parking=='Mpesa':
    print('Nice!')
elif parking=='Safaricom':
    print('Lovely')
elif parking=='Cash':
    print('Ahhhh Ok')
please =input('Please insert your card')
if please == 'ok':
    print('You have 30 minutes to exit the premise Mr or Mrs' ' '+ Name)
else:
    print('You cannot leave until you pay Mr or Mrs' ' '+ Name)