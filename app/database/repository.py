import logging

class Repository():
	"""docstring for Repository"""
	def __init__(self):
		self.log = logging.getLogger(self.__class__.__name__)
		self.log.info("init repository")

	def load_repository(self):
		self.log.info("started load repository")
		data_repository = [
    {
        "id": 1,
        "name": u"tag1",
                "value": 492.2,
                u"quality": "good"

    },
    {
        "id": 2,
        "name": u"tag2",
                "value": 692.2,
                u"quality": "good"
    }
	]
		return data_repository
		
		