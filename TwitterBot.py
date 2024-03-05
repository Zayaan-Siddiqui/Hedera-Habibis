import time
import random
import tweepy
import os
from dotenv import load_dotenv


load_dotenv()

client = tweepy.Client(bearer_token=os.getenv('BEARER_TOKEN'))
client = tweepy.Client(
      consumer_key=os.getenv("API_KEY"), consumer_secret=os.getenv("API_KEY_SECRET"),
      access_token=os.getenv("ACCESS_TOKEN"), access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
  )
def tweet_data(data):
    templates = [
        "🌟 Oh la la! Just stumbled upon an AVeryMoneymaker account on Hedera. This one's dripping in dollars, honey! 💸💋 Address: {evm_address}, Balance: ${usd_balance} #RichAndRisque #Hedera #HederaHabbies",
        "🔥 Hot diggity! Found a saucy AVeryMoneybags account on Hedera. It's raining dollars over here! 💰💋 Address: {evm_address}, Balance: ${usd_balance} #SugarDaddyStatus #Hedera #HederaHabbies",
        "💎 Well, well, well... Look what we've got here! An AVeryBaller account on Hedera. This wallet's got it all, including stacks of cash! 💰✨ Address: {evm_address}, Balance: ${usd_balance} #RichAndReady #Hedera #HederaHabbies",
        "💸 Money, money, money! Just spotted an AVeryCashKing account on Hedera. Cash rules everything around me! 💰💰💰 Address: {evm_address}, Balance: ${usd_balance} #CashIsKing #Hedera #HederaHabbies",
        "🥂 Cheers to the high life! Came across an AVeryLavish account on Hedera. Living large and living it up! 💎💸 Address: {evm_address}, Balance: ${usd_balance} #LavishLifestyle #Hedera #HederaHabbies",
        "💰💋 Feeling lucky? Found an AVeryMoneyMaker account on Hedera Hashgraph. It's a jackpot of riches! 💰💋 Address: {evm_address}, Balance: ${usd_balance} #FortuneFinder #Hedera #HederaHabbies",
        "💼 Business in the front, party in the back! Discovered an AVeryBigSpender account on Hedera. Spending money like it's going out of style! 💸💃 Address: {evm_address}, Balance: ${usd_balance} #BigSpenderEnergy #Hedera #HederaHabbies",
        "💰💋 Oh my, what do we have here? An AVeryDollarDynamo account on Hedera. It's a treasure trove of cash and kisses! 💋💸 Address: {evm_address}, Balance: ${usd_balance} #MoneyAndMore #Hedera #HederaHabbies",
        "💸💎 Bling bling, baby! Spotted an AVeryMoneyManiac account on Hedera. Making it rain like there's no tomorrow! 💸💎 Address: {evm_address}, Balance: ${usd_balance} #BlingBling #Hedera #HederaHabbies",
        "🍾 Pop the champagne! Just discovered an AVeryFortunate account on Hedera. Living the high life with pockets full of cash! 💰🥂 Address: {evm_address}, Balance: ${usd_balance} #FortuneFinds #Hedera #HederaHabbies"
        "💰💼 Cha-ching! Stumbled upon an AVeryWealthy account on Hedera. This wallet is a goldmine! 💼💰 Address: {evm_address}, Balance: ${usd_balance} #WealthyWonder #Hedera #HederaHabbies",
        "💎💵 Shine bright like a diamond! Just found an AVeryRiches account on Hedera. Fortune favors the bold! 💵💎 Address: {evm_address}, Balance: ${usd_balance} #RichesRising #Hedera #HederaHabbies",
        "💸💎 Money talks! Spotted an AVeryCashCraze account on Hedera. Cash flow never looked so good! 💎💸 Address: {evm_address}, Balance: ${usd_balance} #CashCraze #Hedera #HederaHabbies",
        "🌟💰 Stars aligning! Came across an AVeryWealthWizard account on Hedera. Magic in the air and money in the wallet! 💰🌟 Address: {evm_address}, Balance: ${usd_balance} #WealthWizardry #Hedera #HederaHabbies",
        "💵💼 Making it rain! Discovered an AVeryMoneyMaster account on Hedera. Mastering the art of wealth accumulation! 💼💵 Address: {evm_address}, Balance: ${usd_balance} #MoneyMaster #Hedera #HederaHabbies",
        "💰🌈 Rainbow of riches! Just found an AVeryWealthWave account on Hedera. Riding the wave to financial success! 🌈💰 Address: {evm_address}, Balance: ${usd_balance} #WealthWave #Hedera #HederaHabbies",
        "💸✨ Sparkle and shine! Spotted an AVeryCashChampion account on Hedera. Championing the cause of wealth accumulation! 💰✨ Address: {evm_address}, Balance: ${usd_balance} #CashChampion #Hedera #HederaHabbies",
        "💼💰 Making moves! Came across an AVeryMoneyMogul account on Hedera. Moguling the world with wealth! 💰💼 Address: {evm_address}, Balance: ${usd_balance} #MoneyMogul #Hedera #HederaHabbies",
        "💎💰 Diamonds are forever! Discovered an AVeryRichRuler account on Hedera. Ruling the realm of riches! 💰💎 Address: {evm_address}, Balance: ${usd_balance} #RichRuler #Hedera #HederaHabbies",
        "🌟💸 Shining bright! Found an AVeryCashKingpin account on Hedera. Kingpin of cash and kingpin of success! 💸🌟 Address: {evm_address}, Balance: ${usd_balance} #CashKingpin #Hedera #HederaHabbies"
    ]

    template = random.choice(templates)
    tweet_text = template.format(evm_address=data['evm_address'], usd_balance=data['usd_balance'])
    client.create_tweet(text=tweet_text)
    print("Tweeted:", tweet_text)


    time.sleep(60 * 60 * 5) # Tweet every 5 hours

