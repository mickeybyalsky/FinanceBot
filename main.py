import discord
from discord.ext import commands
import requests
import os
from getter import*
import yfinance as yf
from discord import embeds

client = discord.Client()
client = commands.Bot(command_prefix="$")

##########################################################
#THINGS TO ADD: 
################################### - pull dividends from .info 
################################### - help command
# - use embedds for messages
# - try to add stock logo to messages
# - watchlist (would print out all Symbol, price, change in points & %)
# - nicer tables for calender
# - charts using historical data
################################### - more bot commands
# - after hours prices
# - commas for big numbers in data frames (revenue)
########################################################

@client.command(brief='cp - Shows the Current Price of a Stock.', aliases=['cp'])
async def currentPrice(ctx, message):
  stockSymbol = getStockSymbol(message)
  currentPrice = getCurrentPrice(message)
  pointsChange = getChangeInPoints(message)
  percentChange = getChangeInPercent(message)
  #image = getImage(message)
  await ctx.channel.send(f"Current price of {stockSymbol}: {currentPrice:.2f}\nChange: {pointsChange:.2f} | {percentChange:.2f}%")
  
  # f"The after hour price of {ticker} is {afterHoursPrice}. Change: {afterHoursChangeInPoints} Percent Change {afterHoursChangeInPercent}.\nTime of price: {timeOfRetrieval}"

@client.command(brief='tr - Shows the Day Range of a Stock.', aliases=['tr', 'range today'])
async def todayRange(ctx, message):
  message = message.upper()
  stockSymbol = getStockSymbol(message)  
  dRange = getDayRange(message)
  await ctx.channel.send(f"Today's Range of {stockSymbol}: {dRange}.")
  
@client.command(brief='yr - Shows the Year Range of a Stock.',aliases=['yr', '52w'])
async def yearRange(ctx, message):
  message = message.upper()
  stockSymbol = getStockSymbol(message)
  yearRange = get52WkRange(message)
  await ctx.channel.send(f"Year Range of {stockSymbol}: {yearRange}.")

@client.command(brief='mc - Shows the Market Cap of a Stock.', aliases=['mc'])
async def marketCap(ctx, message):
  message = message.upper()
  stockSymbol = getStockSymbol(message)
  marketCap = getMarketCap(message)
  await ctx.channel.send(f"{stockSymbol} Market Cap: {marketCap}.")

@client.command(brief='pc - Shows the closing value on the previous trading day.', aliases=['pc','pcv','prev'])
async def previousCloseValue(ctx, message):
  stockSymbol = getStockSymbol(message)
  prevCloseValue = getPreviousCloseValue(message)
  await ctx.channel.send(f"{stockSymbol} Previous Close Value: {prevCloseValue:,.2f}")

@client.command(brief='mo - Shows the Market Open Price of a Stock.', aliases=['open','mo'])
async def marketOpen(ctx, message):
  stockSymbol = getStockSymbol(message)
  marketOpenValue = getMarketOpen(message)
  await ctx.channel.send(f"{stockSymbol} Market Open Value: {marketOpenValue:.2f}")

@client.command(brief='bio - Shows a description of the Stock.', aliases=['bio','summary'])
async def companyBio(ctx, message):
  stockSymbol = getStockSymbol(message)
  companyBio = getComapnyBio(message)
  await ctx.channel.send(f"__{stockSymbol} Company Bio:__\n{companyBio}")

@client.command(brief='fte - Shows the number of FT Employees at the Company.', aliases=['employees','fte','staff'])
async def fullTimeEmployees(ctx, message):
  stockSymbol = getStockSymbol(message)
  ftEmployees = getFullTimeEmployees(message)
  await ctx.channel.send(f"{stockSymbol} Full Time Employees: {ftEmployees:,}")

@client.command(brief='tv - Shows the amount of Stock traded in the last 24 hours.', aliases=['24hr volume','tvol','tv'])
async def volume24hr(ctx, message):
  stockSymbol = getStockSymbol(message)
  volume24h = get24hrVolume(message)
  await ctx.channel.send(f"{stockSymbol}'s 24hr Volume: {volume24h:,}")

@client.command(brief='pe - Shows the P/E ratio based on last 12 months of earnings.', aliases=['pe','P/E'])
async def trailingPERatio(ctx, message):
  stockSymbol = getStockSymbol(message)
  trailingPE = getTrailingPE(message)
  await ctx.channel.send(f"{stockSymbol} Trailing P/E Ratio: {trailingPE:.2f}")

