import praw

# Minimal Reddit API example using PRAW

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    user_agent="personal_research_tool_by_u_yourusername"
)

subreddit = reddit.subreddit("entrepreneur")

for post in subreddit.hot(limit=5):
    print(post.title)
