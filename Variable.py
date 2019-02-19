
year_of_birth =input("enter year of birth: ") #creating a variable that holds the year that is entered by a user

year = int(year_of_birth)
age = 2019 - year

if age < 18:
    print("this person is a minor") #displays you as minor if the condition is true
elif age >= 18 and age <= 36:
    print("the person is a youth")#displays you as youth if the condition is true
else:
    print("the person is an elder")#displays you as an eleder if  non of the above conditions are true
