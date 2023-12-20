# 查身高
# 导入key，key从 应天API 获取，应天API：https://api.t1qq.com/user/register?cps=eLoJ0
from api_key import key
import requests, re


def csg(original_cid):
    pattern = r'[a-z\d-]+-[a-z\d-]+'
    matches = re.findall(pattern, original_cid)
    url = 'https://api.t1qq.com/api/sky/sc/sg'
    if matches:
        cid = matches[0]
    try:  # 可能会长id不正确引起异常
        params = {
            'key': key,
            'cx': cid
        }
        response = requests.get(url, params=params)#测试时临时注释
    except UnboundLocalError as e:
        print(f'Error: {e}')
        cid = original_cid
        response = {'code': 201, 'msg': '请上传正确格式的id值'}
        return cid, response
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

    try:
        response = response.json()#测试时临时注释
        # response = {'code': 200, 'time': '2023-12-13 17:37:23',
        #             'data': {'scale': '0.0423414456', 'height': '1.9223039720', 'currentHeight': 1.4816540851728153,
        #                      'maxHeight': 1.2485660012852238, 'minHeight': 13.248566001285223},
        #             'adorn': {'cloak': '二级白斗', 'prop': '周年庆抱枕', 'neck': '表演季项链', 'mask': '黑脸面具',
        #                       'horn': '彩虹耳机', 'hair': '雨妈发型', 'pants': '武士裤'},
        #             'action': {'voice': '水母叫声', 'attitude': '初始站姿'}}
        return cid, response

    except Exception as e:
        print(f"Error：出现了一些问题，大概率是因为id不正确{e}")


if __name__ == '__main__':
    print(csg('93'))
