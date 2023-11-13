# 查身高
# 导入key，key从 应天API 获取，应天API：https://api.t1qq.com/user/register?cps=eLoJ0
from api_key import key
import requests

cid = input("请输入长id：")
url = 'https://api.t1qq.com/api/sky/sc/sczb'
params = {
    'key': key,
    'cx': cid
}
xx = '853bbe00-e581-40ac-89f3-7bab94f84566'
try:
    response = requests.get(url, params=params)
    # print(response.json())
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
try:
    sg_url = response.json()['url']
    # print(sg_url)
    response = requests.get(sg_url)
    with open(f'身高.jpg', 'wb') as file:
        file.write(response.content)
    print(f'图像已保存为身高.jpg')
except Exception as e:
    print(f"Error：出现了一些问题，大概率是因为id不正确")
