while True:
    
    from turtle import *

    yob=int(input("Height: "))
    m=yob/100
    t=int(input("Weight: "))

    bmi=t/(m*m)

    if bmi<16:
        print("Severely underweight")
    elif bmi>=16 and bmi<18.5  :
        print("Underweight")
    elif bmi>=18.5 and bmi<25:
        print("Normal")
    elif bmi>=25 and bmi<25:
        print("Overweight")
    else:
        print("Obese")
        
    

