import json 

class tagManager:	
	def postCreated(self, user, text):
		self.hashTaggify(user, text, True)
	def postLiked(self, user, text):
		self.hashTaggify(user, text, True)
	def postDisliked(self, user, text):
		self.hashTaggify(user, text, false)
		
	def updateTags(self, user, tags):
		print "there\n\n\n\n\n\n\n\n\n\n"

	def hashTaggify(self, user, text, fb):
		i = 0
		hashtags = []
		while i < len(text):
			if text[i] == "#":
			    i +=  1
			    word = []
			    while i < len(text) and text[i] != " "  :
			        word.append(text[i])
			        i += 1
			    string = ''.join(word)
			    hashtags.append(str(string))

			if i < len(text):
			    i += 1
			obj = {}
			obj['user'] = str(user)
			obj['tags'] = hashtags
			json_obj = json.dumps(obj)
			self.updateTags(user, hashtags)

	