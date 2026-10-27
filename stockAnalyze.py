import yfinance as yf
import requests
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

def extractBasicInfo(data):
    keysToExtract = ['longName','website','sector','fullTimeEmployees', 'marketCap', 'totalRevenue','epsTrailingTwelveMonths']
    basicInfo ={}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key]
        else:
            basicInfo[key] = ''
    return basicInfo

def getPriceHistory(company):
    historyDf = company.history(period='1y')
    prices = historyDf['Open'].tolist()
    dates = historyDf.index.strftime('%Y-%m-%d').tolist()
    return {
        'price': prices,
        'date': dates
    }

def getEarningDates(company):
    earningDatesDf = company.earnings_dates
    allDates = earningDatesDf.index.strftime('%Y-%m-%d').tolist()
    date_objects = [datetime.strptime(date, '%Y-%m-%d') for date in allDates]
    currentDate = datetime.now()
    futureDates = [date.strftime('%Y-%m-%d') for date in date_objects if date > currentDate]
    return futureDates

def getCompanyNews(company):
    newsList = yf.Search(company, news_count=100).news
    allNewsArticles = []
    for newsDict in newsList:
        newsDictToAdd = {
            'title': newsDict['title'],
            'link': newsDict['link']
        }
        allNewsArticles.append(newsDictToAdd)
    return allNewsArticles

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36'
}

def extractCompanyNewsArticles(newsArticles):
    url = newsArticles[0]['link']
    page = requests.get(url, headers=headers)
    print(page.text)   

def getCompanyStockInfo(tickerSymbol):
    # Get data from Yahoo Finance API
    company = yf.Ticker(tickerSymbol)

    # Get basic info on company
    basicInfo = extractBasicInfo(company.info)
    priceHistory = getPriceHistory(company)
    futureEarningDates = getEarningDates(company)
    newsArticles = getCompanyNews(tickerSymbol)
    extractCompanyNewsArticles(newsArticles)

getCompanyStockInfo('MSFT')