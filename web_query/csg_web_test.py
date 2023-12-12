from flask import Flask, render_template, request
from csg_api import csg
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def test_func():
    return 'hello'


@app.route('/result', methods=['GET', 'POST'])
def result():
    current_time = time.time()
    time_struct = time.localtime(current_time)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
    result = {
        '查询时间': formatted_time
        , '查询长id': ''
        , '查询结果': '查询失败'  # 默认查询失败，查询成功的把它的值改为成功就行
        , '失败原因': '没有输入长id哦'  # 默认没有长id，长id错误改长id错误
        # , 'img': '以后放一张查询失败提示没有长id的图片'
    }
    if request.method == 'POST':
        if not request.form.get('cid'):  # 没有长id
            del result['查询长id']
            return render_template('result.html', img_src='static/no_id.png',result=result)  # fq=fail query
            # result['查询长id'] = 'cid'
            # result['查询结果'] = '查询成功'
            # del result['失败原因']
            # # del result['img']
            # # result['img']='先写着查询成功吧'
            # return render_template('result.html', img_src='static/sg.jpg', result=result)

        else:
            cid = request.form.get('cid')  # 有长id
            if csg(cid):  # 有长id查询正确
                result['查询长id']=cid
                result['查询结果']='查询成功'
                del result['失败原因']
                # del result['img']
                # result['img']='先写着查询成功吧'
                return render_template('result.html', img_src='static/sg.jpg', result=result)
            else:  # 有长id查询失败
                result['失败原因']='大概是长id不对'
                result['查询长id']=cid+'（这是不对的长id哦）'
                # result['img']='以后放一张查询失败提示重新输入的图片'
                return render_template('result.html', img_src='static/error_id.png',result=result)  # fq=fail query


if __name__ == '__main__':
    app.run(debug=True)
