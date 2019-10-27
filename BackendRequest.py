# import webapp3
#
#
# class MainPage(webapp3.RequestHandler):
#     def get(self):
#         self.response.headers["Content-Type"] = "text/plain"
#         self.response.write("FUCKING WEBAPP")
#
#
# routes = [('/', MainPage)]
#
# my_app = webapp3.WSGIApplication(routes, debug=True)
from flask import Flask
from flask import request
import json

from gdatabase import google_db

app = Flask('Sentiment-Support-System')


gdb = google_db()

@app.route('/')
def get_thing():
    return '<form action="/search/" method="GET"><input name="search-id" type="text"><input type="submit" ' \
           'value="search"></form>'

@app.route('/search')
def do_search():
    sources = request.args.get('sources')
    sources = json.loads(sources)

    low_sentiment = request.args.get('low_sentiment', None)
    high_sentiment = request.args.get('high_sentiment', None)

    sentiment_str = request.args.get('sentiment_str', None)


    def query(x):
        if low_sentiment is not None:
            x = x.where('sentiment', '>=', low_sentiment)
        if high_sentiment is not None:
            x = x.where('sentiment', '<=', high_sentiment)
        return x

    data = gdb.get_data_from_sources(sources, query=query)

    if sentiment_str is not None:
        output = ***REMOVED******REMOVED***
        for key in data:
            for datum in data[key]:
                if sentiment_str in datum['sentiment [original]']:
                    temp = output.get(key, list())
                    temp.append(datum)
                    output[key] = temp
        return output

    return data





if __name__ == '__main__':
    app.run()