# Rule-based FAQ chatbot

A simple FAQ chatbot implemented in Python, which makes answers to inquirers based on rule-based systems and keywords. The bot uses primitive Python features. It is not intelligent, it has no neural networks or any other complex ML models.

## How it works

The bot is rule-based. The algorithm is simple and is represented by a few steps:

1. Accepts the input from the user.

2. Converts the input string to the lowercase for case-insensitive comparison.

3. Looks for the keywords in the input string.

4. If any keyword is matched, returns the corresponding answer.

5. If no keywords were matched, returns the default message.

6. The user can type exit to quit the bot.

An example of the interaction with the bot:

---------------------------------------------------------------------------

Welcome to the FAQ Bot!

---------------------------------------------------------------------------

You can ask about:

fees, admission, library, hostel, transport, registration,

examinations, attendance, timings or support.

Type 'exit' to stop the program.

---------------------------------------------------------------------------

You: What are the fees?

Bot: Please check the portal or contact the administration

for current fee and payment information.

You: What are the library timings?

Bot: Please check your institutions website or contact

the library for current timings and book-related information.

You: exit

Thank you for using the FAQ Bot!

```

## Technologies

- Python 3

No other packages are used. The bot is written in pure Python.

## Project's Structure

```text

Rule-Based-FAQ-Chatbot/

│

├── faq_bot.py

├── README.md

├── statement.md

└──.gitignore

```

## How to Run

Make sure that Python3 is installed on your machine

```bash

python --version

```

1. Clone the repository

https://github.com/Make-it-Drac/FAQ-assistant-bot.git

2. Open the project folder

cd FAQ-assistant-bot

3. Run the Python program

Run main.py

## Limitations

The bot is rule-based, hence it has some shortcomings. For instance:

- It can't understand the context of the question.

- It doesn't have any ML models to understand the questions; it matches only the exact words.

- It doesn't remember the previous dialogues.

- It doesn't allow users to ask multiple questions in one message.

- The FAQ's database needs to be updated manually.

- The program's source code and the data are not separated.

## Future Improvements

The future improvements can be represented by the following ideas:

- Implement keyword matching.

- Add an option to match similar words (fuzzy matching).

- Develop a GUI for the application.

- Deploy an application as a web service.

- Store the data in databases.

- Add more categories of questions and answers.

- Separate the code and the data.

- Add an administrator panel to manage the data.

## Learning Outcomes

The project covers several topics related to Python programming language such as:

- Built-in data structures (lists, tuples).

- Built-in functions.

- Loops: for, while.

- Conditional statements: if.

- Working with strings.

- User input.

- The basic structure of the Python programs.

- Using rules to build a decision-making algorithm.

- Git and GitHub.
