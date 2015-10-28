from flask import *
import re
import datetime
import threading

app = Flask(__name__)
app.debug = True

InDate = None

def parse_date():
    matches = re.search(r"(\d+)[-. /](\d+)[-. /]?(\d+)?", InDate)
    (month, dya, year) = matches.groups()
    if not year:
        year = 2015
    ymd = (year, month, dya)
    # year = int(year)
    # month = int(month)
    # dya = int(day)
    ymd = map(lambda n: int(n), ymd) # uses c codepath
    x = datetime.date(*ymd)
    return x.strftime("%Y-%m-%d")

@app.route('/date', methods=['POST'])
def date_parser():
    #test like curl http://127.0.0.1:5000/date --data "input=10-15-2015"
    global InDate
    InDate = request.form['input']
    if not InDate:
        return None

    try:
        return parse_date()
    except:
        return ""

if __name__ == "__main__":
    app.run()