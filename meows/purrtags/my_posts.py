
# from meows.models import Hashtag, User, User_Post, Preference

def select_posts(hashtags, posts):
    # ordered array of (posts, score) pairs
    ordered_posts = []

    for meow in posts:
        score = 0;
        for tag in meow.hashtags.all():
            for user_tag in hashtags:
                if user_tag.hashtag_id == tag:
                    score += user_tag.scores;
                    break;
        ordered_posts.append([meow, score])

    ordered_posts.sort(key=lambda x: -x[1])

    return [x[0] for x in ordered_posts]