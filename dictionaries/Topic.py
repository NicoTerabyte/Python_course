import random as ran
from datetime import datetime

class Topic:

	def __init__(self):
		self.valueX = ran.uniform(0, 1000.5)
		self.valueY = ran.uniform(0, 1000.5)
		self.valueZ = ran.uniform(0, 1000.5)
		self.timeOfRecording = datetime.now()


