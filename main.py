import flask
import pandas as pd

app=flask.Flask(__name__)

@app.route('/')
def home():
    # 一定要放在 templates 資料夾裡
    return  flask.render_template("home.html")

@app.route('/api/v1/<station>/<date>')
def about(station,date):
    filename="data_small/TG_STAID"+str(station).zfill(6)+".txt"
    # 可先在jupyterlab 實驗
    df=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temperature=df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return  {'station':station,
             'date':date,'temperature':temperature}

if __name__ == '__main__':
    app.run(debug=True)