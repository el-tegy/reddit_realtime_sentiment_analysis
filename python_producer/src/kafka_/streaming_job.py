from client.client import get_reddit_client
from kafka_.producer import get_kafka_producer
from praw.models import Comment
def streaming(subreddit_name):
    reddit = get_reddit_client()
    producer = get_kafka_producer()
    subreddit = reddit.subreddit(subreddit_name)
    comment: Comment
    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            comment_json = {
                "id": comment.id,
                "name": comment.name,
                "author": comment.author.name,
                "body": comment.body,
                "subreddit": comment.subreddit.display_name,
                "upvotes": comment.ups,
                "downvotes": comment.downs,
                "over_18": comment.over_18,
                "timestamp": comment.created_utc,
                "permalink": comment.permalink
            }
            print(f'subreddit: {subreddit_name}, comment: {comment_json}')
            producer.send('subreddits_comments', value=comment_json)
            print(f'subreddit: {subreddit_name}, comment: {comment_json}')
        except Exception as e:
            print(f'An error occurred: {str(e)}')
