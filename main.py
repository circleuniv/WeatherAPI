import flask

app=flask.Flask(__name__)

@app.route('/')
def home():
    # 一定要放在 templates 資料夾裡
    return  flask.render_template("Home.html")

@app.route('/about')
def about():
    return  flask.render_template("About.html")

if __name__ == '__main__':
    app.run(debug=True)