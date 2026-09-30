# Project Statement

## Project Title

**Vityarthi VIT Bhopal FAQ Bot**

## Introduction

Students often need quick access to information about university procedures such as fees, admission, attendance, hostel rules, transport, course registration, and examinations. Searching through different notices, portals, and university resources for simple questions can be time-consuming.

The **Vityarthi VIT Bhopal FAQ Bot** is a simple Python-based chatbot developed to provide quick answers to frequently asked questions related to VIT Bhopal.

## Problem Statement

Students may have difficulty finding answers to common administrative and academic questions. A simple FAQ chatbot can provide frequently requested information through an easy command-line interface.

The project aims to create a lightweight chatbot that identifies keywords in a student's question and returns the corresponding predefined answer.

## Objectives

The main objectives of this project are:

1. To develop a simple FAQ chatbot using Python.
2. To provide quick responses to common VIT Bhopal student queries.
3. To implement keyword-based question matching.
4. To create a simple and user-friendly command-line interface.
5. To make the FAQ database easy to update and maintain.
6. To demonstrate basic Python concepts such as lists, loops, functions, conditions, and string processing.

## Scope of the Project

The chatbot currently handles questions related to:

- Fees and tuition payments
- Admission and VITEEE
- Categories and eligibility
- Library timings and books
- Hostel accommodation and timings
- Attendance requirements
- Bus and transport services
- FFCS course registration
- CAT, FAT, marks, grading, and CGPA

The project is intended as an educational prototype and can be expanded into a larger student-support system.

## Methodology

The chatbot follows a rule-based approach.

### Step 1: Store FAQ Rules

Each FAQ contains a list of keywords and its corresponding response.

```python
(["fee", "fees", "tuition", "payment"], "Tuition and academic fees...")
```

### Step 2: Accept User Input

The chatbot asks the user to enter a question.

### Step 3: Clean the Input

The input is converted to lowercase so that matching is not affected by capitalization.

```python
def clean(input):
    return input.lower()
```

### Step 4: Match Keywords

The chatbot checks each FAQ rule and searches for matching keywords in the user's question.

### Step 5: Generate Response

If a keyword is found, the associated response is displayed.

If no keyword matches, the chatbot returns a fallback message asking the user to try again or contact the help desk.

## Technologies Used

- **Programming Language:** Python
- **Interface:** Command Line Interface (CLI)
- **Data Storage:** Python list of tuples
- **Libraries:** No external libraries required

## Expected Outcome

The expected outcome is a functional command-line FAQ chatbot capable of answering common VIT Bhopal student questions using predefined rules.

The project also demonstrates how simple rule-based systems can be used to build basic conversational applications.

## Future Scope

The project can be improved by adding:

- Natural Language Processing (NLP)
- Fuzzy keyword matching
- A graphical user interface
- A web-based interface
- A database for storing FAQs
- More university-specific FAQs
- Multilingual support
- Conversation history
- Automatic FAQ updates from authorized university sources

## Conclusion

The Vityarthi VIT Bhopal FAQ Bot is a simple and practical Python project that demonstrates the implementation of a rule-based chatbot. It provides quick access to predefined student information while keeping the implementation easy to understand and modify.

The project can serve as a foundation for developing a more advanced student-support chatbot in the future.
