import requests
'''下載youbike資料'''
def download_youbike_data():
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    if requests.status_codes == 200:
        print("下載成功")
    else:
        raise Exception("下載失敗")




















