import yfinance as yf

def extractBasicInfo(data):
    keysToExtract = ['longName','website','sector','fullTimeEmployees', 'marketCap', 'totalRevenue','epsTrailingTwelveMonths']
    basicInfo ={}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key]
        else:
            basicInfo[key] = ""
    return basicInfo

def getCompanyStockInfo(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    basicInfo = extractBasicInfo(company.info)
    print(basicInfo)

#get all stock info
getCompanyStockInfo("MSFT")