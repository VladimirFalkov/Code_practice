from datetime import datetime, timedelta
import praw

from environs import Env

env = Env()
env.read_env()

reddit = praw.Reddit(
    client_id=env("CLIENT_ID"),
    client_secret=env("CLIENT_SECRET"),
    user_agent=env("USER_AGENT"),
)

posts = list(reddit.subreddit("django").top(limit=1000, time_filter="week"))
comments = list(reddit.subreddit("django").comments(limit=1000))

three_days_before = (datetime.utcnow() - timedelta(days=3)).timestamp()

posts = list(filter(lambda post: post.created_utc > three_days_before, posts))
comments = list(filter(lambda post: post.created_utc > three_days_before, comments))


post_authors = {}
for post in posts:
    post_authors[post.author.name] = post_authors.get(post.author.name, 0) + 1

top_post_authors = sorted(post_authors.items(), key=lambda x: x[1], reverse=True)
print("Top-10 post's authors for last 3 days:")
for author, count in top_post_authors[:10]:
    print(f"{author} wrote {count} posts")


comments_authors = {}
for comment in comments:
    comments_authors[comment.author.name] = comments_authors.get(comment.author.name, 0) + 1

top_comment_authors = sorted(comments_authors.items(), key=lambda x: x[1], reverse=True)
print("Top-10 comment's authors for last 3 days:")
for author, count in top_comment_authors[:10]:
    print(f"{author} wrote {count} comments")
