from 构建潜在TAP漏洞模式 import con_graph
from 断言 import assertion_interface
import 服务器通信模块
import threading


def process_data(command, dg):
    id = int(command['id'][0])
    op = command['op'][0]
    print(id, op)
    for node in dg.nodes():
        if dg.nodes[node]["id"] == id and dg.nodes[node]["op"] == op:
            dg.nodes[node]["state"] = True
            for neighbor, attrs in dg[node].items():
                if attrs["tag"] == -1:
                    dg.nodes[neighbor]["state"] = False
                if attrs["tag"] == 1:
                    dg.nodes[neighbor]["state"] = True


def http(host, dg):
    服务器通信模块.start_server(host, dg)
    print("start server success...")


if __name__ == '__main__':
    ###
    bug_type = "mCE"
    ###
    dg, relist = con_graph(bug_type)
    check = assertion_interface(bug_type)
    thread1 = threading.Thread(target=check, args=(dg, relist))
    thread1.start()
    host = ('localhost', 8981)
    thread2 = threading.Thread(target=http, args=(host, dg))
    thread2.start()

    print("start server success...")

