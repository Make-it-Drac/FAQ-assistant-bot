# Vityarthi VIT Bhopal FAQ Bot

A simple Python-based FAQ chatbot designed for **Vityarthi, VIT Bhopal** students. The bot uses keyword matching to answer common questions related to fees, admissions, library timings, hostel, transport, course registration, examinations, and attendance.

## Features

- Simple command-line interface (CLI)
- Keyword-based FAQ matching
- Covers common VIT Bhopal student queries
- No external Python libraries required
- Easy to modify and add new FAQs
- Exit command to safely stop the chatbot

## Topics Covered

The current FAQ database includes:

- Tuition and academic fees
- Admission, VITEEE, category and eligibility
- Library timings and book issue
- Hostel accommodation and hostel timings
- Attendance requirements
- Bus and transport services
- FFCS course registration
- CAT, FAT, marks, grading and CGPA

## How It Works

The chatbot stores FAQ rules as keyword-response pairs.

When a student enters a question:

1. The input is converted to lowercase.
2. The program checks the question against the stored keywords.
3. If a keyword is found, the corresponding answer is displayed.
4. If no keyword matches, the bot displays a fallback response.
5. Typing `exit` closes the program.

### Example

```text
Welcome to the FAQ Bot!

You: What are the fees?
Bot: Tuition and academic fees must be paid online through the VTOP portal (vtop.vitbhopal.ac.in) before the announced due date to avoid late fines.

You: What is the hostel in timing?
Bot: The Hostel in timings is 9:30 PM

You: exit
Thank you for visiting
```

## Requirements

- Python 3.x
- Any code editor or IDE such as VS Code, PyCharm, or IDLE

No third-party packages are required.

## How to Run

1. Install Python 3.x.
2. Save the chatbot code as:

```text
faq_bot.py
```

3. Open a terminal in the project folder.
4. Run:

```bash
python faq_bot.py
```

## Project Structure

```text
vityarthi-faq-bot/
│
├── faq_bot.py
├── README.md
├── statement.md
└── .gitignore
```

## Limitations

This project uses basic keyword matching rather than Natural Language Processing or an AI model. Therefore:

- It may not understand differently worded questions.
- It returns the first matching keyword rule.
- It does not maintain conversation history.
- FAQ information must be manually updated when university policies change.

## Future Improvements

Possible improvements include:

- Better natural-language matching
- Fuzzy matching for spelling mistakes
- More comprehensive VIT Bhopal FAQs
- GUI or web interface
- Database-backed FAQ storage
- Conversation history
- Admin interface for updating FAQs
- Integration with an official university information source

## Disclaimer

This is a student-developed FAQ chatbot for educational/project purposes. Information provided by the bot should be verified against official VIT Bhopal/VTOP announcements before making academic, financial, hostel, or administrative decisions.

## Author

Developed as a **Vityarthi / VIT Bhopal student project** using Python.
