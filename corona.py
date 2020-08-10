from bs4 import BeautifulSoup as bs
from requests import get

url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdUOA?Si"

response = get(url)

content = response.content.decode()

page = bs(content,"html.parser")


informations = page.find_all("div" , "maincounter-number")

patients = informations[0].text # Number of Patients
deaths = informations[1].text # Number of Deaths
recovered = informations[2].text # Number Of Recovered

print("Patients : {}".format(patients))
print("Deaths : {}".format(deaths))
print("Recovered : {}".format(recovered))

