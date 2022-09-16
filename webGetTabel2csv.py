import sys
import myFun
import csv
def main(url, page, previouspage, notemp):
    nowurl = url + '&page=' + page
    print(nowurl)
    input("確認url後才按Enter")
    tempfilename = 'htmltemp' + page
    if notemp == 'Y':
        myFun.saveHtml(tempfilename, myFun.getHtml(nowurl))
        print('重新下載')
    html = myFun.readHtml(tempfilename)
    data = myFun.getValue(html, '</td></tr>', '<center>')
    data = data.split('<tr')
    data.pop(0)
    data = myFun.listReplace(data, '</a>')
    lists = []
    for l in data:
        data = myFun.getTabel(l, '>', '</td>')
        data = myFun.listReplace(data, '\n')
        data = myFun.listStrip(data)
        lists.append(data)
    data = []
    for l in lists:
        d = []
        d.append(l[0])
        d.append(l[1])
        d.append(l[2])
        data.append(d)
    nextpage = myFun.getValue(html, '<a href="showlist.asp?page=', '&name=OEMMap&Cmd=Map&ZoomPage=searchmapbranch&Genus=twbank&GenusType=mapbranch&sqlchk=open')
    if previouspage != nextpage:
        print(nextpage)
        kk = input('有進入IF，回答Y繼續')
        if kk == 'y':
            data = data + main(url, nextpage, page, notemp)
    return data
if len(sys.argv) == 3:
    data = []
    data = myFun.readCSV('固定不變.csv')
    data = data + main("https://bot.map.com.tw/search_engine/showlist.asp?name=OEMMap&Cmd=Map&ZoomPage=searchmapbranch&Genus=twbank&GenusType=mapbranch&sqlchk=open", '1', '0', sys.argv[2])
    print(data)
    input("按Enter開始寫入檔案")
    myFun.saveCsv(sys.argv[1], data)
else:
    print('無檔案路徑')
    input("按Enter結束")