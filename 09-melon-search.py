import time
import requests
def melon_search(query:str)->list:
    search_url = "https://www.melon.com/search/keyword/index.json"

    # Query Parameters
    params ={
        "jscallback":"_",
        "query":"idol",
        #"_":"1753756079354",  #75375607935 = time stemp
        "_":int(time.time()),
    }

    headers = {
        "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    res = requests.get(search_url, params=params,headers=headers)
    # print(res)
    # print(res.text)

    if res.status_code == 200:
        return res.json()
    return[]
