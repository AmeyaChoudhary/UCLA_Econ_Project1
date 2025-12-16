class TimeValue:
    #Ameya -> Overview, Constructor
    def __init__(self):
        print("Welcome to Money Value Calculator")

    #Ameya -> Run method, user input
    def run(self):
        print("\nWhat do you want to calculate?")
        print("\t1 = Present value")
        print("\t2 = Future value")
        print("\t3 = Annuity")
        print("\t4 = Perpetuity")
        choice = input("Choose one of the following: 1, 2, 3, or 4: ")

        if choice == '1':
            self.presentValue()
        elif choice == '2':
            self.futureValue()
        elif choice == '3':
            self.annuity()
        elif choice == '4':
            self.perpetuity()
        else:
            print("Not a valid option")

    
    def presentValue(self):
      try:
        futureVal = float(input("Enter future value IN USD ($): "))
        rate = float(input("Enter annual interest rate IN %: ")) / 100
        years = float(input("Enter number of years: "))
        presentVal = futureVal / ((1 + rate) ** years)
        print(f"Present Value = ${presentVal:.2f}")
      except ValueError:
        print("Invalid input. Please enter numeric values only.")

    #Ameya -> Future Value Formula, code
    def futureValue(self):
        presentVal = float(input("Enter present value IN USD ($): "))
        rate = float(input("Enter annual interest rate IN %: ")) / 100
        years = float(input("Enter number of years: "))
        futureVal = presentVal * ((1 + rate) ** years)
        print(f"Future Value = ${futureVal:.2f}")

    #Ameya -> Annuity Formula, code
    def annuity(self):
        paymentVal = float(input("Enter payment per year IN USD ($): "))
        rate = float(input("Enter annual interest rate IN %: ")) / 100
        years = float(input("Enter number of years: "))
        futureVal = paymentVal * (((1 + rate) ** years - 1) / rate)
        print(f"Future Value of Annuity = ${futureVal:.2f}")

    #Ameya -> Perpetuity Formula, code
    def perpetuity(self):
        paymentVal = float(input("Enter payment per year IN USD ($): "))
        rate = float(input("Enter annual interest rate IN %: ")) / 100
        presentVal = paymentVal / rate
        print(f"Present Value of Perpetuity = ${presentVal:.2f}")

calc = TimeValue()
calc.run()
