from flask import Flask, render_template
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

def calculate_time_difference(start_date):
    now = datetime.now()
    diff = relativedelta(now, start_date)

    return {
        'months': diff.months + diff.years * 12,
        'days': diff.days,
        'hours': now.hour - start_date.hour,
        'minutes': now.minute - start_date.minute,
        'seconds': now.second - start_date.second
    }

@app.route('/')
def index():
    start_date = datetime(2024, 6, 19, 12, 20)
    time_diff = calculate_time_difference(start_date)
    return render_template('index.html', time_diff=time_diff)

if __name__ == '__main__':
    app.run(debug=True)
