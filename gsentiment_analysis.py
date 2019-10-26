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


if __name__ == '__main__':
    sa = sentiment_analysis()
    sentiment = sa.get_sentiment('i did nothing today and i feel ok')
    print(sentiment)
