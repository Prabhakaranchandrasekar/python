import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys


# A class is written that will be used to have all the functions that will be used For getting various details which are required for sending the mail and finally sending the mail
class MyMail:

    # a constructor is written to initialise all the required class variables and set the value of all these class variables to none
    def _init_(self):
        self.sender_email = None
        self.receiver_email = None
        self.sender_password = None
        self.email_subject = None
        self.email_body = None

    # a function is written to get the details of the sender the various details that are captured by this function are the email address of the sender and the corresponding password associated with that entered email
    def get_sender_details(self):
        print("Enter the email of the sender::")
        self.sender_email = input()
        print("Enter the Password of the sender::")
        self.sender_password = input()

    # another function is written that is used to retrieve all the receiver details the various  receiver details that are captured by this functions are the email is of the receiver
    def get_reciever_details(self):
        print("Enter the email of the receiver::")
        self.receiver_email = input()

    # another function is written that is particularly capturing the details off the email the various  aspects which are captured by this function are the subject of the sending email and the body of the sending email
    def get_email_details(self):
        print("Enter the Subject of the sending email::")
        self.email_subject = input()
        print("Enter the Body of the sending email::")
        self.email_body = input()

    # this function is used to print all the details Android by the user like sender email receiver email email subject email body and  verify those details
    def print_details(self):
        print("Sender Mail::")
        print(self.sender_email)
        print("Receiver Mail::")
        print(self.receiver_email)
        print("Email Subject::")
        print(self.email_subject)
        print("Email Body::")
        print(self.email_body)

    # and finally a function is written that is actually used to send the email to the specified receiver email address by the specified input sender email address along with the corresponding subject of the email body of the email and if there is an attachment that is also sent with the email
    def send_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.email_subject
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        text = """\\{}""".format(self.email_body)
        html = """ 
        <html>  
          <body>  
            <p>Hi,<br>  
               this is a test email by Nirnay!<br> .  
            </p>  
          </body>  
        </html>  
        """

        obj1 = MIMEText(text, "plain")
        obj2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(obj1)
        message.attach(obj2)

        context_obj = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context_obj) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())

        print("Email sent successfully.")

    #  in the end the main function is written that will be used to call all these functions by creating the object of the above-written class


def main():
    mailer = MyMail()

    while (True):
        print("Please choose one of the below-listed options::")
        print("1. To enter the details of the sender. [Sender email and sender Password]")
        print("2. To enter the details of the receiver. [Receiver email]")
        print("3. To enter the sending email's subject.")
        print("4. To enter the body of the sending email.")
        print("5. To send the email.")
        print(
            "6. To verify all the entered details. [Sender email, Sender Password, Receiver email, Email Subject and Email Body.")
        print("7. To exit from the code execution.")
        menu_choice = input()
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            mailer.get_sender_details()

        elif menu_choice == 2:
            mailer.get_reciever_details()

        elif menu_choice == 3:
            mailer.get_email_details()

        elif menu_choice == 4:
            mailer.get_email_details()

        elif menu_choice == 5:
            mailer.send_email()

        elif menu_choice == 6:
            mailer.print_details()

        elif menu_choice == 7:
            sys.exit()

        print("wanna proceed with the program or want to exit the program [Y/n]")
        continue_or_exit = input()

        if continue_or_exit == 'y' or continue_or_exit == 'Y':
            pass
        elif continue_or_exit == 'n' or continue_or_exit == 'N':
            sys.exit()


if _name_ == '_main_':
    main()