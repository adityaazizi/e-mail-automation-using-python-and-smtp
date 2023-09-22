import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def FiletoList():
    receiver_list = []
    with open('receiver_list.txt', 'r') as file:
        for line in file:
            receiver_list.append(line.strip())
    return receiver_list


def ListtoFile(receiver_list):
    with open('receiver_list.txt', 'w') as file:
        for line in receiver_list:
            file.write(line + '\n')


def CreateList():
    new_receiver = input("Input new receiver: ")
    with open('receiver_list.txt', 'a') as file:
        file.write(f'\n{new_receiver}')
    print('New receiver successfully added.')
    ReadList()


def ReadList():
    with open('receiver_list.txt', 'r') as file:
        numb = 1
        for line in file:
            print(f'{numb}. {line}', end='')
            numb += 1


def UpdateList():
    ReadList()

    receiver_list = FiletoList()
    print("\n")
    item = int(input("Which item you want to update: "))

    receiver_list[item-1] = input("Input new value: ")
    ListtoFile(receiver_list)

    ReadList()


def DeleteList():
    ReadList()
    receiver_list = FiletoList()

    print("\n")
    item = int(input("Which item you want to delete: "))

    receiver_list.pop(item-1)
    ListtoFile(receiver_list)

    ReadList()


def SendEmail():
    smtp_server = 'smtp.gmail.com'
    port = 587  # For TLS
    sender_email = ''  # your email
    sender_password = ''  # your app pasword

    receiver_list = FiletoList()

    # change this into current directory
    folder_path = ''  # your attachment path
    attachment_files = glob.glob(os.path.join(folder_path, '*'))

    subject = input("Insert your subject here: ")
    body = input("Insert your message here: ")

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_list)
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    for file_path in attachment_files:
        with open(file_path, 'rb') as file:
            part = MIMEApplication(file.read(), Name=file_path)
        part['Content-Disposition'] = f'attachment; filename="{file_path}"'
        message.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_list, message.as_string())
        server.quit()

        print('Email with attachments sent successfully!')

    except Exception as e:
        print(f'Error: {str(e)}')


if __name__ == "__main__":
    while True:
        print(
            """

            Welcome, please choose an option:

            1. Add a recipient to the list.
            2. View the list of recipients.
            3. Edit the recipient list.
            4. Remove a recipient from the list.
            5. Send an email to list.
            6. Exit.
            """
        )

        answer = int(input("Insert menu (number only): "))

        if answer == 1:
            CreateList()

        elif answer == 2:
            ReadList()

        elif answer == 3:
            UpdateList()

        elif answer == 4:
            DeleteList()

        elif answer == 5:
            SendEmail()

        elif answer == 6:
            break
        else:
            print("Please input number from menu.")
