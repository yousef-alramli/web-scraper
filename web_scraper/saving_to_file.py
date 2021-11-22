import requests

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

content = requests.get(URL).content

cont = open("./wiki_content.txt", "w")
cont.write(f"{content}")
cont.close()