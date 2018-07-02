#calculating the number of months since marriage and joining the company
def months(occasion,today):
    try:
        occasion = int (occasion)
        today = int(today)

    except:
        print("Invalid date.")
        flag = False
        todayMonth = 0

    else:
        flag = True

    if flag == True:
        occasionYear = occasion % 10000
        occasionMonth = occasion // 10000

        todayYear = today % 10000
        todayMonth = today // 10000

        years = todayYear - occasionYear
        months = todayMonth - occasionMonth

        totalMonths = (years*12) + months
    return  todayMonth


def main():
    basic = input("Enter basic pay:")
    age = input("Enter your age: ")

    try:
        basic = float (basic)
        age = int (age)
    except:
        print("Invalid number.")
        basic = input("Enter basic pay again:")
        age = input("enter age again:")

        #giving the user another chance to right the correct input.
        try:
            basic = float (basic)
            age = int (age)
        except:
            print("Invalid input.")
            basic = 0
            age = 0

    dateOfJoining = input("Enter the date of joining (MMYYYY): ")
    dateOfMarriage = input("Enter the date of marriage (MMYYYY): ")
    todaysDate = input("Enter today's date (MMYYYY): ")

    monthsInService = months(dateOfJoining,todaysDate)
    monthsOfMarriage = months(dateOfMarriage,todaysDate)

#calculating tax
    incomeTax = .05 * basic
    provitionalTax = .07 * basic
    payAfterTax = basic - incomeTax - provitionalTax
    print("Income tax is ",incomeTax)
    print("Provisional tax is ",provitionalTax)
    print("Basic pay after tax is:",payAfterTax)

#calculating old age allowance
    if age < 45:
        oldAgeAllowance = 0

    elif age>= 45 and age <= 55:
        oldAgeAllowance = payAfterTax * .10

    else:
        oldAgeAllowance = payAfterTax * .15

    print("""The old age allowance is given after age of 45.
    During the age 45-55 it is 10% of the basic pay excluding tax,
    while it becomes 15% after the age of 55.""")

    print("Your olg age allowance is",oldAgeAllowance)

#calculating the months of marriage in service
    if monthsInService < monthsOfMarriage:
        monthsInServiceSinceMarriage = monthsInService

    else:
        monthsInServiceSinceMarriage = monthsOfMarriage


    if monthsInServiceSinceMarriage > 0:
        houseRent = payAfterTax * (.15)

    else:
        houseRent = 0

    print("House rent is given 15% of basic(excluding tax) to only married employes")
    print("Your house rent is",houseRent)

    salary = basic + oldAgeAllowance + houseRent


#finding the net pay and gross pension
    variableOne = (basic * 2) * monthsInService
    variableTwo = (houseRent) * monthsInServiceSinceMarriage
    variableThree =  (oldAgeAllowance) * 3
    variableFour = salary * 2

    totalGross = variableOne + variableTwo + variableThree + variableFour
    netPay = totalGross - incomeTax - provitionalTax
    print("(basic pay * 2) number of months in service = ",variableOne)
    print("house rent multiplied by th months in service since marriage = ",variableTwo)
    print("Old age allowance multiplied by three = ", variableThree)
    print("The total pay is the sum of above three minus the taxes.")
    print("The total gross pay is: ",totalGross)
    print("The total net pay is:",netPay)

main()


