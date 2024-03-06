# Hedera Habibi

Hedera Habibi is a Twitter bot that alerts its users whenever it finds a Hedera account with a substantial amount of money in it. The bot uses the Hedera API to parse account data and tweets about accounts with a balance greater than $10,000.

## Features
- **Account Monitoring**: The bot continuously monitors Hedera accounts and their balances.
- **Alerts**: When the bot finds an account with a balance greater than $10,000, it sends out a tweet with the account's EVM address and USD balance.
- **Randomized Tweets**: The bot uses a variety of tweet templates to keep the alerts interesting and engaging.

## Techniques and Skills
- **API Integration**: The bot integrates with the Hedera API to fetch account data and the Tweepy API to send tweets.
- **Data Parsing**: The bot parses JSON data returned from the Hedera API.
- **Error Handling**: The bot includes error handling for failed JSON parsing.
- **Rate Limiting**: The bot includes a sleep function to prevent rate limiting from the Hedera API.
- **Environment Variables**: The bot uses environment variables to securely store API keys.

## How to Use
1. Ensure that Python 3 is installed on your machine.
2. Clone the repository:
   ```
   git clone https://github.com/Zayaan-Siddiqui/Hedera-Habibis.git
   ```
3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
4. Plug in your API keys in .env file.
5. Run the bot:
   ```
   python -u Hedera.py
   ```

## Twitter
Follow the bot on Twitter: @HederaHabibi
```
