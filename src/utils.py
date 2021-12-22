import os
import requests
from dotenv import load_dotenv
import logging
from pathlib import Path

load_dotenv()

root_dir = Path(__file__).parent.parent
bot_version = "0.0.1"

logging.basicConfig(format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler(os.path.join(root_dir, 'logs', 'bot.log')),
                        logging.StreamHandler()])

logger = logging.getLogger(__name__)

def get_environment_variable(key: str):
	""" Get the Environment variables

	DISCORD BOT TOKEN:- https://discord.com/developers/applications/
	OPENWEATHER API KEY:- https://openweathermap.org/
	"""
	value = os.environ.get(key)
	try:
		if value is not None:
			logging.info('Loading... {}'.format(key))
			return value
	except Exception:
		logger.critical('{} is not found in environment variable.'.format(key))

token = get_environment_variable('TOKEN')

def _fetch(url: str):
	""" function to fetch data from api in asynchronous way """
	with requests.get(url) as response:
		return response.json()


logger.info('Version: {}'.format(bot_version))
