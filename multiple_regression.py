from pandas import DataFrame
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import statsmodels.api as sm
import gdatabase

JETBLUE_SENTIMENT_LABELS = ['jetblue_tripadvisor', 'jetblue_twitter']
OTHER_AIRLINE_SENTIMENT_LABELS = ['american airlines_twitter', 'delta airlines_twitter', 'united airlines_tripadvisor']

JETBLUE_DELAY_LABEL = ['JBU_delay_data']
JETBLUE_CANCELLATION_LABEL = ['JBU_cancellation_data']

START_DAY = datetime.now() - timedelta(days=70)
END_DAY = datetime.now()

def extract_sources_label_per_day(gdb, sources, start_day, end_day, label):
    output = []
    day = timedelta(days=1)

    start = start_day
    end = end_day
    while start <= end:
        sentiment_list_for_day = gdb.get_data_from_sources_in_range(sources, start, start + day)

        sentiment_sum = 0
        count = 0
        for i in sentiment_list_for_day:
            for result in sentiment_list_for_day[i]:
                sentiment_sum += result[label]
                count += 1

        if count == 0:
            print("UNDEFINED BEHAVIOR!!!!")
            print("No data for day ", start, ". Will put zero...")
            output.append(0)
        else:
            avg_sentiment_for_day = sentiment_sum / count
            output.append(avg_sentiment_for_day)

        start += day

    return output


if __name__ == '__main__':
    gdb = gdatabase.google_db()

    jetblue_sentiment_each_day = extract_sources_label_per_day(gdb, JETBLUE_SENTIMENT_LABELS, START_DAY, END_DAY, 'sentiment')

    #other_airline_sentiment_each_day = extract_sources_sentiment_per_day(gdb, OTHER_AIRLINE_SENTIMENT_LABELS, START_DAY, END_DAY, 'sentiment')
 
    normalized_jetblue_sentiment_per_day = []

    for i in range(len(jetblue_sentiment_each_day)):
        # Positive sentiment for jetblue and all other airlines:
        jetblue_sentiment_positive = jetblue_sentiment_each_day[i] + 1
        #all_other_sentiment_positive = other_airline_sentiment_each_day[i] + 1

        # Normalize jetblue sentiment relative to feedback for all other airlines:
        #jetblue_sentiment_normalized = jetblue_sentiment_positive / all_other_sentiment_positive
        jetblue_sentiment_normalized = jetblue_sentiment_positive / 1
        # CHANGE LINE ABOVE FOR ACTUAL NORMALIZATION

        # Add that normalized value to sentiment per day
        normalized_jetblue_sentiment_per_day.append(jetblue_sentiment_normalized)


    print ("Number of measured values: ", len(normalized_jetblue_sentiment_per_day))
    cancellations_day = extract_sources_label_per_day(gdb, JETBLUE_CANCELLATION_LABEL, START_DAY, END_DAY, 'cancelled')
    delays_day = extract_sources_label_per_day(gdb, JETBLUE_DELAY_LABEL, START_DAY, END_DAY, 'delays')
    print ("Cancellations per day: ", cancellations_day)
    print("\n\n Delays per day: ", delays_day)
    print("\n\n Jetblue Sentiment per day: ", normalized_jetblue_sentiment_per_day)
    Data = ***REMOVED***'Normalized JetBlue Sentiment (Each Day)': normalized_jetblue_sentiment_per_day,
            'Cancellations (Each Day)': cancellations_day,
            'Delays (Each Day)': delays_day,
            ***REMOVED***

    # construct dataframe with the above data
    df = DataFrame (Data, columns = ['Normalized JetBlue Sentiment (Each Day)','Cancellations (Each Day)', 'Delays (Each Day)'])
    
    ## Plot each indepentent variable (cancellations and delays) vs. dependent (normalized jetblue sentiment)

    plt.scatter(df['Cancellations (Each Day)'], df['Normalized JetBlue Sentiment (Each Day)'], color='red')
    plt.title('Cancellations vs Sentiment', fontsize=14)
    plt.xlabel('Cancellations', fontsize=14)
    plt.ylabel('Sentiment', fontsize=14)
    plt.grid(True)
    plt.show()
    plt.scatter(df['Delays (Each Day)'], df['Normalized JetBlue Sentiment (Each Day)'], color='red')
    plt.title('Delays vs Sentiment', fontsize=14)
    plt.xlabel('Delays', fontsize=14)
    plt.ylabel('Sentiment', fontsize=14)
    plt.grid(True)
    plt.show()

    X = df[['Cancellations (Each Day)','Delays (Each Day)']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets

    Y = df['Normalized JetBlue Sentiment (Each Day)']

    # with statsmodels
    X = sm.add_constant(X) # adding a constant
    
    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X) 
    
    print(model.summary())