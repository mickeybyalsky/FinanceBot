import discord
from discord.ext import commands
import requests
import os
from getter import*
import yfinance as yf

client = discord.Client()
client = commands.Bot(command_prefix="$")

#########
#THINGS TO ADD: 
# - watchlist (would print out all Symbol, price, change in points & %)
# - nicer tables for calender 
# - more bot commands
# - use embedds for messages
# - try to add stock logo to messages
# - after hours prices
#########

x=yf.Ticker("aapl").calendar
x = x.values.tolist()
print(x)
print(type(x))

@client.event
async def on_ready():
    print("Running")

@client.command(aliases=['cp'])
async def currentPrice(ctx, message):
  message = message.upper()
  stockSymbol = getStockSymbol(message)
  currentPrice = getCurrentPrice(message)
  pointsChange = getChangeInPoints(message)
  percentChange = getChangeInPercent(message)
  # image = getImage(message)
  # print(image)
  await ctx.send(f"Current price of {stockSymbol}: {currentPrice:.2f}\nChange: {pointsChange:.2f} | {percentChange:.2f}%")

#         f"The after hour price of {ticker} is {afterHoursPrice}. Change: {afterHoursChangeInPoints} Percent Change {afterHoursChangeInPercent}.\nTime of price: {timeOfRetrieval}"


@client.command(aliases=['tr', 'range today','dr'])
async def todayRange(ctx, message):
  message = message.upper()
  stockSymbol = getStockSymbol(message)  
  dRange = getDayRange(message)
  await ctx.channel.send(f"Today's Range of {stockSymbol}: {dRange}."
    )
  
@client.command(aliases=['yr', '52w'])
async def yearRange(ctx, message):
  message = message.upper()
  stockSymbol = getStockSymbol(message)
  yearRange = get52WkRange(message)
  await ctx.channel.send(f"Year Range of {stockSymbol}: {yearRange}.")

@client.command(aliases=['mc'])
async def marketCap(ctx, message):
  message = message.upper()
  stockSymbol = getStockSymbol(message)
  marketCap = getMarketCap(message)
  await ctx.channel.send(f"{stockSymbol} Market Cap: {marketCap}.")

@client.command(aliases=['pc','pcv','prev'])
async def previousCloseValue(ctx, message):
  stockSymbol = getStockSymbol(message)
  prevCloseValue = getPreviousCloseValue(message)
  await ctx.channel.send(f"{stockSymbol} Previous Close Value: {prevCloseValue:.2f}")

@client.command(aliases=['open','mo'])
async def marketOpen(ctx, message):
  stockSymbol = getStockSymbol(message)
  marketOpenValue = getMarketOpen(message)
  await ctx.channel.send(f"{stockSymbol} Market Open Value: {marketOpenValue:.2f}")

@client.command(aliases=['bio','summary'])
async def companyBio(ctx, message):
  stockSymbol = getStockSymbol(message)
  companyBio = getComapnyBio(message)
  await ctx.channel.send(companyBio)

@client.command(aliases=['employees','staff'])
async def fullTimeEmployees(ctx, message):
  stockSymbol = getStockSymbol(message)
  ftEmployees = getFullTimeEmployees(message)
  await ctx.channel.send(f"{stockSymbol} Full Time Employees: {ftEmployees}")

@client.command(aliases=['24hr volume','tvol'])
async def volume24hr(ctx, message):
  stockSymbol = getStockSymbol(message)
  volume24h = get24hrVolume(message)
  await ctx.channel.send(f"{stockSymbol} 24hr Volume: {volume24h}")

@client.command(aliases=['pe','P/E'])
async def trailingPERatio(ctx, message):
  stockSymbol = getStockSymbol(message)
  trailingPE = getTrailingPE(message)
  await ctx.channel.send(f"{stockSymbol} Trailing P/E Ratio: {trailingPE}")

@client.command(aliases=['EPS','eps'])
async def trailingEPS(ctx, message):
  stockSymbol = getStockSymbol(message)
  trailingEPS = getTrailingEPS(message)
  await ctx.channel.send(f"{stockSymbol} Trailing EPS: {trailingEPS}")

@client.command(aliases=['ls'])
async def lastSplit(ctx, message):
  stockSymbol = getStockSymbol(message)
  lastSplitFactor = getLastSplitFactor(message)
  await ctx.channel.send(f"{stockSymbol} Last Split Factor: {lastSplitFactor}")

@client.command()
async def news(ctx, message):
  data = getStockNews(message)
  index = 0
  for sub in data:
    if index == 5:
      break
    await ctx.channel.send(f"**Title:** {sub['title']}\n**Publisher:** {sub['publisher']}\n**Link:** <{sub['link']}>\n‎\n")
    index+=1
    
@client.command(aliases=['events'])
async def calendar(ctx, message):
  calendar = getCalendar(message)
  await ctx.channel.send(calendar)
  
client.run(os.environ['TOKEN'])
#keep_alive()

