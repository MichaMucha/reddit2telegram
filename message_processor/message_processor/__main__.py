import fire
import redis
from message_processor.active_user_report import most_active_commenters

class MessageProcessor:
    def __init__(self, *args, **kwargs):
        self.r = redis.Redis()

    def active_users(self, top_n=10):
        return most_active_commenters(self.r, top_n)

def main():
    fire.Fire(MessageProcessor)

if __name__ == "__main__":
    main()
