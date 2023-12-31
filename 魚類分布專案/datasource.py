import requests
import json, ssl, urllib.request
import csv


# 抓高鐵ＡＰＩ車站資訊
def Get_THSRstation():
    # API抓 參考網址 https://tdx.transportdata.tw/api-service/swagger/basic/268fc230-2e04-471b-a728-a726167c1cfc#/THSR/THSRApi_Station_2120
    url = f"https://tdx.transportdata.tw/api/basic/v2/Rail/THSR/Station?%24top=30&%24format=JSON"
    response = requests.get(url=url)
    THSRstation_list = []  # list

    if response.ok:
        print("下載成功")
        source_data = response.json()["JSON"]
        for item in source_data:
            # 建立list資料丟到county_forcase裡
            THSRstation_list.append(
                [
                    item["StationUID"],
                    item["StationID"],
                    item["StationCode"],
                    item["StationName"]["Zh_tw"],
                    item["StationName"]["En"],
                    item["StationAddress"],
                ]
            )

        return THSRstation_list

    else:
        raise Exception("下載失敗")  # 自己定義raise 拋出自定義的錯誤訊息


# 抓台北市垃圾車資訊
# 分隊、地點、局編、抵達時間、經度、緯度、行政區、路線、車次、車號、里別、離開時間
def Get_garbageStation():
    # https://quality.data.gov.tw/dq_download_csv.php?nid=136515&md5_url=4b5e05b9646c77fc75d6d64682554b77
    url = f"https://quality.data.gov.tw/dq_download_json.php?nid=136515&md5_url=4b5e05b9646c77fc75d6d64682554b77"

    # 使用SSL module把證書驗證改成不需要驗證即可
    context = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(url, context=context) as jsondata:
            # 將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
            data = json.loads(jsondata.read().decode("utf-8-sig"))
        garbagestation_list = []  # list
        for i in data:
            garbagestation_list.append(i)
        return garbagestation_list
    except:
        raise Exception("下載失敗")  # 自己定義raise 拋出自定義的錯誤訊息


# 抓台北郵遞區域
def Get_FISHTYP():
    # 寫死
    TaipeiArea = {
        "全部": "A00",
        "外來種": "A01",
        "原生種": "A02",
    }
    return TaipeiArea


def Get_FISHYEAR():
    # 寫死
    TaipeiArea = {
        "全部": "A00",
        "97": "A01",
        "98": "A02",
        "99": "A03",
        "100": "A04",
        "101": "A05",
        "102": "A06",
        "103": "A07",
        "104": "A08",
        "105": "A09",
        "106": "A10",
        "107": "A11",
        "108": "A12",
        "109": "A13",
        "110": "A14",
        "111": "A15",
        "112": "A16",
    }
    return TaipeiArea


def Get_MAP():
    # 寫死
    TaipeiArea = {
        "一般": "A00",
        "依數量": "A01",
    }
    return TaipeiArea


