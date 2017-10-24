class Chatlog:
	userId = 0
	timestamp = ""
	channelId = ""
	userSessionNumber = ""
	userMessageNumber = ""
	messageType = ""
	messageChat = ""
	messageTypeFlag = ""
	visualSearch = ""
	productResponseList = ""
	nlpQueryResponse = ""
	visionFileLink = ""
	visionEngineResponse = ""

	def __init__(self, user_id, timestamp, channel_id, user_session_number, user_message_number, \
		message_type, message_chat, message_type_flag, visual_search, product_response_list, \
		nlp_query_response, vision_file_link, vision_engine_response):
		self.userId = user_id
		self.timestamp = timestamp
		self.channelId = channel_id
		self.userSessionNumber = user_session_number
		self.userMessageNumber = user_message_number
		self.messageType = message_type
		self.messageChat = message_chat
		self.messageTypeFlag = message_type_flag
		self.visualSearch = visual_search
		self.productResponseList = product_response_list
		self.nlpQueryResponse = nlp_query_response
		self.visionFileLink = vision_file_link
		self.visionEngineResponse = vision_engine_response