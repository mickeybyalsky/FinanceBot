import yfinance as yf
from yfinance import Ticker
import math

def getStockName(message):
  data = Ticker(message).info
  stockName = data["shortName"]
  return stockName

def getStockSymbol(message):
  data = Ticker(message).info
  stockTicker = data["symbol"]
  return stockTicker

def getCurrentPrice(message):
  data = Ticker(message).info
  currentPrice = data["regularMarketPrice"]
  return currentPrice

def getChangeInPoints(message):
  data = Ticker(message).info
  currentValue = data["regularMarketPrice"]
  openValue = data["previousClose"]
  changeInPoints = currentValue-openValue
  return changeInPoints

def getChangeInPercent(message):
  data = Ticker(message).info
  currentValue = data["regularMarketPrice"]
  openValue = data["previousClose"]
  changeInPercent = (float(currentValue - openValue) /
                     openValue) * 100.00
  return changeInPercent

def getPreviousCloseValue(message):
  data = Ticker(message).info
  previousCloseValue = data["regularMarketPreviousClose"]
  return previousCloseValue

def getMarketOpen(message):
  data = Ticker(message).info
  marketOpen = data["regularMarketOpen"]
  return marketOpen

def getDayRange(message):
  data = Ticker(message).info
  dayHigh = data["regularMarketDayHigh"]
  dayLow = data["regularMarketDayLow"]
  dayRange = f"{dayLow:,.2f} - {dayHigh:,.2f}"
  return dayRange
  
def get52WkRange(message):
  data = Ticker(message).info
  fiftyTwoWeekLow = data["fiftyTwoWeekLow"]
  fiftyTwoWeekHigh = data["fiftyTwoWeekHigh"]
  yearRange = f"{fiftyTwoWeekLow:,.2f} - {fiftyTwoWeekHigh:,.2f}"
  return yearRange

def getComapnyBio(message):
  data = Ticker(message).info
  companyBio = data['longBusinessSummary']
  return companyBio

# def getTwoHundredDayAverage(message):
#   data = Ticker(message).info
#   twoHundredDayAverage = data["twoHundredDayAverage"]
#   return twoHundredDayAverage

# def getFiftyDayAverage(message):
#   data = Ticker(message).info
#   fiftyDayAverage = data["fiftyDayAverage"]
#   return fiftyDayAverage

def get24hrVolume(message):
  data = Ticker(message).info
  volume24hr = data["regularMarketVolume"]
  return volume24hr
  
def getMarketCap(message):
  data = Ticker(message).info
  marketCap = data['marketCap']
  marketCap = float(marketCap)
  millnames = ['',' K',' M',' B',' T']
  millidx = max(0,min(len(millnames)-1, int(math.floor(0 if marketCap == 0 else math.log10(abs(marketCap))/3))))
  return '{:.2f}{}'.format(marketCap / 10**(3 * millidx), millnames[millidx])
  
def getTrailingEPS(message):
  data = Ticker(message).info
  trailingEPS = data["forwardEps"]
  return trailingEPS

def getTrailingPE(message):
  data = Ticker(message).info
  trailingPE = data['trailingPE']
  return trailingPE

def getLastSplitFactor(message):
  data = Ticker(message).info
  lastSplitFactor = data['lastSplitFactor']
  return lastSplitFactor

def getImage(message):
  data = Ticker(message).info
  logoURL = data['logo_url']
  return logoURL

def getCategory(message):
  data = Ticker(message).info
  category = data['category']
  return category

def getSector(message):
  data = Ticker(message).info
  sector = data['sector']
  return sector

def getPEGRatio(message):
  data = Ticker(message).info
  pegRatio = data['pegRatio']
  return pegRatio

def getFullTimeEmployees(message):
  data = Ticker(message).info
  fullTimeEmployees = data['fullTimeEmployees']
  return fullTimeEmployees

def getDividendRate(message):
  data = Ticker(message).info
  dividendRate = data['dividendRate']
  return dividendRate

def getDividendYield(message):
  data = Ticker(message).info
  dividendYield = data['dividendYield']
  return dividendYield

def getExDividendDate(message):
  data = Ticker(message).info
  exDividendDate = data['exDividendDate']
  return exDividendDate
  
def getStockNews(message):
  return Ticker(message).news
  
def getCalendar(message):
  return Ticker(message).calendar

def getAnalystsRecommendations(message):
  return Ticker(message).recommendations.tail()
  
def getInstitutionalHolders(message):
  return Ticker(message).institutional_holders

def getMajorHolders(message):
  return Ticker(message).major_holders

def get5RecentActions(message):
  return Ticker(message).actions.tail().iloc[::-1]
  
def get10RecentActions(message):
  return Ticker(message).actions.tail(10).iloc[::-1]

# def getAllRecentActions(message):
#   return Ticker(message).actions.iloc[::-1]

def get5RecentDividends(message):#record dates
  return Ticker(message).dividends.tail().iloc[::-1]
  
def get10RecentDividends(message):
  return Ticker(message).dividends.tail(10).iloc[::-1]
  
# def getAllRecentDividends(message):
#   return Ticker(message).dividends.iloc[::-1]

def get5RecentSplits(message):
  return Ticker(message).splits.tail().iloc[::-1]
  
def getSustainability(message):
  return Ticker(message).sustainability

def getFinancials(message):
  return Ticker(message).financials

def getQuarterlyFinancials(message):
  return Ticker(message).quarterly_financials

def getBalanceSheet(message):
  return Ticker(message).balance_sheet

def getQuarterlyBalanceSheet(message):
  return Ticker(message).quarterly_balance_sheet

def getCashflow(message):
  return Ticker(message).cashflow

def getQuarterlyCashflow(message):
  return Ticker(message).quarterly_cashflow

def getEarnings(message):
  return Ticker(message).earnings

def getQuarterlyEarnings(message):
  return Ticker(message).quarterly_earnings
  