def Get_FISHNAME():
    # 寫死
    TaipeiArea = {
        "全部": "A00",
        "寬帶裂身鰕虎": "A01",
        "七星鱧": "A02",
        "大口湯鯉": "A03",
        "大口黑鱸": "A04",
        "大吻鰕虎": "A05",
        "大海鰱": "A06",
        "大眼海鰱": "A07",
        "大眼華鯿": "A08",
        "大棘雙邊魚": "A09",
        "大棘鑽嘴魚": "A10",
        "大彈塗魚": "A11",
        "大鱗副泥鰍": "A12",
        "大鱗梅氏鯿": "A13",
        "大鱗龜鮻": "A14",
        "大鱗鮻": "A15",
        "小皮頦鱵": "A16",
        "小盾鱧": "A17",
        "小眼雙邊魚": "A18",
        "中國小沙丁魚": "A19",
        "中華烏塘鱧": "A20",
        "中華鰍": "A21",
        "丹尼氏小䰾": "A22",
        "六帶鰺": "A23",
        "六斑二齒魨": "A24",
        "太平洋棘鯛": "A25",
        "太平洋雙色鰻鱺": "A26",
        "孔雀花鱂": "A27",
        "巴西珠母麗魚": "A28",
        "日本花鱸": "A29",
        "日本海鰶": "A30",
        "日本銀身䱛": "A31",
        "日本瓢鰭鰕虎": "A32",
        "日本鰻鱺": "A33",
        "爪哇擬鰕虎": "A34",
        "半紋小䰾": "A35",
        "半紋鋸鱗鰕虎": "A36",
        "四指馬鮁": "A37",
        "四帶小䰾": "A38",
        "四帶牙鯻": "A39",
        "四點似青鱗魚": "A40",
        "布氏非鯽": "A41",
        "布氏鯧鰺": "A42",
        "布氏鬚鰨": "A43",
        "布魯雙邊魚": "A44",
        "平頜鱲": "A45",
        "正叉舌鰕虎": "A46",
        "白帶魚": "A47",
        "仰口鰏": "A48",
        "吉打副葉鰺": "A49",
        "吉利非鯽": "A50",
        "多鱗四指馬鮁": "A51",
        "多鱗沙鮻": "A52",
        "尖吻蛇鰻": "A53",
        "尖頭曲齒鯊": "A54",
        "尖頭塘鱧": "A55",
        "尖鰭寡鱗鰕虎": "A56",
        "帆鰭花鱂": "A57",
        "曳絲鑽嘴魚": "A58",
        "朱文錦": "A59",
        "汙翅真鯊": "A60",
        "血鸚鵡": "A61",
        "似鯉黃黝魚": "A62",
        "何氏棘䰾": "A63",
        "克氏褐蛇鰻": "A64",
        "尾紋雙邊魚": "A65",
        "谷津氏絲鰕虎": "A66",
        "赤鼻稜鯷": "A67",
        "兔頭瓢鰭鰕虎": "A68",
        "刺蓋塘鱧": "A69",
        "明多羅龍口蛇鰻": "A70",
        "明潭吻鰕虎": "A71",
        "泥鰍": "A72",
        "花身副麗魚": "A73",
        "花身鯻": "A74",
        "花斑劍尾魚": "A75",
        "花錐脊塘鱧": "A76",
        "花鰻鱺": "A77",
        "虱目魚": "A78",
        "金黃叉舌鰕虎": "A79",
        "金錢魚": "A80",
        "長吻仰口鰏": "A81",
        "長吻管嘴魚": "A82",
        "長脂瘋鱨": "A83",
        "長絲𩷶": "A84",
        "長鰭馬口鱲": "A85",
        "長鰭莫鯔": "A86",
        "阿部氏鯔鰕虎": "A87",
        "青魚": "A88",
        "青鱂": "A89",
        "前鰭多環海龍": "A90",
        "前鱗龜鮻": "A91",
        "南方溝鰕虎": "A92",
        "南臺中華爬岩鰍": "A93",
        "南臺吻鰕虎": "A94",
        "厚唇雙冠麗魚": "A95",
        "屏東鬚鱲": "A96",
        "恆河鱯": "A97",
        "恆春吻鰕虎": "A98",
        "扁圓吻鯝": "A99",
        "拜庫雷鰕虎": "A100",
        "星雞魚": "A101",
        "珍珠毛足鬥魚": "A102",
        "珍珠塘鱧": "A103",
        "珍珠鮐": "A104",
        "科勒氏鰍鮀": "A105",
        "紅牙䱛": "A106",
        "紅鯽": "A107",
        "紅鰭鮊": "A108",
        "革條田中鰟鮍": "A109",
        "食蚊魚": "A110",
        "香魚": "A111",
        "唇䱻": "A112",
        "埔里中華爬岩鰍": "A113",
        "浪人鰺": "A114",
        "神仙魚": "A115",
        "粉紅副尼麗魚": "A116",
        "草魚": "A117",
        "逆鈎鰺": "A118",
        "高身小鰾鮈": "A119",
        "高身白甲魚": "A120",
        "高身鯽": "A121",
        "高屏花鰍": "A122",
        "高屏馬口鱲": "A123",
        "高體高鬚魚": "A124",
        "高體斑鮃": "A125",
        "高體鰟鮍": "A126",
        "側帶丘塘鱧": "A127",
        "勒氏笛鯛": "A128",
        "圈頸鰏": "A129",
        "條紋狹鰕虎": "A130",
        "條紋鴨嘴鯰": "A131",
        "清尾鯔鰕虎": "A132",
        "眼斑厚唇鯊": "A133",
        "眼點麗魚": "A134",
        "粗首馬口鱲": "A135",
        "細紋鰏": "A136",
        "細斑吻鰕虎": "A137",
        "莫三比克口孵非鯽": "A138",
        "陳氏鰍鮀": "A139",
        "麥奇鈎吻鮭": "A140",
        "斑海鯰": "A141",
        "斑帶吻鰕虎": "A142",
        "斑駁尖塘鱧": "A143",
        "斑點竿鰕虎": "A144",
        "斑雞魚": "A145",
        "斑鱧": "A146",
        "斯奈德小䰾": "A147",
        "棘星塘鱧": "A148",
        "無棘腹囊海龍": "A149",
        "畫眉口孵非鯽": "A150",
        "短吻小鰾鮈": "A151",
        "短吻紅斑吻鰕虎": "A152",
        "短棘鰏": "A153",
        "短臀瘋鱨": "A154",
        "短攀鱸": "A155",
        "短鑽嘴魚": "A156",
        "絲鰭毛足鬥魚": "A157",
        "菊池氏細鯽": "A158",
        "蛙副雙邊魚": "A159",
        "鈍吻叉舌鰕虎": "A160",
        "陽明山吻鰕虎": "A161",
        "韌鰕虎": "A162",
        "項斑項鰏": "A163",
        "飯島氏銀鮈": "A164",
        "黃姑魚": "A165",
        "黃頰副麗魚": "A166",
        "黃鰭棘鯛": "A167",
        "黃鰭棘鰓塘鱧": "A168",
        "黃鱔": "A169",
        "黑尾小沙丁魚": "A170",
        "黑帶嬌麗魚": "A171",
        "黑斑脊塘鱧": "A172",
        "黑棘鯛": "A173",
        "黑紫枝牙鰕虎": "A174",
        "黑邊布氏鰏": "A175",
        "黑邊湯鯉": "A176",
        "黑鰭枝牙鰕虎": "A177",
        "黑體塘鱧": "A178",
        "奧奈鑽嘴魚": "A179",
        "極樂吻鰕虎": "A180",
        "溪鱧": "A181",
        "路易氏雙髻鯊": "A182",
        "飾妝鎧弓魚": "A183",
        "圖麗魚": "A184",
        "團頭魴": "A185",
        "漢氏稜鯷": "A186",
        "綠背龜鮻": "A187",
        "網紋穗唇䰾": "A188",
        "臺江擬鰕虎": "A189",
        "臺東間爬岩鰍": "A190",
        "臺灣白甲魚": "A191",
        "臺灣石鮒": "A192",
        "臺灣石𩼧" :"A193",
        "臺灣吻鰕虎": "A194",
        "臺灣副細鯽": "A195",
        "臺灣梅氏鯿": "A196",
        "臺灣棘鯛": "A197",
        "臺灣間爬岩鰍": "A198",
        "臺灣䱀": "A199",
        "臺灣龍口蛇鰻": "A200",
        "臺灣鬚鱲": "A201",
        "蓋斑鬥魚": "A202",
        "裸頰鋸鱗鰕虎": "A203",
        "銀紋笛鯛": "A204",
        "銀高體䰾": "A205",
        "銀雞魚": "A206",
        "齊氏石鮒": "A207",
        "劍尾魚": "A208",
        "彈塗魚": "A209",
        "潔身叉舌鰕虎": "A210",
        "盤鰭叉舌鰕虎": "A211",
        "線鱧": "A212",
        "褐塘鱧": "A213",
        "橘色雙冠麗魚": "A214",
        "橘尾窄口䰾": "A215",
        "橫帶沙鱚": "A216",
        "錦鯉": "A217",
        "龍鯉": "A218",
        "曙首厚唇鯊": "A219",
        "環球海鰶": "A220",
        "縱帶黑麗魚": "A221",
        "薛氏莫鯔": "A222",
        "黏皮鯔鰕虎": "A223",
        "點帶叉舌鰕虎": "A224",
        "斷線雙邊魚": "A225",
        "翹嘴鮊": "A226",
        "雙斑伴麗魚": "A227",
        "雜交口孵非鯽": "A228",
        "雜交小䰾": "A229",
        "雜交吉利非鯽": "A230",
        "雜交非鯽": "A231",
        "雜交副尼麗魚": "A232",
        "雜交翼甲鯰": "A233",
        "鮻": "A234",
        "鯁": "A235",
        "鯉": "A236",
        "鯽": "A237",
        "䱗": "A238",
        "羅氏裸身鰕虎": "A239",
        "羅漢魚": "A240",
        "蟾鬍鯰": "A241",
        "鬍子異形": "A242",
        "鬍鯰": "A243",
        "鯔": "A244",
        "鯰": "A245",
        "蘭嶼吻鰕虎": "A246",
        "鬚鰻鰕虎": "A247",
        "鰱": "A248",
        "鱅": "A249",
        "纓口臺鰍": "A250",
    }
    return TaipeiArea


# 抓台北區域的村里
import csv


def Get_AreaVillage_from_csv(fishcode01):
    csv_filename = f"Pie_data{fishcode01}.csv"
    AreaVillage_list = []

    with open(csv_filename, "r", newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        #next(csv_reader)  # 跳過標題列
        for row in csv_reader:
            village_name = row[0]
            AreaVillage_list.append(village_name)



    return AreaVillage_list


