# Smart-Tool Speedtest Bot

This Telegram bot allows you to perform speed tests for your server using the Smart-Tool Speedtest API. It measures the download speed, upload speed, and ping time of your server's internet connection and provides the results in a formatted manner.

## Features

- Performs speed tests for your server's internet connection
- Displays the download speed, upload speed, and ping time
- Provides information about the internet provider

## Usage

1. Start a chat with the bot by clicking on the following link: [Smart-Tool Speedtest Bot](https://t.me/SmartBisnuBio).
2. Type `/speedtest` to initiate the speed test.
3. The bot will calculate your server's speed and display the results.

## How It Works

- The bot utilizes the `speedtest-cli` library to perform the speed test.
- It measures the download speed by downloading a file from the nearest server, the upload speed by uploading a file, and the ping time by testing the connection latency.
- The results are then displayed in a formatted manner, including the download speed, upload speed, ping time, and internet provider.

## Requirements

- Python 3.7 or higher
- `aiogram` library
- `speedtest-cli` library

## Installation

1. Clone the repository:
git clone https://github.com/bisnuray/Smart-Tool-Speedtest-Bot.git

2. Install the required dependencies:
pip install -r requirements.txt

3. Update the `bot_token` variable in the `main.py` file with your Telegram bot API token obtained from the BotFather.

4. Run the bot:
python main.py

## Author

- Name: Bisnu Ray
- Telegram: [@SmartBisnuBio](https://t.me/SmartBisnuBio)

Feel free to reach out if you have any questions or feedback.

Please note that the README assumes you have created a Telegram bot and obtained the API token from the BotFather. Additionally, it provides instructions on how to install and run the bot. You may need to update the installation and execution steps if necessary.
