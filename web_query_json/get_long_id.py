import re
def get_cid(original_string):
    pattern =  r'[a-z\d-]+-[a-z\d-]+'
    matches = re.findall(pattern, original_string)
    if matches:
        for match in matches:
            print(match)
            return match
    else:
        print("未找到匹配的字符串")

