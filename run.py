# run.py
# This is the file that is invoked to start up a development server. 
# It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development.

from app import app

if __name__ == "__main__":
	import logging
	from logging.handlers import RotatingFileHandler
	FORMAT = "[%(asctime)s : %(levelname)s : %(filename)s : %(lineno)s : %(funcName)20s() ] %(message)s"
	logging.basicConfig(filename="logs.log", level=logging.DEBUG, format=FORMAT)
	# simple format  # "%(asctime)s - %(levelname)s - %(message)s")
	logger = logging.getLogger("main")
	logger.info("Main started")


	app.run(port=6060)