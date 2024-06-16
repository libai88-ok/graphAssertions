#coding=utf-8
import http.client
import time
import random
from urllib import request, parse


def send_get(url, path, data):
    conn = http.client.HTTPConnection(url)
    conn.request("GET", path)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()
    print(data1)  #
    conn.close()


def send_post(url, path, datalist, header):
    conn = http.client.HTTPConnection(url)
    for data in datalist:
        conn.request("POST", path, data, header)
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        data1 = r1.read()
        print(data1)  #
    conn.close()


def send_head(url, path, data, header):
    conn = http.client.HTTPConnection(url)
    conn.request("HEAD", path, data, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.headers  #
    print(data1)  #
    conn.close()


def send_put(url, path, filedata, header):
    conn = http.client.HTTPConnection(url)
    conn.request("PUT", path, filedata, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()  #
    print(data1)
    conn.close()


def AL_RR():
    url = "localhost:8981"
    data = {
        'device': 'Sensor',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data).encode('utf-8')
    datalist = []
    datalist.append(datas)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    print("----------Send post test:-----------")
    send_post(url, path="/index", datalist=datalist, header=headers)


def CE():
    url = "localhost:8981"
    data1 = {
        'device': 'Door&WindowSensor',
        'id': '10',
        'MAC': 'XXXXXXXX',
        'op': 'door open'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(13)
    data2 = {
        'device': 'Camera',
        'id': '11',
        'MAC': 'XXXXXXXX',
        'op': 'close hibernate mode'
    }
    datas = parse.urlencode(data2).encode('utf-8')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(25)
    data3 = {
        'device': 'Camera',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data3).encode('utf-8')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    data4 = {
        'device': 'Light',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'switched off'
    }
    datas = parse.urlencode(data4).encode('utf-8')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    conn.close()


def CB():
    url = "localhost:8981"

    data0 = {
        'device': 'Light',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(3)
    data1 = {
        'device': 'Light',
        'id': '10',
        'MAC': 'XXXXXXXX',
        'op': 'turn on'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(13)
    data2 = {
        'device': 'Light',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn off'
    }
    datas = parse.urlencode(data2).encode('utf-8')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(25)
    data3 = {
        'device': 'Camera',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data3).encode('utf-8')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    conn.close()


def RC():
    url = "localhost:8981"
    data = {
        'device': 'Light',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data).encode('utf-8')
    datalist = []
    datalist.append(datas)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    print("----------Send post test:-----------")
    send_post(url, path="/index", datalist=datalist, header=headers)


def CBp():
    url = "localhost:8981"

    data0 = {
        'device': 'Light',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(5)
    data1 = {
        'device': 'Bulb',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(35)
    data3 = {
        'device': 'Light',
        'id': '2',
        'MAC': 'XXXXXXXX',
        'op': 'turn on'
    }
    datas = parse.urlencode(data3).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #


def IL():
    url = "localhost:8981"

    data0 = {
        'device': 'Light',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(5, 8))
    data1 = {
        'device': 'Light',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(25, 100))
    data2 = {
        'device': 'Bulb',
        'id': '2',
        'MAC': 'XXXXXXXX',
        'op': 'turn off'
    }
    datas = parse.urlencode(data2).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(25, 120))
    data3 = {
        'device': 'Light',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'turn on'
    }
    datas = parse.urlencode(data3).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #


def AR():
    url = "localhost:8981"

    data0 = {
        'device': 'Light',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data1 = {
        'device': 'Camera',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'set high sensitivity'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(125, 200))
    data2 = {
        'device': 'Camera',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data2).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data3 = {
        'device': 'Camera',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'open hibernate mode'
    }
    datas = parse.urlencode(data3).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #


def PRC():
    url = "localhost:8981"

    data0 = {
        'device': 'Light',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data1 = {
        'device': 'Bulb',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn off'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(100, 200))
    data2 = {
        'device': 'Camera',
        'id': '2',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data2).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data3 = {
        'device': 'Bulb',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn on'
    }
    datas = parse.urlencode(data3).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #


def RP():
    url = "localhost:8981"

    data0 = {
        'device': 'Light',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'switched on'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data1 = {
        'device': 'Bulb',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn off'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #


def mPRC():
    url = "localhost:8981"
    data0 = {
        'device': 'Camera',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data1 = {
        'device': 'Bulb',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn on'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(5, 40))
    data2 = {
        'device': 'Bulb',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn off'
    }
    datas = parse.urlencode(data2).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    ###
    time.sleep(random.uniform(10, 120))
    data0 = {
        'device': 'Camera',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data1 = {
        'device': 'Bulb',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn on'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #

def mCE():
    url = "localhost:8981"
    data0 = {
        'device': 'Light',
        'id': '1',
        'MAC': 'XXXXXXXX',
        'op': 'turn on'
    }
    datas = parse.urlencode(data0).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #
    time.sleep(random.uniform(10, 120))
    data1 = {
        'device': 'Sensor',
        'id': '0',
        'MAC': 'XXXXXXXX',
        'op': 'motion detected'
    }
    datas = parse.urlencode(data1).encode('utf-8')
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    path = "/index"
    header = headers
    print("----------Send post test:-----------")
    conn = http.client.HTTPConnection(url)
    conn.request("POST", path, datas, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    datare = r1.read()
    print(datare)  #


if __name__ == '__main__':
    """
    print("----------Send get test:-----------")
    send_get(url,path="/index",data="None")
    print("----------Send put test:-----------")
    tfile=open("test.txt",encoding="utf-8",mode='r')
    filedatas=tfile.read()
    print("----------Send head test:-----------")
    send_head(url, path="/index", data=datas, header=headers)
    fileheaders = {"Content-type": "text/plain", "Accept": "text/plain",\
                   "content-length":str(len(filedatas))}
    send_put(url, path="/index", filedata=filedatas, header=fileheaders)
    """
    ###
    mCE()
    ###
