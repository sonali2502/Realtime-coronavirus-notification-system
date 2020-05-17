from plyer import notification # to generate notification
import requests # to request data from page while using web scarapping
from bs4 import BeautifulSoup # for parsing web data
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\\Users\\Mani\\Corona Notification\\coronaicon.ico",
        timeout = 3
    )
def getData(url):
    r = requests.get(url)
    return r.text # returns the data in text format

if __name__ == "__main__":
    while True:
        #notifyMe("Sonali", "Lets stop the spread of this virus together")
        myHtmlData = getData("https://www.mohfw.gov.in/") # you must have an internet connection
        #print(myHtmlData) # gets the data in html # to bring it in some form bs4 is used

        # using beautiful soup to convert the data of html page into some format, using dataframe.This is called
        # as parsing.Parsing: It involves breaking down of the scraped data into smaller bits. This is to aid
        # understanding of the scrapped data.

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify()) # Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document.
        myDataStr= ""
        for table in soup.find_all('table'):
            myDataStr += table.get_text()
        myDataStr = myDataStr[1:]
            
        itemList = myDataStr.split("\n\n")

        states=['Delhi','Haryana','Maharashtra']
        for item in itemList[3:36]:
            dataList= item.split('\n')
            if dataList[2] in states:
                print(dataList[1:])
                nTitle = "Cases of Covid-19"
                nText = f"State: {dataList[2]}\nTotal cases: {dataList[3]}\nCured: {dataList[4]}\nDeaths: {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(4)
        timee.sleep(3*60*60)

    
    
    



    