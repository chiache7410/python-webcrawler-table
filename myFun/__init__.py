import urllib.request
import csv
def getHtml(url):
    return urllib.request.urlopen(url).read()
def saveHtml(file_name, file_content):
    with open(file_name, "wb") as f:
        f.write(file_content)
def readHtml(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        return f.read()
def getValue(html, headword, endword):
    return str(html).split(endword)[-2].split(headword).pop()
def getTabel(html, headword, endword):
    data = []
    for s in str(html).split(endword)[:-1]:
        data.append(s.split(headword)[-1])
    return data
def saveCsv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        csv.writer(f).writerows(data)
def listStrip(data):
    outdata = []
    for d in data:
        outdata.append(d.strip())
    return outdata
def listReplace(data, word):
    outdata = []
    for d in data:
        outdata.append(d.replace(word, ""))
    return outdata
def readCSV(filename):
    with open(filename, 'r', newline='', encoding='utf-8-sig') as f:
        return list(csv.reader(f))