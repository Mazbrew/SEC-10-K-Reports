import requests
import html
import json

def url_build(link,item):
    if link == None and item == None:
        base_URL = "https://api.sec-api.io?token="
        API_key = "0e6bc410e80edc5d34778ef137e4ac1764cf7366dfa0f52bec739bb4d1362b72"

        return base_URL + API_key

    elif link != None and item != None:
        base_URL = "https://api.sec-api.io/extractor?url="
        API_key = "0e6bc410e80edc5d34778ef137e4ac1764cf7366dfa0f52bec739bb4d1362b72"
        item_str = ""

        if item == 0:
            item_str = "1"
        elif item == 1:
            item_str = "1A"
        elif item == 2:
            item_str = "1B"
        elif item == 3:
            item_str = "2"
        elif item == 4:
            item_str = "3"
        elif item == 5:
            item_str = "4"
        elif item == 6:
            item_str = "5"
        elif item == 7:
            item_str = "6"
        elif item == 8:
            item_str = "7"
        elif item == 9:
            item_str = "7A"
        elif item == 10:
            item_str = "8"
        elif item == 11:
            item_str = "9"
        elif item == 12:
            item_str = "9A"
        elif item == 13:
            item_str = "9B"
        elif item == 14:
            item_str = "10"
        elif item == 15:
            item_str = "11"
        elif item == 16:
            item_str = "12"
        elif item == 17:
            item_str = "13"
        elif item == 18:
            item_str = "14"
        elif item == 19:
            item_str = "15"

        

        return base_URL + link + "&item=" + item_str + "&type=html&token=" + API_key 
    
def read_links():
    links_file = open("links.txt", "r",encoding="utf-8")
    iter = 1

    for z in range(10):
        link = links_file.readline().replace('\n', "")

        output_file = open(str(iter) + ".txt","w",encoding="utf-8")

        for i in range(20):
            print(url_build(link,i))

            if requests.get(str(url_build(link,i))).status_code == 200:
                res = requests.get(str(url_build(link,i)))
                output_file.write(html.unescape(res.text))

        if link == '':
            break

        iter+=1

        output_file.close()

        
if __name__ == "__main__":
    # make into a function to get this from another api maybe or text file
    full_URL = url_build(None,None)

    # full_URL = url_build(cik, acc_no, filename)
    req = requests.post(full_URL, json= {"query": { "query_string": { "query": "formType:\"10-K\"" } }})

    file = open("temp"+".json", "w", encoding="utf-8")
    file.write(html.unescape(req.text))
    file.close()

    file = open("temp.json","r", encoding="utf-8")
    data = json.load(file)

    links_file = open("links.txt","w",encoding="utf-8")

    for i in range(len(data["filings"])):
        links_file.write(str(data["filings"][i]["linkToFilingDetails"])+"\n")

    file.close()
    links_file.close()

    read_links()