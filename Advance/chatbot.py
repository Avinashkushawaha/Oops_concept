import re

def main():
    print("WELCOME TO DYRS COLLEGE OF ENGINEERING INQUIRY CHATBOT")

    # Student Details
    name = input("1) What is your name? (Alphabetic characters and spaces only): ")
    while not name.replace(" ", "").isalpha():
        name = input("Invalid input. Please enter a valid name: ")

    contact_number = input("2) What is your contact number? (10-digit numeric only): ")
    while not (contact_number.isdigit() and len(contact_number) == 10):
        contact_number = input("Invalid input. Please enter a valid 10-digit contact number: ")

    email = input("3) What is your email address? (e.g., example@gmail.com): ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email = input("Invalid email. Please enter a valid email address: ")

    dob = input("4) What is your date of birth? (YYYY-MM-DD): ")
    while not re.match(r"\d{4}-\d{2}-\d{2}", dob):
        dob = input("Invalid format. Please enter DOB in YYYY-MM-DD format: ")

    # Qualification Details
    qualifications = ["10th", "12th", "Diploma", "Graduate"]
    highest_qualification = input(f"5) What is your highest qualification? {qualifications}: ")
    while highest_qualification not in qualifications:
        highest_qualification = input(f"Invalid input. Choose from {qualifications}: ")

    percentage = input("6) What percentage/grade did you achieve in your last qualification? (Numeric only): ")
    while not percentage.replace(".", "").isdigit():
        percentage = input("Invalid input. Please enter a numeric value: ")

    completion_year = input("When did you complete your last qualification? (YYYY): ")
    while not (completion_year.isdigit() and len(completion_year) == 4):
        completion_year = input("Invalid year. Please enter in YYYY format: ")

    courses = {
        "10th": ["Diploma in CSE", "IT", "EC", "CIVIL", "MECHANICAL", "ELECTRICAL"],
        "12th": ["Graduation in CSE", "IT", "EC", "CIVIL", "MECHANICAL", "ELECTRICAL"],
        "Diploma": ["Graduation in CSE", "IT", "EC", "CIVIL", "MECHANICAL", "ELECTRICAL"],
        "Graduate": ["Post graduation in CSE", "IT", "EC", "CIVIL", "MECHANICAL", "ELECTRICAL"]
    }
    interested_course = input(f"7) Which course are you interested in? {courses[highest_qualification]}: ")
    while interested_course not in courses[highest_qualification]:
        interested_course = input(f"Invalid choice. Please choose from {courses[highest_qualification]}: ")

    previous_studies = input("8) From where did you complete your previous studies? (Alphabetic only): ")
    while not previous_studies.replace(" ", "").isalpha():
        previous_studies = input("Invalid input. Please enter alphabetic characters only: ")

    entrance_exam = input("9) Have you taken any entrance exam for this course? (YES or NO): ").upper()
    while entrance_exam not in ["YES", "NO"]:
        entrance_exam = input("Invalid input. Please answer with YES or NO: ")

    # Student Interests
    modes = ["Online", "Offline", "Hybrid"]
    mode_of_study = input(f"10) What is your preferred mode of study? {modes}: ")
    while mode_of_study not in modes:
        mode_of_study = input(f"Invalid input. Please choose from {modes}: ")

    hostel = input("11) Are you interested in hostel accommodation? (YES or NO): ").upper()
    while hostel not in ["YES", "NO"]:
        hostel = input("Invalid input. Please answer with YES or NO: ")

    counseling = input("12) Would you like to attend an online or offline admission counseling session? (YES or NO): ").upper()
    while counseling not in ["YES", "NO"]:
        counseling = input("Invalid input. Please answer with YES or NO: ")

    campus_visit = input("13) Are you interested in visiting our campus for a tour? (YES or NO): ").upper()
    while campus_visit not in ["YES", "NO"]:
        campus_visit = input("Invalid input. Please answer with YES or NO: ")

    sources = ["Newspaper", "Internet", "Other"]
    source = input(f"14) How did you hear about this college? {sources}: ")
    while source not in sources:
        source = input(f"Invalid input. Please choose from {sources}: ")

    tuition_info = input("15) Do you require information about tuition fees and payment plans? (YES or NO): ").upper()
    while tuition_info not in ["YES", "NO"]:
        tuition_info = input("Invalid input. Please answer with YES or NO: ")

    funding_options = ["Self-funded", "Sponsor", "Education Loan"]
    funding = input(f"16) How will you be funding your education? {funding_options}: ")
    while funding not in funding_options:
        funding = input(f"Invalid input. Please choose from {funding_options}: ")

    print("\nTHANK YOU FOR SUBMITTING YOUR DETAILS!")
    print("Our team will connect with you soon for further communication/discussion.")

if __name__ == "__main__":
    main()
