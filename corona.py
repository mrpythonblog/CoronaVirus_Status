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

print("------------ Corona Virus Status ---------------")
print("[Patients] : \n+ {}\n".format(patients.strip("\n")))
print("[Deaths] : \n+ {}\n".format(deaths.strip("\n")))
print("[Recovered] : \n+ {}\n".format(recovered.strip("\n")))
print("------------------------------------------------")
