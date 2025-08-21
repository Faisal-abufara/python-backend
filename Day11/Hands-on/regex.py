import re
'''
no module

email="faisalpartners.com"

if not "@" in email or not "." in email:
    print("invalid email")

else:
    print(f"valid emal: {email}")
    '''

emailtest = "Faisal@partner.com"

ReForEmail = r'^([\w\.-]+)@([\w\.-]+)\.(\w{2,})$'

search = re.match(ReForEmail,emailtest)

if search:
    print("valid email")
else:
    print("invalid email")
