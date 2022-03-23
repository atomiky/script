import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key='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')
from_email = Email("awkys96@gmail.com")
to_email = To("412757277@qq.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)