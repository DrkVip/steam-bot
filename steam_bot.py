import os
import requests
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

# Fetch Telegram Bot Token and Group Chat ID
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# Fetch Exchange Rate from USD to INR using ExchangeRate-API
def get_usd_to_inr():
    """
    Fetches the exchange rate for USD to INR from ExchangeRate-API.
    :return: The exchange rate or None if there was an error.
    """
    url = "https://v6.exchangerate-api.com/v6/e165674924e0f00b2fb916c8/latest/USD"  # Your API key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates'].get('INR', None)
    else:
        return None

# Fetch all Steam offers using CheapShark API
def fetch_all_steam_offers():
    """
    Fetches all active Steam deals from the CheapShark API.
    :return: A list of deals with game details.
    """
    url = "https://www.cheapshark.com/api/1.0/deals"
    params = {
        "storeID": "1",  # Steam Store ID
        "limit": "100",   # Limit to 100 offers (you can adjust this)
        "offset": "0",    # Offset for pagination (you can change this)
        "sortBy": "dealRating",  # Sort deals by deal rating (or other criteria like price, discount)
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Send Telegram message function (asynchronous)
async def send_telegram_message(bot_token, chat_id, message):
    """
    Sends a message to a Telegram bot.
    :param bot_token: Your Telegram bot token.
    :param chat_id: The chat ID where the message will be sent.
    :param message: The message content.
    """
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

# Function to split a message into chunks of 4096 characters or less
def split_message(message, max_length=4096):
    """
    Splits the message into chunks if it exceeds the maximum length.
    :param message: The message content.
    :param max_length: The maximum length for a message (default is 4096).
    :return: A list of message chunks.
    """
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]

# Main function (asynchronous)
async def main():
    # Fetch the exchange rate for USD to INR
    exchange_rate = get_usd_to_inr()
    
    if exchange_rate is None:
        print("Error fetching exchange rate.")
        return
    
    # Fetch all Steam offers
    offers = fetch_all_steam_offers()

    if offers:
        message = "🔥 Steam Deals Alert! 🔥\n\n"
        for offer in offers:
            # Convert price to INR
            sale_price_in_inr = float(offer['salePrice']) * exchange_rate
            normal_price_in_inr = float(offer['normalPrice']) * exchange_rate

            # Format the price in INR
            sale_price_in_inr = round(sale_price_in_inr, 2)
            normal_price_in_inr = round(normal_price_in_inr, 2)

            message += f"🎮 *{offer['title']}*\n"
            message += f"💰 Sale Price: ₹{sale_price_in_inr} (was ₹{normal_price_in_inr})\n"
            message += f"🔗 [View on Steam](https://store.steampowered.com/app/{offer['dealID']})\n\n"

        # Split the message if it exceeds the limit
        message_chunks = split_message(message)
        
        # Send each chunk to Telegram group
        for chunk in message_chunks:
            await send_telegram_message(BOT_TOKEN, CHAT_ID, chunk)
    else:
        await send_telegram_message(BOT_TOKEN, CHAT_ID, "No offers found at the moment!")

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())