import requests
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer undefined",
    "cache-control": "no-cache",
    "cookie": "__zlcmid=1IzmIS4zrY8sNK3; _p2s_uvi=23e1a398.8005264232051166.1714076278278; searchHistory=[%22mouse%22%2C%22yaz%C4%B1c%C4%B1%20dolum%20seti%22%2C%22printer%20tankl%C4%B1%22%2C%22laser%20yaz%C4%B1c%C4%B1%22%2C%22huawei%20matebook%20d16%20%22]; hbus_anonymousId=f17c18a1-0b17-4e4d-b016-474130c79c2f; useinternal=true; moriaSearchHistory=[{%22type%22:%22keyword%22%2C%22value%22:%22cep%20telefonu%22%2C%22logoUrl%22:%22%22%2C%22isOfficialMerchant%22:false}]; OptanonAlertBoxClosed=2024-12-05T04:13:35.013Z; bm_sz=5457E26D6621DC65B70FCFEAA88043F5~YAAQBLOvw6rJozWTAQAAuOfKlRo00NChx7+eeIhkF29C6dxEYwpU/wllldbgQ1ZDCOwVbONCrsOeWn1j7q7fgk9iHfD18d3pWV075DBiUT7kHH6mfWuSvJkKeO9iUupHyVaVVi+58YqQrE53ha/Kiq89AlE6S02mQ9MPLf0sRAHhJ8n2NrP/hLmX+7ukacR4x1ZL9C0uupmMCpw77Bc1NUoXV1g44SPOnRy7iWH0MoanV9RmA9DXLRF0g2gLknXbsO+dsNHaQkcCJYQufSujFC4ahc1s9BdLVqWBzap8o2F6LltC0WYf63pgKM4ShYz18JMShECjdWUeGj3AO3+PfVU4h41qEFJ841cVoWqypk41kU3O9QWQYr/HBBETGbZztBXnQlrcANcfI4Yr/AvRiOJxaEWc4oXsFOhEmQQUXm5XuYPeO3otcCIy81BK5YxfIs2jILMja3zl/+fwxquzgG0Jjtz6O7ZamvVAD4M6XtU9a+j7eL2lXAQqM9db~3355961~4473156; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+05+2024+11%3A31%3A11+GMT%2B0300+(GMT%2B03%3A00)&version=6.38.0&isIABGlobal=false&hosts=&consentId=3e81b7c1-bd72-4a8b-bd93-9f2696b7635e&interactionCount=3&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=TR%3B06; hbus_sessionId=af852f60-4282-47b2-a817-89cd6b5e39d5%7C1733389319823; _abck=8A9400DEFE1DF506A1EEEA794F8F1C34~0~YAAQTbOvw6SBdI2TAQAA8xz1lQ0CVODOJTwWLcc/YSFEcLnopAJkW9wzuVVsh23jrCXCy0ZAin+eyQqyMA+O8qRQ4iyjD3V+c8+F+81zGLS3f7mxgjkwd4NIRE/3F1llPvdK6T++galHHcIBY0ZdmnEH1y1A3ny9DFislT0Gwg0NyoHpcilokIi+kwJ1XOcFwxGTotho49FBnADvonNgEuMAWkoXxCBVF7gz/WS7X1Pn8BXpwslrZz1r3yKAGYOFyuLD2+I5afT1fo07WINnm5c7awl5pYuw0bSYX9Qy+fccMSt+3cbpkcsa2VEFYEx+31k7etFqVUD3JUCj6MK9z1XFSFqmd4jhROUZ8WLJJuli36+D4Te27fUTbA9GguIMnEezDffcjq+XJHaHAaHcaiuVJOOGqx0OJZ9HG0lDkFYIfeGtxFmo261LYX4097ZhMi3vnyQPYz+j6fpos4o/7p/6bkeoAjVhWgrYXnKUtkHrxJtsI1WLZVs+OwJmNlCDE7U5xYWhlaxwfyYhjkqqpnjNLqbGeb7EuHwsco7YgJ78BcwU/D4P8WJEEOxCOQULLXKSoAhbC540LRWTavX5Lb/h/CH/FmGpCdnCyR/q7sPFjeS6lra2~-1~-1~-1",
    "origin": "https://www.hepsiburada.com",
    "referer": "https://www.hepsiburada.com/samsung-galaxy-m34-5g-6-gb-128-gb-samsung-turkiye-garantili-mavi-128-gb-mavi-p-hbcv00004wo01a-yorumlari",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}
from colorama import Fore
from time import sleep
for sayfa in range(10,12000,10):
   for yıldız in range(1,6):
     try:
            data = requests.get(headers=headers,url=f"https://user-content-gw-hermes.hepsiburada.com/queryapi/v2/ApprovedUserContents?sku=HBCV00004WO01A&from={sayfa}&size=10&includeSiblingVariantContents=true&selectedStars={yıldız}&includeSummary=true")
            data = data.json()
            data = data["data"]["approvedUserContent"]["approvedUserContentList"]
            for i in data:
                print(i["review"]["content"])
                print(Fore.LIGHTMAGENTA_EX)
                print("Yıldız sayısıs : ",yıldız)
                print(Fore.RESET)
                print("\n")
                sleep(0.5)
                print("*"*40)
     except:
            print(f"bu ürün için {i} yıldız bulunamadı")