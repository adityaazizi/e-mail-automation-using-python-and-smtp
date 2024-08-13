import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from typing import List

from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = 'smtp.gmail.com'
PORT = 587

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
FOLDER_PATH = os.getenv('ATTACHMENT_PATH', 'attachment')

RECEIVER_LIST_FILE = 'receiver_list.txt'


def read_receiver_list() -> List[str]:
    with open(RECEIVER_LIST_FILE, 'r') as file:
        return [line.strip() for line in file]


def write_receiver_list(receiver_list: List[str]) -> None:
    with open(RECEIVER_LIST_FILE, 'w') as file:
        file.writelines(f'{line}\n' for line in receiver_list)


def add_receiver() -> None:
    new_receiver = input("Input new receiver: ").strip()
    with open(RECEIVER_LIST_FILE, 'a') as file:
        file.write(f'{new_receiver}\n')
    print('New receiver successfully added.')
    list_receivers()


def list_receivers() -> None:
    with open(RECEIVER_LIST_FILE, 'r') as file:
        for i, line in enumerate(file, start=1):
            print(f'{i}. {line.strip()}')


def update_receiver() -> None:
    receiver_list = read_receiver_list()
    list_receivers()

    try:
        item = int(input("Which item you want to update: ")) - 1
        receiver_list[item] = input("Input new value: ").strip()
        write_receiver_list(receiver_list)
        print("Receiver updated successfully.")
    except (IndexError, ValueError):
        print("Invalid selection.")

    list_receivers()


def delete_receiver() -> None:
    receiver_list = read_receiver_list()
    list_receivers()

    try:
        item = int(input("Which item you want to delete: ")) - 1
        receiver_list.pop(item)
        write_receiver_list(receiver_list)
        print("Receiver deleted successfully.")
    except (IndexError, ValueError):
        print("Invalid selection.")

    list_receivers()


def send_email() -> None:
    receiver_list = read_receiver_list()
    attachment_files = glob.glob(os.path.join(FOLDER_PATH, '*'))

    subject = input("Insert your subject here: ").strip()
    body = input("Insert your message here: ").strip()

    for receiver in receiver_list:
        message = MIMEMultipart()
        message['From'] = SENDER_EMAIL
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        for file_path in attachment_files:
            with open(file_path, 'rb') as file:
                part = MIMEApplication(
                    file.read(),
                    Name=os.path.basename(file_path)
                )
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            message.attach(part)

        try:
            with smtplib.SMTP(SMTP_SERVER, PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, receiver, message.as_string())
            print(f'Email sent successfully to {receiver}!')
        except Exception as e:
            print(f'Error sending email to {receiver}: {e}')


def main():

    options = {
        1: add_receiver,
        2: list_receivers,
        3: update_receiver,
        4: delete_receiver,
        5: send_email,
        6: exit
    }

    while True:
        print("""
            Welcome, please choose an option:
            1. Add a recipient to the list.
            2. View the list of recipients.
            3. Edit the recipient list.
            4. Remove a recipient from the list.
            5. Send an email to the list.
            6. Exit.
        """)

        try:
            choice = int(input("Insert menu (number only): "))
            action = options.get(choice)
            if action:
                action()
            else:
                print("Please input a valid number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
