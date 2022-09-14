import urllib.request
import csv
import time
import sys
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html
def getName(html):
    str0 = str(html, 'utf-8')
    str1 = str0.split('</td>')
    str2 = str1[7].split('<td class="rt">')
    return str2[1]
def numberToName(number):
    aurl = "https://ibank.tcbbank.com.tw/PIB/cb5/cb501005/CB" + number + ".faces"
    print(aurl)
    input("確定開始?")
    html = getHtml(aurl)
    return getName(html)
def main1(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8-sig') as f:
        lines = csv.reader(f)
        for line in lines:
            d = []
            d.append(line[0])
            d.append(numberToName(line[0]))
            print(line[0])
            time.sleep(1)
            data.append(d)
    print(data)
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerows(data)


if len(sys.argv) == 1:
    while True:
        num = input('輸入分機:')
        if num == 'q':
            break
        print(numberToName(num))
elif len(sys.argv) == 2:
    main1(sys.argv[1])
else:
    print('無該選項')