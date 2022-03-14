import yagmail
import os
sender = 'example@gmail.com'
receiver = 'myfusbo2020@gmail.com'

subject = "This is the subject"

contents = """
Here is the content of the email!
Hello!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")