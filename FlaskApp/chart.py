import os

# from flask import render_template
# from flask import Flask
from flask import Flask, request, g, render_template
import pandas as pd
import csv
from math import ceil

# 创建一个app
app = Flask(__name__)


@app.before_request
def load_csv():
    g.path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'imdb_top_1000.csv')


# 准备一个函数来处理浏览器发出来的请求
# 设置flask定时任务
@app.route('/')
def hello():
    df = pd.read_csv("imdb_top_1000.csv")
    # 数据切片
    # data = df.loc[:, 'Series_Title':'Certificate']
    data = df[['Series_Title', 'Series_Title']]
    data = data.rename(columns={"Series_Title": "value", "Certificate": "name"})
    data = data.to_dict(orient="records")
    print(data)
    return render_template("hello.html", data=data)


@app.route('/read_csv/page/<int:page_num>')
def read_csv(page_num):
    # 目标url:http://127.0.0.1:5000/read_csv/page/1?limit=100

    # 若不指定limits默认为100
    limits = request.args.get('limits')
    if limits:
        limits = int(limits)
    else:
        limits = 10

    # 根据limits和所在页数生成数据
    def show_csv(reader, page_num, limits):
        df = []
        for row in reader:
            if reader.line_num == 1:
                continue
            if page_num * limits >= (reader.line_num - 1) > (page_num - 1) * limits:
                df.append(row)
        return df

    # 计算页面数
    with open(g.path, 'r+') as f:
        row_length = len(f.readlines()) - 1
        pages = int(ceil(row_length / limits))

    # 计算数据
    with open(g.path, 'r+') as f:
        reader = csv.reader(f)
        df = show_csv(reader, page_num, limits)

    return render_template('index.html', df=df, pages=pages, page_num=page_num, limits=limits)


# 运行app
if __name__ == '__main__':
    app.run()
