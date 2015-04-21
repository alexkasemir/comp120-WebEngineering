
import json 
from meows.models import Hashtag, User, User_Post, Preference


class tagManager:
    def postCreated(self, user, post):
        hashtags = self.hashTaggify(post.text_content)
        for hashtag in hashtags:
            try:
                tag = Hashtag.objects.get(content=hashtag)
                tag.count += 1
                tag.save()
            except Hashtag.DoesNotExist:
                tag = Hashtag(content=hashtag, count=1)
                tag.save()
            post.hashtags.add(tag)
            self.postLiked(user, post)

    def postLiked(self, user, post):
        print "liked"
        hashtags = self.hashTaggify(post.text_content)
        print "did hashtaggify"
        if hashtags:
            print "in if statement"
            for hashtag in hashtags:
                print "in for loop"
                tag = Hashtag.objects.get(content=hashtag)
                beenLiked = Preference.objects.filter(user_id=user, hashtag_id=tag)
                print beenLiked
                if beenLiked:
                    print "in here"
                    print beenLiked[0].score
                    beenLiked[0].score += 1
                    beenLiked[0].save()
                    print "score: "
                    print beenLiked[0].score
                else:
                    preference = Preference(user_id=user, hashtag_id=tag, score=1)
                    print preference.score
                    preference.save()

    def postDisliked(self, user, post):
        hashtags = self.hashTaggify(post.text_content)
        for hashtag in hashtags:
            tag = Hashtag.objects.get(content=hashtag)
            beenLiked = Preference.objects.filter(user_id=user, hashtag_id=tag)
            if beenLiked:
                beenLiked.score -= 1
                beenLiked.save()
            else:
                preference = Preference(user_id=user, hashtag_id=tag, score=-1)
                preference.save()
		
	def updateTags(self, user, tags):
		print "there\n\n\n\n\n\n\n\n\n\n"

    def hashTaggify(self, text):
        i = 0
        hashtags = []
        while i < len(text):
            if text[i] == "#":
                i += 1
                word = []
                while i < len(text) and text[i] != " ":
                    word.append(text[i])
                    i += 1
                string = ''.join(word)
                hashtags.append(str(string))
            if i < len(text):
                i += 1
        print "here"
        return hashtags
