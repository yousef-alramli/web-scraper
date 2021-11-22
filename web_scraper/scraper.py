import requests
from bs4 import BeautifulSoup
import re

def get_citations_needed_count():
    content_file = open("./wiki_content.txt")
    content = content_file.read()
    content_file.close()

    soup = BeautifulSoup(content , "html.parser")
    div = soup.find("div" , class_="mw-parser-output")
    sub = div.find_all(class_="noprint Inline-Template Template-Fact")
    number_of_citations = len(sub)

    return number_of_citations


print("all citations count: ",get_citations_needed_count())

def get_citations_needed_report():

    content_file = open("./wiki_content.txt")
    content = content_file.read()
    content_file.close()

    soup = BeautifulSoup(content , "html.parser")
    div = soup.find("div" , class_="mw-parser-output")
    sub = div.find_all(class_="noprint Inline-Template Template-Fact")
    all_cintations_needed_text = []
    for i in sub:
        all_text = i.parent.get_text()
        reg = re.findall("\[.*$", all_text)
        citation_text = all_text.replace(f'{reg[0]}' , "")

        all_cintations_needed_text.append(citation_text)

    return all_cintations_needed_text

print("all reports needs citations: ",get_citations_needed_report())
