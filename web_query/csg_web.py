from flask import Flask, render_template,request
from csg_api import csg
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


def test_func():
    return 'hello'
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        if not request.form.get('cid'):
            sbyy='没有输入长id哦'#sbyy=失败原因
            return render_template('fq.html', sbyy=sbyy)#fq=fail query
        else:
            cid = request.form.get('cid')
            # cid=test_func()
            if csg(cid):
                return render_template('sq.html', img_src='static/sg.jpg')
            else:
                result={
                    'id': '',
                    'result':'',
                    'img':'',
                    'sbyy':''
                }
                sbyy = '大概是长id不对'
                return render_template('fq.html', sbyy=sbyy)#fq=fail query



if __name__ == '__main__':
    app.run(debug=True)
