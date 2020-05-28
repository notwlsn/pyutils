from lxml import html
import requests

url = input("Boss url with guild tag: ")
page = requests.get(url)
tree = html.fromstring(page.content)

#This will create a list of scores:
scores = tree.xpath('//td/text()')

def convert(scores):

    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in scores:
        new += x

    # return string
    return new

print(convert(scores))
# print(scores)

with open('output.txt', 'w', encoding="utf8") as filehandle:
    for listitem in scores:
        listitem.replace(" ", "")
        filehandle.write('%s\n' % listitem)
