# Steam Deals Telegram Bot

This bot fetches the latest Steam game deals using the CheapShark API and converts prices to INR with real-time exchange rates. It then sends updates to a Telegram group, helping gamers find the best discounts.

## Features
- Fetches real-time Steam deals
- Converts prices to INR using ExchangeRate-API
- Sends deal updates to a Telegram group

## Requirements
- Python 3.8+
- Telegram Bot API Token
- CheapShark API
- ExchangeRate-API Key
- Required Python packages (listed in `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a `.env` file and add:
   ```
   BOT_TOKEN=your_telegram_bot_token
   CHAT_ID=your_telegram_chat_id
   EXCHANGE_API_KEY=your_exchange_rate_api_key
   ```

## Usage
Run the bot:
```bash
python steam_bot.py
```

## Deploying on Render
1. Push your code to GitHub.
2. Create a new Render Web Service.
3. Link your GitHub repository.
4. Set the start command to:
   ```
   python steam_bot.py
   ```
5. Set environment variables in Render's dashboard.
6. Deploy and monitor logs.

## License
This project is licensed under the MIT License.

## Contributors
- Your Name (@your-github-username)

## Support
For issues, open a GitHub issue or contact me on Telegram.

