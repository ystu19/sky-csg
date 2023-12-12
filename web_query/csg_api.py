from api_key import key
import requests,os
def csg(cid):
    url = 'https://api.t1qq.com/api/sky/sc/sczb'
    params = {
        'key': key,
        'cx': cid
    }
    try:
        response = requests.get(url, params=params)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    try:
        sg_url = response.json()['url']
        response = requests.get(sg_url)
        script_folder = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join(script_folder, 'static', 'sg.jpg')
        with open(relative_path, 'wb') as file:
            file.write(response.content)
        print(f'图像已保存为“sg.jpg”')
        return 1
    except Exception as e:
        print(f"Error：出现了一些问题，大概率是因为id不正确")
        return 0