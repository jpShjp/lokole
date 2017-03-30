from opwen_email_server.api import sendgrid_sender
from opwen_email_server.services import server_datastore
from opwen_email_server.utils.queue_consumer import QueueConsumer


class OutboundEmailQueueConsumer(QueueConsumer):
    def __init__(self):
        super().__init__(sendgrid_sender.QUEUE.dequeue)

    def _process_message(self, message: dict):
        email = server_datastore.fetch_email(message['resource_id'])
        sendgrid_sender.send(email)


if __name__ == '__main__':
    consumer = OutboundEmailQueueConsumer()
    consumer.run_forever()