@client.command(brief='eps - Shows the EPS based on last 12 months of earnings.',aliases=['EPS','eps'])
async def trailingEPS(ctx, message):
  stockSymbol = getStockSymbol(message)
  trailingEPS = getTrailingEPS(message)
  await ctx.channel.send(f"{stockSymbol} Trailing EPS: {trailingEPS:.2f}")

@client.command(brief='ls - Shows the Last Split Factor.',aliases=['ls'])
async def lastSplit(ctx, message):
  stockSymbol = getStockSymbol(message)
  lastSplitFactor = getLastSplitFactor(message)
  await ctx.channel.send(f"{stockSymbol} Last Split Factor: {lastSplitFactor}")

@client.command(brief='news - Shows 5 news articles related to the stock.')
async def news(ctx, message):
  data = getStockNews(message)
  index = 0
  string = " "
  for sub in data: 
    if index == 5:
      break
    string +=f"**Title:** {sub['title']}\n**Publisher:** {sub['publisher']}\n**Link:** <{sub['link']}>\n‎\n"
    index+=1
  await ctx.channel.send(string)
    
@client.command(aliases=['events'])
async def calendar(ctx, message):
  stockSymbol = getStockSymbol(message)
  calendar = getCalendar(message)
  await ctx.channel.send(f"{stockSymbol} Calendar:\n{calendar}")

@client.command(brief='cat - Shows the Stock Sector and Category.',aliases=['category','sector','cat'])
async def categoryAndSector(ctx, message):
  category = getCategory(message)
  sector = getSector(message)
  await ctx.channel.send(f"Category: {category}\nSector: {sector}")

@client.command(brief='peg - Shows the PEG based on last 12 months of earnings.',aliases=['PEG','peg'])
async def trailingPEGRatio(ctx, message):
  stockSymbol = getStockSymbol(message)
  trailingPEG = getPEGRatio(message)
  await ctx.channel.send(f"{stockSymbol} PEG Ratio: {trailingPEG}")

@client.command(brief='dr - Shows the Annual Dividend Rate.',aliases=['dr'])
async def dividendRate(ctx, message):
  stockSymbol = getStockSymbol(message)
  dividendRate = getDividendRate(message)
  await ctx.channel.send(f"{stockSymbol} Annual Dividend Rate: ${dividendRate} per share")

@client.command(brief='dr - Shows the Annual Dividend Yield.',aliases=['dy'])
async def dividendYield(ctx, message):
  stockSymbol = getStockSymbol(message)
  dividendYield = getDividendYield(message)
  print(dividendYield)
  await ctx.channel.send(f"{stockSymbol} Annual Dividend Yield: {dividendYield*100.0:.2f}%")
  

@client.command(brief='ar - Shows analysts recommendations for the Stock.',aliases=['analyst','recs','rec','ar'])
async def analystRecommendation(ctx, message):
  stockSymbol = getStockSymbol(message)
  analystRecs = getAnalystsRecommendations(message)
  await ctx.channel.send(f"{stockSymbol} Analyst Recommendations:\n {analystRecs}")

@client.command(brief='ih - Shows the largest Institutional Holders for the Stock.',aliases=['ih'])
async def institutionalHolders(ctx, message):
  stockSymbol = getStockSymbol(message)
  institutionalHolders = getInstitutionalHolders(message)
  await ctx.channel.send(f"{stockSymbol} Institutional Holders:\n {institutionalHolders}")

@client.command(brief='mh - Shows the Major Holders for the Stock.',aliases=['mh'])
async def majorHolders(ctx, message):
  stockSymbol = getStockSymbol(message)
  majorHolders = getMajorHolders(message)
  await ctx.channel.send(f"{stockSymbol} Major Holders:\n {majorHolders}")

@client.command(brief='5ra - Shows the 5 latest Dividends or Stock Splits.',aliases=['5ra'])
async def recentActions5(ctx, message):
  stockSymbol = getStockSymbol(message)
  recentActions5 = get5RecentActions(message)
  await ctx.channel.send(f"{stockSymbol}'s 5 Recent Actions:\n {recentActions5}")

@client.command(brief='10ra - Shows the 10 latest Dividends or Stock Splits.',aliases=['10ra'])
async def recentActions10(ctx, message):
  stockSymbol = getStockSymbol(message)
  recentActions10 = get10RecentActions(message)
  await ctx.channel.send(f"{stockSymbol}'s 10 Recent Actions:\n {recentActions10}")

