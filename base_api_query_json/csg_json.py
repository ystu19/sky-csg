# 查身高
# 导入key，key从 应天API 获取，应天API：https://api.t1qq.com/user/register?cps=eLoJ0
from api_key import key
from get_long_id import get_cid
import requests

original_cid = input("请输入长id：")
cid = get_cid(original_cid)
url = 'https://api.t1qq.com/api/sky/sc/sg'
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
    response = response.json()
    query_time = response['time']
    data = response['data']
    scale = data['scale']
    height = data['height']
    currentHeight = data['currentHeight']
    maxHeight = data['maxHeight']
    minHeight = data['minHeight']
    print('查询结果：')
    print(f'体型值：{scale}')
    print(f'身高值：{height}')
    print(f'当前身高：{currentHeight:.10f}')
    print(f'最大身高：{maxHeight:.10f}')
    print(f'最小身高：{minHeight:.10f}')
    print(data)
except Exception as e:
    print(f"Error：出现了一些问题，大概率是因为id不正确")
