import flask
import pandas as pd

app=flask.Flask(__name__)
#variable={'data1':'您好嗎','data2':'我很好'}
stations=pd.read_csv("data_small/stations.txt",skiprows=17)
stations=stations[['STAID',
                   'STANAME                                 ']]

@app.route('/')
def home():
    # 一定要放在 templates 資料夾裡
    return  flask.render_template("home.html",data=stations.to_html())

@app.route('/api/v1/<station>/<date>')
def about(station,date):
    filename="data_small/TG_STAID"+str(station).zfill(6)+".txt"
    # 可先在jupyterlab 實驗
    df=pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temperature=df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return  {'station':station,
             'date':date,'temperature':temperature}

@app.route('/api/v1/<station>')
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result=df.to_dict(orient="records")
    return result

@app.route('/api/v1/yearly/<station>/<year>')
def yearly(station,year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"]=df["    DATE"].astype(str)
    result=df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return  result

if __name__ == '__main__':
    app.run(debug=True)