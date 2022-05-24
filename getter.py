import yfinance as yf

#def gettest(message):
  #data = yf.Ticker(message).actions
  # data = yf.Ticker(message).news
  # print(data.get('title'))
  #return data
  
def getStockName(message):
  data = yf.Ticker(message).info
  stockName = data["longName"]
  return stockName

def getStockSymbol(message):
  data = yf.Ticker(message).info
  stockTicker = data["symbol"]
  return stockTicker

def getCurrentPrice(message):
  data = yf.Ticker(message).info
  currentPrice = data["regularMarketPrice"]
  return currentPrice

def getChangeInPoints(message):
  data = yf.Ticker(message).info
  changeInPoints = float(data["regularMarketPrice"]) - float(
      data["previousClose"])
  return changeInPoints

def getChangeInPercent(message):
  data = yf.Ticker(message).info
  changeInPercent = ((data["regularMarketPrice"] - data["previousClose"]) /
                     data["previousClose"]) * 100
  return changeInPercent

def getPreviousCloseValue(message):
  data = yf.Ticker(message).info
  previousCloseValue = data["previousClose"]
  return previousCloseValue

def getMarketOpen(message):
  data = yf.Ticker(message).info
  marketOpen = data["regularMarketOpen"]
  return marketOpen

def getDayRange(message):
  data = yf.Ticker(message).info
  dayHigh = data["regularMarketDayHigh"]
  dayLow = data["regularMarketDayLow"]
  dayRange = f"{dayLow} - {dayHigh}"

def get52WkRange(message):
  data = yf.Ticker(message).info
  fiftyTwoWeekLow = data["fiftyTwoWeekLow"]
  fiftyTwoWeekHigh = data["fiftyTwoWeekHigh"]
  yearRange = f"{fiftyTwoWeekLow} - {fiftyTwoWeekHigh}"
  return yearRange

def getComapnyBio(message):
  data = yf.Ticker(message).info
  companyBio = data['longBusinessSummary']
  return companyBio

def getTwoHundredDayAverage(message):
  data = yf.Ticker(message).info
  twoHundredDayAverage = data["twoHundredDayAverage"]
  return twoHundredDayAverage

def getFiftyDayAverage(message):
  data = yf.Ticker(message).info
  fiftyDayAverage = data["fiftyDayAverage"]
  return fiftyDayAverage

def get24hrVolume(message):
  data = yf.Ticker(message).info
  volume24hr = data["volume24Hr"]
  return volume24hr
  
def getMarketCap(message):
  data = yf.Ticker(message).info
  marketCap = data['marketCap']
  marketCap = float('{:.3g}'.format(marketCap))
  magnitude = 0
  while abs(marketCap) >= 1000:
      magnitude += 1
      marketCap /= 1000.0
  return '{} {}'.format('{:f}'.format(marketCap).rstrip('0').rstrip('.'),  ['', 'K', 'M', 'B', 'T'][magnitude])

def getTrailingEPS(message):
  data = yf.Ticker(message).info
  trailingEPS = data["trailingEps"]
  return trailingEPS

def getTrailingPE(message):
  data = yf.Ticker(message).info
  trailingPE = data['trailingPE']
  return trailingPE

def getLastSplitFactor(message):
  data = yf.Ticker(message).info
  lastSplitFactor = data['lastSplitFactor']
  return lastSplitFactor

def getImage(message):
  data = yf.Ticker(message).info
  logoURL = data['logo_url']
  return logoURL

def getCategory(message):
  data = yf.Ticker(message).info
  category = data['category']
  return category

def getSector(message):
  data = yf.Ticker(message).info
  sector = data['sector']
  return sector

def getPEGRatio(message):
  data = yf.Ticker(message).info
  pegRatio = data['pegRatio']
  return pegRatio

def getFullTimeEmployees(message):
  data = yf.Ticker(message).info
  fullTimeEmployees = data['fullTimeEmployees']
  return fullTimeEmployees

def getStockNews(message):
  return yf.Ticker(message).news
  
def getCalendar(message):
  return yf.Ticker(message).calendar

def getAnalystsRec(message):
  return yf.Ticker(message).recommendations
  
def getInstitutionalHolders(message):
  return yf.Ticker(message).institutional_holders

def getMajorHolders(message):
  return yf.Ticker(message).major_holders

#print(yf.Ticker("aapl").major_holders)

# print("%.2f" % currentPrice)
# print("%.2f" % changeInPoints)
# CNBC
# Last | 12:13 PM EDT
# Enbridge Inc
# 55.82
#
# Yahoo
# Enbridge Inc. (ENB.TO)
# At close:  04:00PM EDT
# 58.47
