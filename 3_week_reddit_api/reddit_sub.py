from datetime import datetime, timedelta
import praw
import json

credentials = "3_week_reddit_api/client_secrets.json"

with open(credentials) as f:
    creds = json.load(f)


reddit = praw.Reddit(
    client_id=creds["client_id"],
    client_secret=creds["client_secret"],
    user_agent=creds["user_agent"],
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
print("Top post's authors for last 3 days:")
for author, count in top_post_authors[:10]:
    print(f"{author} wrote {count} posts")


comments_authors = {}
for comment in comments:
    comments_authors[comment.author.name] = comments_authors.get(comment.author.name, 0) + 1

top_comment_authors = sorted(comments_authors.items(), key=lambda x: x[1], reverse=True)
print("Top comment's authors for last 3 days:")
for author, count in top_comment_authors[:10]:
    print(f"{author} wrote {count} comments")
