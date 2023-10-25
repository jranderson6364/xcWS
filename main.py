import csv
import requests
from bs4 import BeautifulSoup
import re
from operator import itemgetter


def main():
    timesList = []
    schoolIDList = getSchools()
    meetName = schoolIDList[0]
    schoolIDList.pop(0)
    for schoolID in schoolIDList:
        schoolDataList = schoolTopTimes(schoolID)
        for time in schoolDataList:
            timesList.append(time)

    timesList = sorted(timesList, key=itemgetter(3))
    count =1
    for x in timesList:
        
        print(f'{count}. {x[3]} {x[2]}')
        count+=1

def schoolTopTimes(schoolID): 
    data = []
    url = "https://www.athletic.net/CrossCountry/seasonbest?SchoolID=" + str(schoolID)
    r = requests.get(url)   
    soup = BeautifulSoup(r.content, 'html.parser')
    txt = soup.get_text()
    _,txt = txt.split("5,000")
    x=  re.findall("([0-9])\.([0-9][0-9]?)(.*?\s.*?)([1-9][0-9]\:[0-9][0-9](?:\.?\d))",txt)
    c = 1
    for item in x:
        row = [item[0],item[1],item[2],item[3],schoolID]
        
        if int(row[0]) != c or int(row[0]) > 7:
            c+=1
            continue
            
        else:
            c+=1
            data.append(row)
    return data

def getSchools():
    return ["Regionals","13062","13060","13063"]

    

if __name__ == "__main__":
    main()