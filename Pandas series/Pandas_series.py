import pandas as pd

cars = pd.Series(['Suzuki','Toyota','Skoda','Range rover','Hyundai'])

print(cars)
print('\nType:', type(cars))

print('\nEXTRINSIC INDEX\n')




brand = pd.Series(
    ['Suzuki','Toyota','Skoda','Range rover','Hyundai'],
    index=['Swift', 'Camry', 'Fabia', 'Vogue', 'Venue'])

print(brand)

print('\nSORTED_BY_INDEX')



print('\nPLACE_DETAILS')

favorite_place = pd.Series({ 'danish': 'chennai', 'vijay': 'kashmir',
                            'zayan': 'ooty','Akshara': 'keralam'})

print(favorite_place)




 
print('\nPRINT SPECIFIC SET OF ROW FROM START')

favorite_place = pd.Series({ 'danish': 'chennai', 'vijay': 'kashmir',
                            'zayan': 'ooty','Akshara': 'keralam'})

print(favorite_place.head(1))




print('\nPRINT SPECIFIC SET OF ROW FROM END')

favorite_place = pd.Series({ 'danish': 'chennai', 'vijay': 'kashmir',
                            'zayan': 'ooty','Akshara': 'keralam'})

print(favorite_place.tail(1))




print("\nDETAILS")

players_details = pd.Series(["India", "Australia", "Afghanistan", "England", "India", "SouthAfrica", "Srilanka"],
index=["Virat Kohli", "Michael Clarke", "Rashid khan","Joe Root", "MS Dhoni", "Dewald Brevis", "Pathirana"])

print(players_details.describe())




print("\nSLICING")

countries_slicing = pd.Series(["India", "Australia", "Afghanistan", "England", "India", "SouthAfrica", "Srilanka"])

print(countries_slicing[1:3])


 

countries_slicing = pd.Series(  ["India", "Australia", "Afghanistan", "England", "India", "SouthAfrica", "Srilanka"])

print("\nREVERSED")
print(countries_slicing[::-1])
