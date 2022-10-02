import requests

def parse(xml):
    for line in xml.split('\n'):
        if 'http://www.roblox.com/asset/' in line:
            return line.split('id=')[1].split('</url>')[0]

def copy(cid):
    location = requests.get(f'https://assetdelivery.roblox.com/v1/assetId/{cid}').json()['location']
    templateid = parse(requests.get(location).text)
    template = requests.get(f'https://assetdelivery.roblox.com/v1/assetId/{templateid}').json()['location']
    with open(f'{cid}.png', 'wb') as coutput:
        coutput.write(requests.get(template).content)
    print(f'saved asset as {cid}.png')

copy(input('item id: '))