"""
imperial system
bmi = 703*weight(in pounds)/height**2(in inches)

metric system
bmi=weight(in kiograms)/height**2(in metres)

BMI chart 
if bmi = 16.0-18.5 underwight
      18.5-25.0 normal
      25.0-40.0 overweight
"""


print("*************************************************************************************************************************************************")
print("Press any key to calculate your BMI")
b=input("Enter I for Imperial system or M for Metric system : ")

if b=='i' or b=='I':
    w1=float(input("Enter your weight in pounds(lbs) : "))
    h1=float(input("Enter your height in inches(in) : "))
    bmi=(703*w1)/h1**2
    print("Your BMI is",bmi)
    if(bmi>=16.0 and bmi<=18.5):
        print("You are Underweight")
    elif(bmi>=18.5 and bmi<=25.0):
        print("You are Normal")
    elif(bmi>25.0):
        print("You are Overweight")
    else:
        print("Thank You")

elif  b=='m' or b=='M':
    w2=float(input("Enter your weight in kilograms(kgs) : "))
    h2=float(input("Enter your height in metres(m) : "))
    bmi=w2/(h2**2)
    print("Your BMI is",bmi)
    if(bmi>=16.0 and bmi<=18.5):
        print("You are Underweight")
    elif(bmi>=18.5 and bmi<=25.0):
        print("You are Normal")
    elif(bmi>25.0):
        print("You are Overweight")
    else:
        print("Thank You")
else:
    print("Enter only above characters to perform the right operation")
