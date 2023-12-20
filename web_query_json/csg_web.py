import time

from flask import Flask, render_template, request
from csg_json_api import csg

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
            return render_template('result_fail.html', img_src='static/no_id.png',result=result)
        else:
            original_cid = request.form.get('cid')  # 有长id
            cid,response=csg(original_cid)
            if response['code']==200:  # 有长id查询正确
                data = response['data']
                scale = data['scale']
                height = data['height']
                currentHeight = data['currentHeight']
                maxHeight = data['maxHeight']
                minHeight = data['minHeight']
                result['查询长id']=cid
                result['查询结果']=('查询结果：'+'\n'+
                                    f'体型值：{scale}'+'\n'+
                                    f'身高值：{height}'+'\n'+
                                    f'当前身高：{currentHeight:.10f}'+'\n'+
                                    f'最大身高：{maxHeight:.10f}'+'\n'+
                                    f'最小身高：{minHeight:.10f}')
                del result['失败原因']
                return render_template('result.html', img_src='static/csg.png', result=result)
            else:  # 有长id查询失败
                result['失败原因']='大概是长id不对'
                result['查询长id']=cid+'（这是不对的长id哦）'
                return render_template('result_fail.html', img_src='static/error_id.png',result=result)  # fq=fail query


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')