# Eric McMullen April 18, 2019.
# Extreme Weather Alert System. Used openweathermap.org api, SMTP email sending and hosted for free on pythonanywhere.com


import requests
import time


def weather_data(query):
	res=requests.get('http://api.openweathermap.orgXXXXXXXXXXXXXXXXXX);
	return res.json();

def print_weather(result,city):
  hot = ("{}".format(result['main']['temp'])) # Isolating the current temperature from the API output.
  return hot

def main():
  city='Toronto'
  recieve= 'XXXX@gmail.com' # Create a list of all emails which will recieve an alert.  
  print()
  try:
    query='q='+city;
    w_data=weather_data(query);
    tmp = print_weather(w_data,city)
    #print(city,"is currently",float(tmp),"C")
    #print (float(tmp))
    extreme = (float(tmp))
    extreme = float(35.00) # Set what the extreme temperature value is.

    while (float(tmp) <= extreme):
        print("Checking... the weather is not dangerously hot. Its only",float(tmp))
        time.sleep(30) # Test for Current Temperature > 35 deg C every 30 seconds.
        main()
  except:
    print('City name not found.')
  if (float(tmp) >= extreme): #If current temperature is above 35 deg C.
    import smtplib, ssl
    def read_creds():
        user = passw = ""
        user = 'XXX@gmail.com' # Email address for the sender's email.
        passw = 'XXXXXXXXXX' # Password for the sender's email.
        return user, passw
    port = 465
    sender, password = read_creds()
    sender = 'XXXXXXXXXXXX@gmail.com' # Email account for the sender's email.
    subject = "Subject: Extreme Heat Alert!"
    text = " It is currently " + str(tmp) + " deg C in "  + str(city) + ". Stay hydrated!"
    message = subject + text
    context = ssl.create_default_context()
    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    print("Sent.")
    exit() # Ending loop once the alert is sent. This stops numerous alerts.
main()
exit()
