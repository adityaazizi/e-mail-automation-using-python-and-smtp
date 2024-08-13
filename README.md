# E-Mail Automation using Python

This project is a practical implementation of basic Python programming concepts that I learned during my initial stages of learning. The program automates the process of sending emails, including subjects, attachments, and message content, to multiple recipients listed in receiver_list.txt. Currently, it runs on the command-line interface (CLI), but there are plans to add a graphical user interface (GUI) in the future to enhance user-friendliness.

## Features

- Send emails with subject, body, and attachments.
- Manage recipients through a text file.
- Command-line interface for simplicity.

## Prerequisites

- Python 3.x installed on your machine.
- A Gmail account to send emails.
- Basic knowledge of using the command line.

## Getting Started

Follow these steps to set up and run the program:

### 1. Clone the Repository

First, clone this repository to your local device:

```bash
git clone https://github.com/adityaazizi/e-mail-automation-using-python-and-smtp.git
cd e-mail-automation-using-python-and-smtp
```

### 2. Create Virtual Environment

It is recommended to create a virtual environment to manage dependencies. Run the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

Once your virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Your Environment

Email Credentials:

- Create a .env file in the project root directory and add your email credentials:

```bash
SENDER_EMAIL='your-email@gmail.com'
SENDER_PASSWORD='your-app-password'
ATTACHMENT_PATH='attachment'
```

- Follow the instructions [here](https://support.google.com/mail/answer/185833?hl=en) to create an app password for your Gmail account.

Attachment path:

- Ensure that all attachment files are placed in the attachment folder, or specify the path in the .env file.

### 5. Prepare Your Recipient List

Add the email addresses of recipients in the receiver_list.txt file, with each email on a new line

### 6. Run the Program

After setting everything up, you can run the program with:

```bash
python main.py
```

### 7. Follow the CLI Instructions

The program will guide you through adding, viewing, updating, and deleting recipients, as well as sending emails.

## Future Plans

- Graphical User Interface (GUI): A future update will include a GUI to make the application more accessible and user-friendly.
- Enhanced Features: Additional features like scheduling emails, logging sent emails, and more.

## Contribution

Feel free to contribute to this project by forking the repository, making your changes, and submitting a pull request.

## Contact

If you have any feedback, suggestions, or questions, feel free to reach out:

email: azizi.business@gmail.com

Good Luck! 😊
