import http.client, time

target = "web-server:8080"

while True:
    conn = http.client.HTTPConnection(target)
    conn.request("GET", "/ping")
    resp = conn.getresponse()
    print(resp.read().decode("utf-8"))
    time.sleep(5)