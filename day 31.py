'''
Create a program that checks if a given string is a valid email address.
'''
email_domains = ['@gmail.com', '@yahoo.com', '@aol.com']
email = input('What is your email? ')
def email_check(email=email):
    domain_start_index = email.find('@')
    email_domain = email[domain_start_index:]
    if email_domain in email_domains:
        print('Valid Email')
    else:
        print('Not a Valid Email')
email_check()