import fire
import redis
from message_processor.active_user_report import most_active_commenters
from message_processor.infra import launch_pubsub_task
from message_processor.ner_detector import model as ner_model

class MessageProcessor:
    def __init__(self, *args, **kwargs):
        self.__r = redis.Redis()

    def active_users(self, top_n=10):
        return most_active_commenters(self.__r, top_n)

    def serve_spacy_ner(self):
        launch_pubsub_task(ner_model)
    

def main():
    fire.Fire(MessageProcessor)

if __name__ == "__main__":
    main()
