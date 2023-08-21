from requests import get, utils
import json
import time


""" response = get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings) """


#with open(file="nginx_logs.json", mode="w", encoding="utf-8") as f:
#    json.dump(content, f, ensure_ascii=False, indent=4)

#with open(file="nginx_logs.txt", mode="w", encoding="utf-8") as f:
#    f.write(content)

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


if __name__ == "__main__":
    print(nginx_logs())
