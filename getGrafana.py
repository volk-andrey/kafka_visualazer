import json
import requests
import time
import fake_useragent

# current_timestamp = int(time.time() * 1000)
old_timestamp = int(time.time() * 1000)
current_timestamp = old_timestamp - 3000001
# old_timestamp = current_timestamp - 300000
fake_ua = fake_useragent.UserAgent().random
payload = {"queries":[{"expr":"sum(rate(kafka_topic_partition_current_offset{topic=~\"(123|hahahaha)\", namespace=~\"\"}[1m])) by (topic)","format":"time_series","intervalFactor":1,"legendFormat":"{{topic}}","refId":"B","datasource":{"type":"prometheus","uid":"PBFA97CFB590B2093"},"exemplar":False,"requestId":"14B","utcOffsetSec":36000,"interval":"","datasourceId":1,"intervalMs":15000,"maxDataPoints":1578}],"from":f"{current_timestamp}","to":f"{old_timestamp}"}
headers = {
    'Content-Type': 'application/json',
    'User-Agent': fake_ua
}

url = "http://localhost:3000/api/ds/query?ds_type=prometheus&requestId=Q550"

requests = requests.post(url, headers=headers, json=payload)
print(requests.text)
print(current_timestamp)
print(old_timestamp)
requests_json = requests.json()
print(requests_json)
requests_dict = json.loads(requests.text)
data = requests_dict['results']['B']['frames']
for i in data:
    load = i['data']['values']
    print(load)
    o = 0
    for j in load:
        o = o + 1
        if o == 2:
            sum = 0
            i = 0
            for k in j:
                i = i + 1
                sum = sum + k
            average = sum / i
            max = sorted(j)
            print(max[len(j)-1])
            print(average)
