import yagmail
from datetime import date

# start a connection
yag = yagmail.SMTP("bodieplants@gmail.com", oauth2_file="~/plant-table-oauth2.json")

# date
today = date.today()
monthday = today.strftime("%b %d, %Y")

def refillwater():
    # define the variables
    to = "bodenschatz.nathan@gmail.com"
    to2 = "erin.steinmetz16@gmail.com"
    ####### Remove next # to send to both addresses
    # to = [to,to2]
    subject = "Refill Plant Watering Jug %s!" % monthday
    body = "Do it now you bitch!"

    # send the email
    yag.send(to,subject,contents=body)
    # print("Email sent!")
