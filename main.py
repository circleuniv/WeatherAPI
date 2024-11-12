import flask

app=flask.Flask(__name__)

@app.route('/')
def home():
    # 一定要放在 templates 資料夾裡
    return  flask.render_template("home.html")

@app.route('/api/v1/<station>/<date>')
def about(station,date):
    temperature=23
    return  {'station':station,
             'date':date,'temperature':temperature}

if __name__ == '__main__':
    app.run(debug=True)