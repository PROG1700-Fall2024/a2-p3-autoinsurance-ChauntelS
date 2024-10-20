#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:  W0239497   
#Student Name:  Chauntel Smith

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Welcome message 
    print("Welcome to the Monthly Auto Insurance Calculator\nPlease fill out all required information below:")
    #input Varaibles 
    gender = input("Are you Male or Female?: ")
    age = int(input("Enter your age: "))
    carPrice = float(input("Enter price of vehicle: $"))
    rate = 0
    #if gender and age =
    if gender.lower() == "male" and (age>15 and age<=25):
        rate = 0.25
    elif gender.lower() == "male" and (age>25 and age<=40):
        rate = 0.17
    elif gender.lower() == "male" and (age>40 and age<=100):
        rate = 0.10
    elif gender.lower() == "female" and (age>15 and age<=25):
        rate = 0.20
    elif gender.lower() == "female" and (age>25 and age<=40):
        rate = 0.15
    elif gender.lower() == "female" and (age>40 and age<=100):
        rate = 0.10
    else:
        print("Error! Information is not valid, plesae try again.")
    
    #Outcome calculations
    monthlyPayment = ((carPrice * rate)/12)
    #Outcome message
    print("Your monthly payment will be: ${0:.2f}".format(monthlyPayment))
    # YOUR CODE ENDS HERE

main()