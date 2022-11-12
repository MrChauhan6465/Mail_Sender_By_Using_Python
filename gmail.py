import smtplib as s 

ob = s.SMTP("smtp.gmail.com",587) #connecting to the gmail server 
ob.ehlo()
ob.starttls()

try :
   #code for getting password from your txt file
   with open('pass.txt', 'r') as file:
    data = file.read().replace('\n', '')
   user_mail = input("Enter your Gmail :\n")

   ob.login(user_mail,data)
   subject = input("Enter your gmail subject :\n ")

   body = input("Enter your message:")
   message = f"subject:{subject} \n\n {body}"

   list_address = [name for name in input("Enter receiver mails :\n(you can provide multiple mails also by providing spacing in between them.  )").split(" ")]

   ob.sendmail(user_mail,list_address,message)
   print(f"Your mail has been sent to : {list_address} :")

except Exception as e:
   print("Unfortunately can't sent the mail")


ob.quit()
