import yfinance as yf
from datetime import datetime

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

def getCompanyStockInfo(tickerSymbol):
    # Get data from Yahoo Finance API
    company = yf.Ticker(tickerSymbol)

    # Get basic info on company
    basicInfo = extractBasicInfo(company.info)
    priceHistory = getPriceHistory(company)
    futureEarningDates = getEarningDates(company)
    newsArticles = getCompanyNews(tickerSymbol)

getCompanyStockInfo('MSFT')