@client.command(brief='5d - Shows the 5 latest Dividends.',aliases=['5d'])
async def recentDividends5(ctx, message):
  stockSymbol = getStockSymbol(message)
  recentDividends5 = get5RecentDividends(message)
  await ctx.channel.send(f"{stockSymbol}'s 5 Recent Dividend Record Dates:\n {recentDividends5}")

@client.command(brief='10d - Shows the 10 latest Dividends.',aliases=['10d'])
async def recentDividends10(ctx, message):
  stockSymbol = getStockSymbol(message)
  recentDividends10 = get10RecentDividends(message)
  await ctx.channel.send(f"{stockSymbol}'s 10 Recent Dividend Record Dates:\n {recentDividends10}")

@client.command(brief='5s - Shows the 5 latest Stock Splits.',aliases=['5s'])
async def recentSplits5(ctx, message):
  stockSymbol = getStockSymbol(message)
  recentSplits5 = get5RecentSplits(message)
  await ctx.channel.send(f"{stockSymbol}'s 5 Recent Stock Splits:\n {recentSplits5}")

@client.command(brief='sus - Shows Company Sustainability for the Stock.',aliases=['sus'])
async def companySustainability(ctx, message):
  stockSymbol = getStockSymbol(message)
  sustainability = getSustainability(message)
  await ctx.channel.send(f"{stockSymbol} Company Sustainability:\n {sustainability}")

@client.command(brief='fin - Shows Company Financials.',aliases=['fin'])
async def financials(ctx, message):
  stockSymbol = getStockSymbol(message)
  financials = getFinancials(message)
  await ctx.channel.send(f"{stockSymbol} Company Financials:\n {financials}")

@client.command(brief='qfin - Shows Quarterly Company Financials.',aliases=['qfin'])
async def quarterlyFinancials(ctx, message):
  stockSymbol = getStockSymbol(message)
  quarterlyFinancials = getQuarterlyFinancials(message)
  await ctx.channel.send(f"{stockSymbol} Quarterly Company Financials:\n {quarterlyFinancials}")

@client.command(brief='bs - Shows Company\'s Balance Sheet.',aliases=['bs'])
async def balanceSheet(ctx, message):
  stockSymbol = getStockSymbol(message)
  balanceSheet = getBalanceSheet(message)
  await ctx.channel.send(f"{stockSymbol} Balance Sheet:\n {balanceSheet}")

@client.command(brief='qbs - Shows Company\'s Quarterly Balance Sheet.',aliases=['qbs'])
async def quarterlyBalanceSheet(ctx, message):
  stockSymbol = getStockSymbol(message)
  quarterlyBalanceSheet = getQuarterlyBalanceSheet(message)
  await ctx.channel.send(f"{stockSymbol} Quarterly Balance Sheet:\n {quarterlyBalanceSheet}")

# @client.command(brief='cf - Shows Company Cashflow.',aliases=['cf'])
# async def cashflow(ctx, message):
#   stockSymbol = getStockSymbol(message)
#   cashflow = getCashflow(message)
#   await ctx.channel.send(f"{stockSymbol} Cashflow:\n {cashflow}")

# @client.command(brief='qcf - Shows Company Quarterly Cashflow.',aliases=['qcf'])
# async def quarterlyCashflow(ctx, message):
#   stockSymbol = getStockSymbol(message)
#   quarterlyCashflow = getQuarterlyCashflow(message)
#   await ctx.channel.send(f"{stockSymbol} Quarterly Cashflow:\n {quarterlyCashflow}")

@client.command(brief='ce - Shows Company Earnings.',aliases=['ce'])
async def companyEarnings(ctx, message):
  stockSymbol = getStockSymbol(message)
  companyEarnings = getEarnings(message)
  await ctx.channel.send(f"{stockSymbol} Company Earnings:\n {companyEarnings}")

@client.command(brief='qce - Shows Quarterly Company Earnings.',aliases=['qce'])
async def quarterlyEarnings(ctx, message):
  stockSymbol = getStockSymbol(message)
  quarterlyCompanyEarnings = getQuarterlyEarnings(message)
  await ctx.channel.send(f"{stockSymbol} Quarterly Company Earnings:\n {quarterlyCompanyEarnings}")
  
client.run(os.environ['TOKEN'])
#keep_alive()

