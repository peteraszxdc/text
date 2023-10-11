import requests
import csv
import io
def __download()->list[list]:
    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108'
    response=requests.request('GET',url)
    try:
        response.raise_for_status()
    except:
        raise Exception('連線錯誤','網路中斷')
    else:
        if not response.ok:
            raise Exception('下載錯誤','伺服器錯誤')
        else:
            file = io.StringIO(response.text)
            csv_reader = csv.reader(file)
            next(csv_reader)
            return list(csv_reader)
def cities_info()->list[list]:
    cities = []
    try:
        data_list=__download()
    except Exception as e:
        print(f'錯誤:{e}')
    else:
        for row in data_list:
            if row[0]=='111':
                cities.append(row)
    return cities