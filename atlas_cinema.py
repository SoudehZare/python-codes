print('welcome to Atlas cinema.' , ' The regular price of a movie ticket is $10, but you may be eligible for a discount if you meet any of the following conditions')
age=input('How old are you?  ')
Education = ""

age_as_int= int(age)
if age_as_int <= 3:
    Pay_1= 10-10
    print(f" you have to pay ${Pay_1} for your discount")
elif age_as_int < 5:
    Pay_2= 10-5
    print(f" you have to pay ${Pay_2} for your discount")
elif age_as_int < 18 and Education == "high school student":
        Education=input("What is your current level of education?\n 'high school student' or 'university student'?")
        dis = 10*20/100
        pay_3= 10-dis
        print(f" you have to pay ${pay_3} for your discount")
elif  age_as_int < 24 and Education == "university student":
        Education=input("What is your current level of education?\n 'high school student' or 'university student'?")
        dis = 10*30/100
        pay_4= 10-dis
        print(f" you have to pay ${pay_4} for your discount")
else:
     if age_as_int > 24:
            print(f" you have to pay $10 for your discount")
