from datetime import datetime, date
from gdatabase import google_db

bob = ***REMOVED***'JBU': ***REMOVED***'27-Oct-2019': ***REMOVED***'delays': 0, 'tot': 37***REMOVED***, '26-Oct-2019': ***REMOVED***'delays': 10, 'tot': 49***REMOVED***, '25-Oct-2019': ***REMOVED***'delays': 2, 'tot': 43***REMOVED***, '24-Oct-2019': ***REMOVED***'delays': 12, 'tot': 45***REMOVED***, '23-Oct-2019': ***REMOVED***'delays': 3, 'tot': 40***REMOVED***, '22-Oct-2019': ***REMOVED***'delays': 11, 'tot': 36***REMOVED***, '21-Oct-2019': ***REMOVED***'delays': 8, 'tot': 47***REMOVED***, '20-Oct-2019': ***REMOVED***'delays': 8, 'tot': 45***REMOVED***, '19-Oct-2019': ***REMOVED***'delays': 6, 'tot': 46***REMOVED***, '18-Oct-2019': ***REMOVED***'delays': 5, 'tot': 47***REMOVED***, '17-Oct-2019': ***REMOVED***'delays': 22, 'tot': 39***REMOVED***, '16-Oct-2019': ***REMOVED***'delays': 10, 'tot': 36***REMOVED***, '15-Oct-2019': ***REMOVED***'delays': 5, 'tot': 40***REMOVED***, '14-Oct-2019': ***REMOVED***'delays': 2, 'tot': 46***REMOVED***, '13-Oct-2019': ***REMOVED***'delays': 7, 'tot': 46***REMOVED***, '12-Oct-2019': ***REMOVED***'delays': 7, 'tot': 50***REMOVED***, '11-Oct-2019': ***REMOVED***'delays': 6, 'tot': 40***REMOVED***, '10-Oct-2019': ***REMOVED***'delays': 4, 'tot': 45***REMOVED***, '09-Oct-2019': ***REMOVED***'delays': 3, 'tot': 39***REMOVED***, '08-Oct-2019': ***REMOVED***'delays': 5, 'tot': 38***REMOVED***, '07-Oct-2019': ***REMOVED***'delays': 8, 'tot': 44***REMOVED***, '06-Oct-2019': ***REMOVED***'delays': 8, 'tot': 45***REMOVED***, '05-Oct-2019': ***REMOVED***'delays': 1, 'tot': 46***REMOVED***, '04-Oct-2019': ***REMOVED***'delays': 7, 'tot': 47***REMOVED***, '03-Oct-2019': ***REMOVED***'delays': 10, 'tot': 40***REMOVED***, '02-Oct-2019': ***REMOVED***'delays': 5, 'tot': 37***REMOVED***, '01-Oct-2019': ***REMOVED***'delays': 4, 'tot': 37***REMOVED***, '30-Sep-2019': ***REMOVED***'delays': 4, 'tot': 45***REMOVED***, '29-Sep-2019': ***REMOVED***'delays': 3, 'tot': 42***REMOVED***, '28-Sep-2019': ***REMOVED***'delays': 6, 'tot': 45***REMOVED***, '27-Sep-2019': ***REMOVED***'delays': 6, 'tot': 44***REMOVED***, '26-Sep-2019': ***REMOVED***'delays': 9, 'tot': 41***REMOVED***, '25-Sep-2019': ***REMOVED***'delays': 1, 'tot': 36***REMOVED***, '24-Sep-2019': ***REMOVED***'delays': 2, 'tot': 34***REMOVED***, '23-Sep-2019': ***REMOVED***'delays': 2, 'tot': 45***REMOVED***, '22-Sep-2019': ***REMOVED***'delays': 5, 'tot': 43***REMOVED***, '21-Sep-2019': ***REMOVED***'delays': 5, 'tot': 42***REMOVED***, '20-Sep-2019': ***REMOVED***'delays': 5, 'tot': 42***REMOVED***, '19-Sep-2019': ***REMOVED***'delays': 4, 'tot': 44***REMOVED***, '18-Sep-2019': ***REMOVED***'delays': 5, 'tot': 35***REMOVED***, '17-Sep-2019': ***REMOVED***'delays': 3, 'tot': 34***REMOVED***, '16-Sep-2019': ***REMOVED***'delays': 2, 'tot': 43***REMOVED***, '15-Sep-2019': ***REMOVED***'delays': 11, 'tot': 46***REMOVED***, '14-Sep-2019': ***REMOVED***'delays': 1, 'tot': 42***REMOVED***, '13-Sep-2019': ***REMOVED***'delays': 9, 'tot': 44***REMOVED***, '12-Sep-2019': ***REMOVED***'delays': 15, 'tot': 39***REMOVED***, '11-Sep-2019': ***REMOVED***'delays': 7, 'tot': 31***REMOVED***, '10-Sep-2019': ***REMOVED***'delays': 3, 'tot': 32***REMOVED***, '09-Sep-2019': ***REMOVED***'delays': 8, 'tot': 44***REMOVED***, '08-Sep-2019': ***REMOVED***'delays': 1, 'tot': 39***REMOVED***, '07-Sep-2019': ***REMOVED***'delays': 4, 'tot': 43***REMOVED***, '06-Sep-2019': ***REMOVED***'delays': 13, 'tot': 41***REMOVED***, '05-Sep-2019': ***REMOVED***'delays': 7, 'tot': 42***REMOVED***, '04-Sep-2019': ***REMOVED***'delays': 10, 'tot': 28***REMOVED***, '03-Sep-2019': ***REMOVED***'delays': 3, 'tot': 28***REMOVED***, '02-Sep-2019': ***REMOVED***'delays': 11, 'tot': 25***REMOVED***, '01-Sep-2019': ***REMOVED***'delays': 7, 'tot': 31***REMOVED***, '31-Aug-2019': ***REMOVED***'delays': 4, 'tot': 35***REMOVED***, '30-Aug-2019': ***REMOVED***'delays': 5, 'tot': 37***REMOVED***, '29-Aug-2019': ***REMOVED***'delays': 10, 'tot': 37***REMOVED***, '28-Aug-2019': ***REMOVED***'delays': 7, 'tot': 31***REMOVED***, '27-Aug-2019': ***REMOVED***'delays': 5, 'tot': 39***REMOVED***, '26-Aug-2019': ***REMOVED***'delays': 5, 'tot': 31***REMOVED***, '25-Aug-2019': ***REMOVED***'delays': 4, 'tot': 35***REMOVED***, '24-Aug-2019': ***REMOVED***'delays': 4, 'tot': 38***REMOVED***, '23-Aug-2019': ***REMOVED***'delays': 9, 'tot': 36***REMOVED***, '22-Aug-2019': ***REMOVED***'delays': 14, 'tot': 38***REMOVED***, '21-Aug-2019': ***REMOVED***'delays': 20, 'tot': 36***REMOVED***, '20-Aug-2019': ***REMOVED***'delays': 14, 'tot': 36***REMOVED***, '19-Aug-2019': ***REMOVED***'delays': 15, 'tot': 31***REMOVED***, '18-Aug-2019': ***REMOVED***'delays': 17, 'tot': 32***REMOVED***, '17-Aug-2019': ***REMOVED***'delays': 10, 'tot': 36***REMOVED***, '16-Aug-2019': ***REMOVED***'delays': 16, 'tot': 36***REMOVED***, '15-Aug-2019': ***REMOVED***'delays': 19, 'tot': 39***REMOVED***, '14-Aug-2019': ***REMOVED***'delays': 12, 'tot': 31***REMOVED***, '13-Aug-2019': ***REMOVED***'delays': 13, 'tot': 32***REMOVED***, '12-Aug-2019': ***REMOVED***'delays': 8, 'tot': 35***REMOVED***, '11-Aug-2019': ***REMOVED***'delays': 5, 'tot': 38***REMOVED***, '10-Aug-2019': ***REMOVED***'delays': 8, 'tot': 38***REMOVED***, '09-Aug-2019': ***REMOVED***'delays': 10, 'tot': 36***REMOVED***, '08-Aug-2019': ***REMOVED***'delays': 19, 'tot': 28***REMOVED******REMOVED******REMOVED***


def convert_month_to_num(month):
    month = month.upper()
    if month == 'JAN':
        return 1
    elif month == 'FEB':
        return 2
    elif month == 'MAR':
        return 3
    elif month == 'APR':
        return 4
    elif month == 'MAY':
        return 5
    elif month == 'JUN':
        return 6
    elif month == 'JUL':
        return 7
    elif month == 'AUG':
        return 8
    elif month == 'SEP':
        return 9
    elif month == 'OCT':
        return 10
    elif month == 'NOV':
        return 11
    elif month == 'DEC':
        return 12

gdb = google_db()

for airline in bob:
    for date_obj in bob[airline]:
        try:
            year = int(date_obj[-4:])
            month = int(convert_month_to_num(date_obj[3:6]))
            day = int(date_obj[0:2])
        except Exception:
            continue
        print(year, month, day)
        timestamp = datetime(year, month, day)

        new_data = bob[airline][date_obj]
        new_data['timestamp'] = timestamp
        gdb.store_data(new_data, date_obj, airline + '_delay_data')
