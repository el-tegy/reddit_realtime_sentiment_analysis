
from praw import Reddit
from utils import config

conf = config.load_config()
config.set_environment_variables(conf)

USER_AGENT = os.getenv('USER_AGENT')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def get_reddit_client():
    try:
        client = Reddit(
            user_agent=USER_AGENT,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET
        )
        return client
    except Exception as e:
        print(f'An error occurred when creating the Reddit Client: {e}')
