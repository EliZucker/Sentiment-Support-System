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
from flask import Flask, render_template
from flask import request
import json

from gdatabase import google_db

app = Flask('Sentiment-Support-System')


gdb = google_db()

@app.route('/')
def get_thing():
    # return '<form action="/search/" method="GET"><input name="search-id" type="text"><input type="submit" ' \
    #        'value="search"></form>'
    return render_template('index.html')

# @app.route('/')
# def root():
#     return app.send_static_file('index.html')

@app.route('/search')
def do_search():
    print(request.args)
    sources = request.args.get('sources')
    print(request.args)
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

    # data = gdb.get_data_from_sources(sources, query=query)
    one = ***REMOVED***'sentiment': -0.5, 'sentiment [original]': 'fuck12', 'timestamp': 5***REMOVED***
    two = ***REMOVED***'sentiment': -0.5, 'sentiment [original]': 'finkelcjsmm', 'timestamp': 7***REMOVED***
    example = [one, two]
    return render_template('display_results.html', tweets=example)

    # if sentiment_str is not None:
    #     output = ***REMOVED******REMOVED***
    #     for key in data:
    #         for datum in data[key]:
    #             if sentiment_str in datum['sentiment [original]']:
    #                 temp = output.get(key, list())
    #                 temp.append(datum)
    #                 output[key] = temp
    #         # return render_template('display_results.html', tweets=data[key])
    #         return render_template('display_results.html', tweets=example)

    # return data





if __name__ == '__main__':
    app.run()