import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import random
import tweepy

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('filepath', scope)
#"C:\Users\zayaa\Downloads\cosmic-tensor-416004-7a4b1035ec68.json"
client = gspread.authorize(creds)

sheet = client.open('Hedera sheet').sheet1

def add_row(data):
    sheet.append_row(data)

def remove_row():
    sheet.delete_rows(2)

def update_sheet(data):
    add_row(data)
    remove_row()

while True:
    data = ["sending wallet", "receiving wallet", "transaction volume", "time"]
    update_sheet(data)
    time.sleep(600)

#api key X1NMqsB81ewDRkfmo85Mt5o5M
#api key secret RqAhUOlCnMKR0iU17fhHxlcqMSKmfZv9G91whWF5mWCY1wpmNv
# access token  1674548290472357889-E482CItXNx8l5uSEk2qUl0xu0P45wc
# access token secret 7eSbxoMnaydJOKxvowAKb1Js22UQwNjJ9LDJBO3MEcDJj

auth = tweepy.OAuthHandler('api key', 'api key secret')
auth.set_access_token('access token', 'acccess token secret')
api = tweepy.API(auth)

def tweet_update(data):

    messages = [
        "Breaking news!!! Massive transfer from big whale on Hedera!!! {2} amount from {0} wallet to {1} wallet.",
        "Alert!!! A huge transaction on Hedera just took place!!! {2} transferred from {0} to {1}.",
        "Just in!!! A big whale on Hedera moved {2} from {0} to {1}. Stay tuned for more updates!",
        "News flash!!! A significant amount of {2} just moved between wallets on Hedera! From {0} to {1}.",
        "Update!!! A major transaction has occurred on Hedera! {2} has been transferred from {0} to {1}."
    ]

    # Randomly select a message
    message = random.choice(messages)
    # Format the message with data
    message = message.format(data[0], data[1], data[2])

    api.update_status(message)

while True:
    data = sheet.row_values(1)  
    tweet_update(data)
    time.sleep(3600) 



