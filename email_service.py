from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Union
from smtplib import SMTP
from os import getenv

class EmailService:

    def __init__(self) -> None:
        self.client = SMTP(getenv('SMTP_HOST'))


    def _create_connection(self):
        self.client.connect(
            host= getenv('SMTP_HOST'),
            port= getenv('SMTP_PORT')
        )
        self.client.starttls()
        self.client.login(
            user= getenv('SMTP_USERNAME'),
            password= getenv('SMTP_PASSWORD')
        )


    def send_email(self, email_list: Union[str,list], subject:str, **kwargs):
        if isinstance(email_list,str):
            email_list = [email_list]
        self._create_connection()
        for email in email_list:
            mime = MIMEMultipart()
            mime['To'] = email
            mime['Subject'] = subject
            mime['From'] = getenv('SMTP_USERNAME')
            email_format = MIMEText(kwargs.get('message'),kwargs.get('format')) 
            mime.attach(email_format)
            try:
                self.client.sendmail(getenv('SMTP_USERNAME'),email,email_format.as_string())
            except:
                return "hola"
            finally:
                self.client.quit()
                self._close_connection()


    def _close_connection(self):
        self.client.close()
            

email_client = EmailService()
