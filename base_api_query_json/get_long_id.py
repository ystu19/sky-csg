import re
def get_cid(original_string):
    pattern =  r'[a-z\d-]+-[a-z\d-]+'
    matches = re.findall(pattern, original_string)
    print(type(matches))
    if matches:
        print(matches[0])
        return matches[0]
    else:
        print("未找到匹配的字符串")

if __name__ == '__main__':
    get_cid('853bbe00-e581-40ac-89f3-7bab94f84566')