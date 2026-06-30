Customer_Name = input("Enter the name of the Customer:\n")
Age = int(input("Enter the age of the Customer/user:\n"))
if Age <= 18:
    print("Age is not valid\n")
    exit()
Monthly_Salary = int(input("Enter the Monthly Salary of the Customer:\n"))
if Monthly_Salary <= 25000:
    print("Salary is rejected")
else:
    print("Salary is accepted")
Credit_Score = int(input("Enter the credit Score:\n"))
if Credit_Score < 300 or Credit_Score > 900:
  print("credit score is not valid")
  exit()
print(" 1:Salaried\n 2:Self-Employed\n 3:Government\n 4:Business\n")
Employment_Type = int(input("Enter the Employment Type:\n"))
if Employment_Type < 1 or Employment_Type > 4:
    print("Invalid Employment Type")
    exit()
print(" 1:Home\n 2:Car\n 3:Personal\n 4:Education\n")
Loan_Type = int(input("Enter the loan type:\n"))
if Loan_Type < 1 or Loan_Type > 4:
    print("Invalid Loan Type")
    exit()
Loan_Amount = int(input("Enter the Loan Amount:"))
if Loan_Amount <=  0:
    print( "Zero loan amount is not supportive")
    exit()
Loan_Tenure_Years = int(input("Enter the loan tenure years:"))
if Loan_Tenure_Years <= 0:
    print("Not eligible")
    exit()
Existing_EMI = int(input("Enter the Exisitiong EMI:"))
match Employment_Type:
    case 1:
        print("Salaried")
    case 2:
        print("Self - Employed")
    case 3:
        print("Government")
    case 4:
        print("Business")
    case _:
        print("Default")
        exit()
match Loan_Type:
    case 1:
        print("Home")
        Int_rate = 8.5
        print(f"Interest rate:{Int_rate}%")
    case 2:
        print("Car")
        Int_rate = 9.5
        print(f"Interest rate:{Int_rate}%")
    case 3:
        print("Personal")
        Int_rate = 12
        print(f"Interest rate :{Int_rate}%")
    case 4:
        print("Education")
        Int_rate = 7.5
        print(f"Interest rate :{Int_rate}%")
    case _:
        print("Default")
        exit()
Interest = (Loan_Amount * Int_rate * Loan_Tenure_Years)/ 100
Total_Amount = Loan_Amount + Int_rate
Months = Loan_Tenure_Years * 12
Monthly_EMI = Total_Amount / Months
print("********* Information of the Loan Applicant **********")
print(f"Name :{Customer_Name}")
print(f"Age:{Age}")
print(f"Monthy Salary:{Monthly_Salary}")
print(f"Credit Score:{Credit_Score}")
print(f"Employment Type:{Employment_Type}")
print(f"Loan Type:{Loan_Type}")
print(f"Loan Amount:{Loan_Amount}")
print(f"Loan Tenure Years:{Loan_Tenure_Years}")
print(f"Existing EMI:{Existing_EMI}")
print(f"Interest :{Interest}")
print(f"Total_Amount:{Total_Amount}")
print(f"Months:{Months}")
print(f"Monthly_EMI:{Monthly_EMI}")














        




