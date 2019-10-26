from util import setup_credentials

from google.cloud import language_v1
from google.cloud.language_v1 import enums


class sentiment_analysis:
    def __init__(self):
        setup_credentials()
        self.client = language_v1.LanguageServiceClient()

    def get_sentiment(self, data: str):
        """
        Runs the data through sentiment analysis

        :param data: A string to process
        :return: A number between -1 and 1 representing sentiment (1 is very positive and -1 is quite negative)
        """
        type_ = enums.Document.Type.PLAIN_TEXT
        document = ***REMOVED***"content": data, "type": type_***REMOVED***

        response = self.client.analyze_sentiment(document, encoding_type=enums.EncodingType.UTF8)
        return response.document_sentiment.score

    def get_bulk_sentiment(self, data: list):
        """
        Gets sentiments for a list of strings

        :param data: A list of strings to process
        :return: An iterator where the ith element in the map represents the sentiment of the ith element in data
        """
        return map(self.get_sentiment, data)


