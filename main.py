#List of rules to store our FAQ data 
faq_rules = [
    (["fee", "fees","tuition","payment"],"Tuition and academic fees must be paid online through the VTOP portal (vtop.vitbhopal.ac.in) before the announced due date to avoid late fines."),
    (["admission","viteee", "category", "eligibility"], "Admissions at VIT Bhopal are granted through VITEEE rank counseling across Category 1 to Category 5 fee structures."),
    (["library", "timing", "books", "hours"],"The Central Library in the Academic Block 1 and Academic Block 2 is open on all working day till 7 P.M. Books can be issued using your Student ID card."),
    (["hostel accommodation", "room"], "Hostel accommodation is allotted on a first-come-first-served basis. Contact the hostel office for details."),
    (["hostel","intimings"]," The Hostel in timings is 9:30 PM"),
    (["attendance", "debarred", "percent"], "Minimum 75% attendance is mandatory in each subject to appear for FAT. Students with CGPA >= 9.0 (9-Pointers) may get attendance relaxation."),
    (["bus", "transport", "route", "commute", "sehore"],"VIT Bhopal operates day-scholar bus services covering major routes across Bhopal, Sehore, and nearby regions. Transport fee is paid annually on VTOP."),
    (["ffcs","slot","course","registration", "subject", "faculty"],"Course registration is conducted via FFCS (Fully Flexible Credit System) on VTOP which allow students to select preferred faculty and time slots."),
    (["exam", "cat","fat", "marks","grading", "cgpa"],"Evaluation includes CAT-1, CAT-2, internal lab assessments, and FAT. VIT Bhopal follows a relative grading system displayed on VTOP.")

]

#Function modules
#1: Displaying the welcome screen
def welcome():
    print("-"*75)
    print("                      Welcome to the FAQ Bot!                      ")
    print("-"*75)
    print("You can ask about: fees, admission, library,hostel,transport,course registration,examination or attendance")
    print("Type 'exit' to stop the program.")
    print("-"*75)

#2: Cleaning the user input 
def clean(input):
    return input.lower()   

#3: Finding the matching answer
def ans(ques):
    #Loop through our list of rules
    for keywords,response in faq_rules:
        for word in keywords:
            if word in ques:
                return response
                
    #Fallback if no match found
    return "sorry, I did not understand type again or contact the help desk?"

#5: Main control flow 
def start():
    welcome()
    
    while True:
        question=input("\nYou: ")
        
        cleaned_ques =clean(question)
        
        #Break condition to stop the loop
        if cleaned_ques == "exit":
            print("Thank you for visiting")
            break
            
        #Get answer and printing
        answer= ans(cleaned_ques)
        print("Bot:", answer)


#Start
if __name__ == "__main__":
    start()