from requests import get, utils
import json
import time


def nginx_logs():
    logs_list = []
    with open(file="nginx_logs.txt", mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        counter = 1
        for line in lines:
            remote_addr = line[:line.find(" ")]
            request_type = line[line.find("]")+3:line.find("/", line.find("]"))]
            requested_resource = line[line.find("/", line.find("]")):line.find("HTTP")-1]
            logs_list.append((remote_addr, request_type, requested_resource))
            #print(counter)
            #print(line)
            #counter += 1
            #print(request_type)
            #print(requested_resource)
            #time.sleep(1)
    return logs_list


spam_detect_dict = dict()
counter = 0
for log in nginx_logs():
    if log[0] in spam_detect_dict.keys():
        counter += 1
        spam_detect_dict[log[0]] = counter
    else:
        spam_detect_dict[log[0]] = counter
max_requests_quantity = max(spam_detect_dict.values())

for log in spam_detect_dict.items():
    if log[1] == max_requests_quantity:
        print(f"Самая высокая СПАМ-активность исходит от IP-адреса: общее количество запросов: {log[0]} ({log[1]})!")
        break
