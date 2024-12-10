import datetime

def calculate_emi(principal, rate_of_interest, tenure_months):
    """Calculate the EMI for a loan."""
    monthly_rate = rate_of_interest / (12 * 100)  # Convert annual interest rate to monthly and decimal
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return round(emi, 2)

def collect_personal_information():
    """Collect personal and address information."""
    print("Enter Personal and Address Information:")
    personal_info = {}

    personal_info["Full Name"] = input("Full name: ")
    personal_info["Address"] = input("Address (e.g., house number, street name): ")

    while True:
        personal_info["City"] = input("City: ")
        if personal_info["City"].isalpha():
            break
        print("Invalid input. Please enter a valid city name.")

    while True:
        personal_info["State"] = input("State: ")
        if personal_info["State"].isalpha():
            break
        print("Invalid input. Please enter a valid state name.")

    while True:
        personal_info["Pin Code"] = input("Pin code: ")
        if personal_info["Pin Code"].isdigit() and len(personal_info["Pin Code"]) == 6:
            break
        print("Invalid input. Pin code must be a 6-digit number.")

    while True:
        personal_info["Phone Number"] = input("Phone number: ")
        if personal_info["Phone Number"].isdigit() and len(personal_info["Phone Number"]) == 10:
            break
        print("Invalid input. Phone number must be a 10-digit number.")

    personal_info["Email ID"] = input("Email ID: ")

    return personal_info

def collect_loan_details():
    """Collect loan details."""
    print("\nEnter Loan Details:")
    loan_details = {}
    loan_details["Loan Type"] = input("Loan type (Personal/Home/Business/Car): ")

    while True:
        try:
            loan_details["Loan Amount"] = float(input("Loan amount borrowed: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        try:
            loan_details["Loan Tenure"] = int(input("Loan tenure (total repayment period in months): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    while True:
        try:
            interest_rate = float(input("Annual interest rate (in %): "))
            loan_details["Monthly EMI"] = calculate_emi(
                loan_details["Loan Amount"], interest_rate, loan_details["Loan Tenure"]
            )
            print(f"Your monthly EMI will be: {loan_details['Monthly EMI']}")
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    loan_details["Repayment Start Date"] = input("Repayment start date (YYYY-MM-DD): ")
    return loan_details

def collect_repayment_information():
    """Collect repayment details."""
    print("\nEnter Repayment Information:")
    repayment_info = {}
    repayment_info["Total Number of Repayments"] = int(input("Total number of repayments (e.g., monthly or weekly): "))
    repayment_info["Missed Installments"] = int(input("Number of delayed or missed installments: "))
    repayment_info["Reason for Delay"] = input("Reason for delayed repayment: ")
    repayment_info["Partial Repayment"] = input("Have you been able to partially repay? (Yes/No): ")
    return repayment_info

def collect_mortgage_details():
    """Collect mortgage details."""
    print("\nEnter Mortgage Details:")
    mortgage_details = {}
    mortgage_details["Property Mortgaged"] = input("Property mortgaged for the loan (e.g., house, jewelry, vehicle): ")

    while True:
        try:
            mortgage_details["Current Estimated Value"] = float(input("Current estimated value of mortgaged property: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    mortgage_details["Third-Party Appraisal"] = input("Was a third-party appraisal done? (Yes/No): ")
    return mortgage_details

def collect_assistance_feedback():
    """Collect feedback on assistance required."""
    print("\nEnter Assistance and Feedback Details:")
    assistance_feedback = {}
    assistance_feedback["Repayment Restructuring Assistance"] = input("Do you require assistance for repayment restructuring? (Yes/No): ")
    assistance_feedback["Contacted Debt Collection Agency"] = input("Have you contacted the debt collection agency for help? (Yes/No): ")
    assistance_feedback["Financial Counseling"] = input("Would you be interested in financial counseling services? (Yes/No): ")
    assistance_feedback["Additional Comments"] = input("Any additional comments or concerns: ")
    return assistance_feedback

def collect_consent():
    """Collect consent for data use."""
    print("\nConsent and Declaration:")
    consent = input("Do you consent to the use of this information for analysis and assistance purposes only? (Yes/No): ")
    return consent

if __name__ == "__main__":
    personal_info = collect_personal_information()
    loan_details = collect_loan_details()
    repayment_info = collect_repayment_information()
    mortgage_details = collect_mortgage_details()
    assistance_feedback = collect_assistance_feedback()
    consent = collect_consent()

    print("\nSummary of Provided Information:")
    print("Personal Information:", personal_info)
    print("Loan Details:", loan_details)
    print("Repayment Information:", repayment_info)
    print("Mortgage Details:", mortgage_details)
    print("Assistance and Feedback:", assistance_feedback)
    print("Consent Given:", consent)

    if consent.lower() == "yes":
        print("\nThank you for providing your information. We will use this for analysis and assistance purposes.")
    else:
        print("\nConsent not given. No action will be taken.")
