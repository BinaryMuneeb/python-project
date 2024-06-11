name=input("enter your name ")
weigth=int(input("enter the weigth in pound : "))
heigth=int(input("enter the heigth in inches : "))
bmi=(weigth*703)/(heigth*heigth)
print("your body mass calculation is: ",bmi)
if bmi>0:
        if(bmi<18.5):
            print(name +", you are underwight")
        elif (bmi<=24.9):
            print(name +", you are normal weight.")
        elif (bmi<29.9):
            print(name +", you are overweight.")
        elif (bmi<34.9):
            print(name +", you are obese.")
        elif (bmi<39.9):
            print(name +", you are severely obese.")
        else:
            print(name +", you are morbidly obese.")
else:
         print("Enter valid input")
