class User:
	userId = ""
	firstActiveTs = ""
	firstName = ""
	lastName = ""
	profilePicLink = ""
	locale = ""
	timezone = ""
	gender = ""
	isPaymentEnabled = ""
	markedSpam = ""
	hasBlocked = ""

	def __init__(self, user_id, first_active_ts, first_name, last_name, profile_pic_link, locale, timezone, gender, is_payment_enabled, marked_spam, has_blocked):
		self.userId = user_id
		self.firstActiveTs = first_active_ts
		self.firstName = first_name
		self.lastName = last_name
		self.profilePicLink = profile_pic_link
		self.locale = locale
		self.timezone = timezone
		self.gender = gender
		self.isPaymentEnabled = is_payment_enabled
		self.markedSpam = marked_spam
		self.hasBlocked = has_blocked