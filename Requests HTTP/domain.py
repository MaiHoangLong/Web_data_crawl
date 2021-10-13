import requests
import json

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Opera GX";v="79", "Chromium";v="93"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.73',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://webrank.vn',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://webrank.vn/',
    'Accept-Language': 'en-US,en;q=0.9',
}

params = (
    ('task', 'getTopWebsiteInVietnam'),
    ('userToken', 'ZGdZVktsdE91by9qOUtndjc4MjYwTHdQeXllT3NKTS9ZUHVzdThJYTNWST06OhMNb7G48NOo6noCn1JFw0I'),
    ('draw', '1'),
    ('columns[0][data]', 'function'),
    ('columns[0][name]', ''),
    ('columns[0][searchable]', 'true'),
    ('columns[0][orderable]', 'false'),
    ('columns[0][search][value]', ''),
    ('columns[0][search][regex]', 'false'),
    ('columns[1][data]', 'function'),
    ('columns[1][name]', ''),
    ('columns[1][searchable]', 'true'),
    ('columns[1][orderable]', 'false'),
    ('columns[1][search][value]', ''),
    ('columns[1][search][regex]', 'false'),
    ('columns[2][data]', 'countryTraffic'),
    ('columns[2][name]', ''),
    ('columns[2][searchable]', 'true'),
    ('columns[2][orderable]', 'false'),
    ('columns[2][search][value]', ''),
    ('columns[2][search][regex]', 'false'),
    ('columns[3][data]', 'uniqueUser'),
    ('columns[3][name]', ''),
    ('columns[3][searchable]', 'true'),
    ('columns[3][orderable]', 'false'),
    ('columns[3][search][value]', ''),
    ('columns[3][search][regex]', 'false'),
    ('columns[4][data]', 'time_on_site'),
    ('columns[4][name]', ''),
    ('columns[4][searchable]', 'true'),
    ('columns[4][orderable]', 'false'),
    ('columns[4][search][value]', ''),
    ('columns[4][search][regex]', 'false'),
    ('columns[5][data]', 'pages'),
    ('columns[5][name]', ''),
    ('columns[5][searchable]', 'true'),
    ('columns[5][orderable]', 'false'),
    ('columns[5][search][value]', ''),
    ('columns[5][search][regex]', 'false'),
    ('columns[6][data]', 'DesktopVsMobile'),
    ('columns[6][name]', ''),
    ('columns[6][searchable]', 'true'),
    ('columns[6][orderable]', 'false'),
    ('columns[6][search][value]', ''),
    ('columns[6][search][regex]', 'false'),
    ('columns[7][data]', 'function'),
    ('columns[7][name]', ''),
    ('columns[7][searchable]', 'true'),
    ('columns[7][orderable]', 'false'),
    ('columns[7][search][value]', ''),
    ('columns[7][search][regex]', 'false'),
    ('start', '0'),
    ('length', '50'),
    ('search[value]', ''),
    ('search[regex]', 'false'),
    ('_', '1633923205704'),
)

r = requests.get('https://localapi.trazk.com/webdata/v3.php', headers=headers, params=params)
data = json.loads(r.text)
data2 = data['data'].get('data')
i = 0
# print(data2)

for key, value in data.items():
    try:
        while i < 50:
                i += 1
                writedata = data2[i]['domain']
                writecategories = data2[i]['category1']
                if writecategories == None :
                    print("None:", data)
                break
                # if writecategories=='':
                #     print('Empty:', data)

                # saveddata = open('domain.json', 'a')
                # saveddata.write(f'{writecategories} : {writedata} \n')
                # saveddata.close()
        else:
            break
    except IndexError as ie:
        pass
    continue