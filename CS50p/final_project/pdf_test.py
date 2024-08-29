import requests



response = requests.get("https://raw.githubusercontent.com/lenyi/Microsoft/master/libs/msjh.ttf")
with open('msjh.ttf', 'wb') as file:
    file.write(response.content)


