```python
@app.route('/read_csv/page/<int:page_num>')
def read_csv(page_num):
    # 目标url:http://127.0.0.1:5000/read_csv/page/1?limit=100

    # 若不指定limits默认为100
    limits = request.args.get('limits')
    if limits:
        limits = int(limits)
    else:
        limits = 20

    # 根据limits和所在页数生成数据
    def show_csv(reader, page_num, limits):
        df = []
        for row in reader:
            if page_num * limits >= reader.line_num > (page_num - 1) * limits:
                df.append(row)
        return df

    # 计算页面数
    with open(g.path, 'r+') as f:
        row_length = len(f.readlines())
        pages = int(ceil(row_length / limits))

    # 计算数据
    with open(g.path, 'r+') as f:
        reader = csv.reader(f)
        df = show_csv(reader, page_num, limits)

    return render_template('index.html', df=df, pages=pages, page_num=page_num, limits=limits)
```