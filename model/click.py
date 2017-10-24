class Click:
	userId = 0
	sessionNumber = ""
	messageNumber = ""
	timestamp = ""
	clickItem = ""

	def __init__(self, user_id, session_number, message_number, timestamp, click_item):
		self.userId = user_id
		self.sessionNumber = session_number
		self.messageNumber = message_number
		self.timestamp = timestamp
		self.clickItem = click_item