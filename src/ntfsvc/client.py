import requests


class Client:
    """
    Notification service client.
    """

    url: str
    """
    Notification service URL.
    """

    api_key: str
    """
    API key.
    """

    def __init__(self, url: str, api_key: str):
        """
        Constructs a new Client.

        :param url: Notification service URL
        :param api_key: API key
        """
        self.url = url
        self.api_key = api_key

    def send_notification(self, topic: str, message: str) -> None:
        """
        Send notification.

        :param topic: Topic
        :param message: Message
        :return: None
        """
        rsp = requests.post(self.url, json={
            'topic': topic,
            'message': message,
        }, headers={
            'X-API-Key': self.api_key,
        })
        if rsp.status_code != 200:
            raise RuntimeError('HTTP %d %s' % (rsp.status_code, rsp.reason))
