# StockBot-using-Rasa

### The assistant bot which help you tell the Stock Price of any stocks.


## Dependencies
- rasa(a bot framework)
- BeautifulSoup4(a web scraping tool)
- lxml(a XML and HTML parser)

To run this model create an environment.

Then, You can use these commands to install dependencies.
> pip install rasa

> pip install beautifulsoup4

> pip install lxml

Then train the model by the command

> rasa train

Run the actions.py to scrape the data from website

> rasa run actions

To chat with the bot in command line

> rasa shell

You can also integrate this bot with telegram,slack,facebook messenger and other channels.
You can refer it here https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels/
