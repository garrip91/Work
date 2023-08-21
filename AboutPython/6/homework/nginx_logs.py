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

