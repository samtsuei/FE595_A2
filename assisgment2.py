## Reference used to develop the code
##  Beautifulsoup
##https://www.crummy.com/software/BeautifulSoup/bs4/doc/
##https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup

# String and loop
##https://www.w3schools.com/python/python_string_formatting.asp
##https://www.pythonforbeginners.com/control-flow-2/python-for-and-while-loops

import requests
from bs4 import BeautifulSoup
for x in range(0, 50, 1):

     url=" http://18.207.92.139:8000/random_company"
     html_content = requests.get(url).text
     ##print(html_content)

     soup = BeautifulSoup(html_content, "lxml")
     soup_text =soup.get_text()
     ##print(soup_text)

     name_start = soup_text.find("Name")
     name_end =soup_text[name_start:].find("\n")
     name_end = name_start + name_end
     name = soup_text[name_start:name_end]

     purpose_start = soup_text.find("Purpose")
     purpose_end = soup_text[purpose_start:].find("\n")
     purpose_end = purpose_start+purpose_end
     purpose = soup_text[purpose_start:purpose_end]

      ##print(name)
      ##print(purpose)

      f = open("myfile.txt","a")
      f.write(name + '\n')
      f.write(purpose + '\n')