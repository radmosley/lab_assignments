#Extract Header

email_in = input('What is your email address: ')
email_wo_com = email_in[0:-4]
fin_email = email_wo_com.split('@')
print(fin_email[1])
