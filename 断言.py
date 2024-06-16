import networkx as nx
from typing import List, Any
import time


def assertion_interface(assertion_type):
    if assertion_type == "AL" or assertion_type == "RR":
        return AL_RR
    if assertion_type == "CE":
        return CE
    if assertion_type == "CB":
        return CB
    if assertion_type == "RC":
        return RC
    if assertion_type == "CBp":
        return CBp
    if assertion_type == "IL":
        return IL
    if assertion_type == "AR":
        return AR
    if assertion_type == "PRC":
        return PRC
    if assertion_type == "RP":
        return RP
    if assertion_type == "mPRC":
        return mPRC
    if assertion_type == "mCE":
        return mCE
    if assertion_type == "mCB":
        return mCB


# 断言元素E实现
def E(nid, rid, dg: nx.DiGraph):
    if nid not in dg:
        raise ValueError(f"ERROR: not exit node{nid}")
    flag = 0
    for i in dg.nodes[nid]["form"]:
        if i[0] == rid:
            # if i[1] == 'a':
            # raise ValueError("ERROR: E must input t or c node")
            # else:
            flag = 1
    if not flag:
        raise ValueError(f"ERROR: node{nid} not match rule{rid}")
    return dg.nodes[nid]["state"]


"""
#断言元素S实现
def S(nid, rid, dg: nx.DiGraph):
    if nid not in dg:
        raise ValueError(f"ERROR: not exit node{nid}")
    flag = 0
    for i in dg[nid]["form"]:
        if i[0] == rid:
            flag = 1
    if not flag:
        raise ValueError(f"ERROR: node{nid} not match rule{rid}")
    l: list[Any] = [dg[nid]["did"], dg[nid]["op"]]
    return l
"""


# 断言元素I实现
def I(nid, rid, dg: nx.DiGraph):
    if nid not in dg:
        raise ValueError(f"ERROR: not exit node{nid}")
    flag = 0
    for i in dg[nid]["form"]:
        if i[0] == rid:
            if i[1] != 'a':
                raise ValueError("ERROR: E must input t or c node")
            else:
                flag = 1
    if not flag:
        raise ValueError(f"ERROR: node{nid} not match rule{rid}")
    l: list[Any] = [dg[nid]["did"], dg[nid]["op"]]
    return l


def satisfy(nid, rid, dg: nx.DiGraph):
    checkmate = E(nid, rid, dg)
    if checkmate:
        return True
    return False


def obs(nid, rid, dg: nx.DiGraph, tag1, interval=1, stopduration=-1):
    if tag1 == 'E':
        previous_state = E(nid, rid, dg)
        if previous_state:
            raise ValueError(f"node{nid}'s initial state is True")

        print(f"Monitoring node {nid} for state changes. Initial state: {previous_state}")
        start_time = time.time()
        while True:
            if stopduration != -1:
                elapsed_time = time.time() - start_time
                if elapsed_time >= stopduration:
                    break
            time.sleep(interval)  # 等待指定的轮询间隔时间
            current_state = dg.nodes[nid].get('state')
            if current_state:
                print(f"Node {nid} state changed from '{previous_state}' to '{current_state}'")
                return True
        return False
    if tag1 == 'A':
        return


def obs_multi(nids: List, rids: List, dg: nx.DiGraph, tag1, interval=1, stopduration=-1):
    if tag1 == 'E':
        previous_states = []
        i = 0
        for i in range(len(nids)):
            previous_state = E(nids[i], rids[i], dg)
            if previous_state:
                raise ValueError(f"node{nids[i]}'s initial state is True")
            previous_states.append(previous_state)
            print(f"Monitoring node {nids[i]} for state changes. Initial state: {previous_state}")
        start_time = time.time()
        while True:
            if stopduration != -1:
                elapsed_time = time.time() - start_time
                if elapsed_time >= stopduration:
                    break
            time.sleep(interval)  # 等待指定的轮询间隔时间
            for i in range(len(nids)):
                current_state = dg.nodes[nids[i]].get('state')
                if current_state:
                    print(f"Node {nids[i]} state changed from '{previous_states[i]}' to '{current_state}'")
                    return True, nids[i], rids[i]
        return False
    if tag1 == 'A':
        return


def reset(dg):
    for node in dg.nodes():
        node["state"] = False


def AL_RR(dg, relist):
    rid = relist[0]
    t_nid, c_nid, a_nid = -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid and form[1] == 't':
                t_nid = node
            if form[0] == rid and form[1] == 'c':
                c_nid = node
            if form[0] == rid and form[1] == 'a':
                a_nid = node
    assert1_1 = obs(t_nid, rid, dg, 'E')
    assert1_2 = False
    print("check assert1")
    if c_nid == -1:
        assert1_2 = True
    else:
        # 5秒内检查条件是否满足
        times = 0
        while True:
            if times >= 10:
                # 总共执行了5秒，退出循环
                break
            result = satisfy(c_nid, rid, dg)
            if result:
                # 如果函数A返回True，输出True并退出循环
                assert1_2 = True
                break
                # 否则等待0.5秒后再试一次
            times = times + 1
            time.sleep(0.5)
    print("check assert2")
    if assert1_1 and assert1_2:
        # 180s内检查动作是否发生
        #print("step3")
        times = 0
        while True:
            #print(times)
            if times >= 360:
                raise ValueError("TAP bug: AL or RR!!!")
            result = satisfy(a_nid, rid, dg)
            if result:
                break
            times = times + 1
            time.sleep(0.5)
    return
    #reset(dg)


def CE(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    t1_nid, c1_nid, a1_nid = -1, -1, -1
    t0_nid, c0_nid, a0_nid = -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t0_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid0 and form[1] == 'a':
                a0_nid = node
            if form[0] == rid1 and form[1] == 't':
                t1_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
            if form[0] == rid1 and form[1] == 'a':
                a1_nid = node
    edge = (a0_nid, c1_nid)
    print(a0_nid, c1_nid)
    # 将规则rid0的动作执行rid1的条件
    if not dg.has_edge(*edge):
        raise ValueError(f"rule{rid0}的动作与rule{rid1}的条件之间不构成CE")
    print("begin")
    assert1_1 = obs(t0_nid, rid0, dg, 'E')
    assert1_2 = False
    print("step1")
    if c0_nid == -1:
        assert1_2 = True
    else:
        # 5秒内检查条件是否满足
        times = 0
        while True:
            if times >= 10:
                # 总共执行了5秒，退出循环
                print("条件不满足")
                break
            result = satisfy(c0_nid, rid0, dg)
            if result:
                # 如果函数A返回True，输出True并退出循环
                assert1_2 = True
                break
                # 否则等待0.5秒后再试一次
            times = times + 1
            time.sleep(0.5)
    if assert1_1 and assert1_2:
        print("step2")
        assert2_1 = satisfy(c1_nid, rid1, dg)
        assert2_2 = False
        while True:
            times = 0
            #print(times)
            if times >= 360:
                #raise ValueError("TAP bug: AL or RR!!!")
                break
            result = satisfy(a0_nid, rid0, dg)
            if result:
                assert2_2 = True
                break
            times = times + 1
            time.sleep(0.5)
        print(not assert2_1, assert2_2)
        if (not assert2_1) and assert2_2:
            print("step3")
            assert3_1 = False
            while True:
                if times >= 360:
                    # 总共执行了5秒，退出循环
                    print("条件不满足")
                    break
                assert3_1 = satisfy(c1_nid, rid1, dg)
                if assert3_1:
                    # 如果函数A返回True，输出True并退出循环
                    assert1_2 = True
                    break
                    # 否则等待0.5秒后再试一次
                times = times + 1
                time.sleep(0.5)
            print(assert3_1)
            if assert3_1:
                print("step4")
                assert4_1 = obs(t1_nid, rid1, dg, 'E', stopduration=5 * 60)
                if assert4_1:
                    raise ValueError("TAP bug: CE!!!")


def CB(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    t1_nid, c1_nid, a1_nid = -1, -1, -1
    t0_nid, c0_nid, a0_nid = -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t0_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid0 and form[1] == 'a':
                a0_nid = node
            if form[0] == rid1 and form[1] == 't':
                t1_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
            if form[0] == rid1 and form[1] == 'a':
                a1_nid = node
    edge = (a0_nid, c1_nid)
    #print(a0_nid, c1_nid)
    # 规则rid0的动作与rid1的条件对立
    if not dg.has_edge(*edge):
        raise ValueError(f"rule{rid0}的动作与rule{rid1}的条件之间不构成CB")
    print("begin")
    assert1_1 = obs(t0_nid, rid0, dg, 'E')
    assert1_2 = False
    print("step1")
    if c0_nid == -1:
        assert1_2 = True
    else:
        # 5秒内检查条件是否满足
        times = 0
        while True:
            if times >= 10:
                # 总共执行了5秒，退出循环
                print("条件超时不满足")
                break
            result = satisfy(c0_nid, rid0, dg)
            if result:
                # 如果函数A返回True，输出True并退出循环
                assert1_2 = True
                break
                # 否则等待0.5秒后再试一次
            times = times + 1
            time.sleep(0.5)
    if assert1_1 and assert1_2:
        print("step2")
        assert2_1 = satisfy(c1_nid, rid1, dg)
        assert2_2 = False
        #print(satisfy(a0_nid, rid0, dg))
        while True:
            times = 0
            #print(times)
            if times >= 360:
                #raise ValueError("TAP bug: AL or RR!!!")
                break
            result = satisfy(a0_nid, rid0, dg)
            #print(result)
            if result:
                assert2_2 = True
                break
            times = times + 1
            time.sleep(0.5)
        print(assert2_1, assert2_2)
        if assert2_1 and assert2_2:
            print("step3")
            assert3_1 = True
            while True:
                if times >= 360:
                    # 总共执行了180秒，退出循环
                    print("条件不满足")
                    break
                assert3_1 = satisfy(c1_nid, rid1, dg)
                if not assert3_1:
                    # 如果函数A返回True，输出True并退出循环
                    assert1_2 = True
                    break
                    # 否则等待0.5秒后再试一次
                times = times + 1
                time.sleep(0.5)
            print(assert3_1)
            if not assert3_1:
                print("step4")
                assert4_1 = obs(t1_nid, rid1, dg, 'E', stopduration=5 * 60)
                if assert4_1:
                    raise ValueError("TAP bug: CB!!!")


def RC(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    c0_nid, c1_nid, t_nid = -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
    assert1 = obs(t_nid, rid0, dg, 'E')
    print("check assert1")
    assert2 = False
    if c0_nid == -1 and c1_nid == -1:
        assert2 = True
    else:
        # 5秒内检查条件是否满足
        times = 0
        result0 = False
        result1 = False
        while True:
            if times >= 10:
                # 总共执行了5秒，退出循环
                break
            if c0_nid != -1:
                result0 = satisfy(c0_nid, rid0, dg)
            if c1_nid != -1:
                result1 = satisfy(c1_nid, rid1, dg)
            if result0 and result1:
                # 如果函数A返回True，输出True并退出循环
                assert2 = True
                break
                # 否则等待0.5秒后再试一次
            times = times + 1
            time.sleep(0.5)
    print("check assert2")
    if assert1 and assert2:
        raise ValueError("TAP bug: RC!!!")
    return
    # reset(dg)


def CBp(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    c0_nid, c1_nid, t_nid, a_nid = -1, -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
            if form[0] == rid0 and form[1] == 'a':
                a_nid = node
    print("step1")
    assert1 = obs(t_nid, rid0, dg, 'E')
    if c0_nid == -1 or c1_nid == -1:
        raise ValueError("TAP bug: CBp!!!")
    if assert1:
        print("step2")
        assert2 = obs(a_nid, rid0, dg, 'E', stopduration=5 * 60)
        if assert2:
            result0 = int(satisfy(c0_nid, rid0, dg))
            result1 = int(satisfy(c1_nid, rid1, dg))
            if result0 ^ result1:
                raise ValueError("TAP bug: CBp!!!")


def IL(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    c0_nid, c1_nid, t0_nid, t1_nid, a0_nid, a1_nid = -1, -1, -1, -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t0_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid0 and form[1] == 'a':
                a0_nid = node
            if form[0] == rid1 and form[1] == 't':
                t1_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
            if form[0] == rid1 and form[1] == 'a':
                a1_nid = node
    nids = [t0_nid, t1_nid]
    assert1_1, nid_be, rid_be = obs_multi(nids, relist, dg, 'E')
    print("step1")
    if assert1_1:
        # 确保循环从r0开始
        if nid_be == t1_nid:
            t0_nid, t1_nid = t1_nid, t0_nid
            c0_nid, c1_nid = c1_nid, c0_nid
            a0_nid, a1_nid = a1_nid, a0_nid
        assert1_2 = satisfy(c0_nid, rid0, dg)
        if assert1_1 and assert1_2:
            print("step2")
            assert2_1 = E(t1_nid, rid1, dg)
            assert2_2 = obs(a0_nid, rid0, dg, 'E', stopduration=5 * 60)
            #print(assert2_1, assert2_2)
            if (not assert2_1) and assert2_2:
                print("step3")
                assert3_1 = E(t1_nid, rid1, dg)
                assert3_2 = satisfy(c1_nid, rid1, dg)
                if assert3_2 and assert3_1:
                    print("step4")#, dg.nodes[a1_nid]["state"])
                    assert4 = obs(a1_nid, rid1, dg, 'E', stopduration=5 * 60)
                    if assert4:
                        print("step5")
                        assert5_1 = E(t0_nid, rid0, dg)
                        assert5_2 = E(c0_nid, rid0, dg)
                        #print(assert5_1, assert5_2)
                        if assert5_1 and assert5_2:
                            raise ValueError("TAP bugs: IL!!!")


def AR(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    c0_nid, c1_nid, t0_nid, t1_nid, a0_nid, a1_nid = -1, -1, -1, -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t0_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid0 and form[1] == 'a':
                a0_nid = node
            if form[0] == rid1 and form[1] == 't':
                t1_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
            if form[0] == rid1 and form[1] == 'a':
                a1_nid = node
    assert1_1 = obs(t0_nid, rid0,dg, 'E')
    if assert1_1:
        assert1_2 = False
        if c0_nid == -1:
            assert1_2 = True
        else:
            # 5秒内检查条件是否满足
            times = 0
            while True:
                if times >= 10:
                    # 总共执行了5秒，退出循环
                    print("条件超时不满足")
                    break
                result = satisfy(c0_nid, rid0, dg)
                if result:
                    # 如果函数A返回True，输出True并退出循环
                    assert1_2 = True
                    break
                    # 否则等待0.5秒后再试一次
                times = times + 1
                time.sleep(0.5)
        if assert1_1 and assert1_2:
            assert2_1 = E(t1_nid, rid1, dg)
            assert2_2 = obs(a0_nid, rid0, dg, 'E', stopduration=5*60)
            if (not assert2_1) and assert2_2:
                assert3_1 = E(t1_nid, rid1, dg)
                assert3_2 = False
                if c1_nid == -1:
                    assert3_2 = True
                else:
                    # 5秒内检查条件是否满足
                    times = 0
                    while True:
                        if times >= 10:
                            # 总共执行了5秒，退出循环
                            print("条件超时不满足")
                            break
                        result = satisfy(c1_nid, rid0, dg)
                        if result:
                            # 如果函数A返回True，输出True并退出循环
                            assert3_2 = True
                            break
                            # 否则等待0.5秒后再试一次
                        times = times + 1
                        time.sleep(0.5)
                if assert3_1 and assert3_2:
                    raise ValueError("TAP bugs: AR!!!")


def PRC(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    c0_nid, c1_nid, t0_nid, t1_nid, a0_nid, a1_nid = -1, -1, -1, -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t0_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid0 and form[1] == 'a':
                a0_nid = node
            if form[0] == rid1 and form[1] == 't':
                t1_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
            if form[0] == rid1 and form[1] == 'a':
                a1_nid = node
    nids = [t0_nid, t1_nid]
    assert1_1, nid_be, rid_be = obs_multi(nids, relist, dg, 'E')
    if assert1_1:
        print("step1")
        assert1_2 = False
        # 确保rid0先执行
        if nid_be == t1_nid:
            t0_nid, t1_nid = t1_nid, t0_nid
            c0_nid, c1_nid = c1_nid, c0_nid
            a0_nid, a1_nid = a1_nid, a0_nid
        if c0_nid == -1:
            assert1_2 = True
        else:
            # 5秒内检查条件是否满足
            times = 0
            while True:
                if times >= 10:
                    # 总共执行了5秒，退出循环
                    print("条件超时不满足")
                    break
                result = satisfy(c0_nid, rid0, dg)
                if result:
                    # 如果函数A返回True，输出True并退出循环
                    assert1_2 = True
                    break
                    # 否则等待0.5秒后再试一次
                times = times + 1
                time.sleep(0.5)
        if assert1_1 and assert1_2:
            print("step2")
            assert2 = obs(a0_nid, rid0, dg, 'E', stopduration=5*60)
            if assert2:
                print("step3")
                assert3_1 = obs(t1_nid, rid1, dg, 'E', stopduration=5*60)
                assert3_2 = False
                if c1_nid == -1:
                    assert3_2 = True
                else:
                    # 5秒内检查条件是否满足
                    times = 0
                    while True:
                        if times >= 10:
                            # 总共执行了5秒，退出循环
                            print("条件超时不满足")
                            break
                        result = satisfy(c1_nid, rid0, dg)
                        if result:
                            # 如果函数A返回True，输出True并退出循环
                            assert3_2 = True
                            break
                            # 否则等待0.5秒后再试一次
                        times = times + 1
                        time.sleep(0.5)

                if assert3_1 and assert3_2:
                    raise ValueError("TAP bugs: PRC")


def RP(dg, relist):
    rid0 = relist[0]
    rid1 = relist[1]
    c0_nid, c1_nid, t0_nid, t1_nid, a0_nid, a1_nid = -1, -1, -1, -1, -1, -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid0 and form[1] == 't':
                t0_nid = node
            if form[0] == rid0 and form[1] == 'c':
                c0_nid = node
            if form[0] == rid0 and form[1] == 'a':
                a0_nid = node
            if form[0] == rid1 and form[1] == 't':
                t1_nid = node
            if form[0] == rid1 and form[1] == 'c':
                c1_nid = node
            if form[0] == rid1 and form[1] == 'a':
                a1_nid = node
    nids = [t0_nid, t1_nid]
    assert1_1, nid_re, rid_re = obs_multi(nids, relist, dg, 'E')
    if nid_re == t0_nid:
        assert1_2 = False
        if c0_nid == -1:
            assert1_2 = True
        else:
            # 5秒内检查条件是否满足
            times = 0
            while True:
                if times >= 10:
                    # 总共执行了5秒，退出循环
                    print("条件超时不满足")
                    break
                result = satisfy(c0_nid, rid0, dg)
                if result:
                    # 如果函数A返回True，输出True并退出循环
                    assert1_2 = True
                    break
                    # 否则等待0.5秒后再试一次
                times = times + 1
                time.sleep(0.5)
        if assert1_1 and assert1_2:
            assert1_3 = obs(a0_nid, rid0, dg, 'E', stopduration=5*60)
            if assert1_3:
                assert2 = False
                if c0_nid == -1:
                    assert2 = True
                else:
                    # 180秒内检查条件是否满足
                    times = 0
                    while True:
                        if times >= 360:
                            # 总共执行了180秒，退出循环
                            print("条件超时不满足")
                            break
                        result = satisfy(c0_nid, rid0, dg)
                        if result:
                            # 如果函数A返回True，输出True并退出循环
                            assert2 = True
                            break
                            # 否则等待0.5秒后再试一次
                        times = times + 1
                        time.sleep(0.5)
                if assert2:
                    raise ValueError("TAP bugs: RP!!!")


def mPRC(dg, relist):
    rid = relist[0]
    t_nid, c_nid, a_nid = -1, -1, -1
    m_nid = -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid and form[1] == 't':
                t_nid = node
            if form[0] == rid and form[1] == 'c':
                c_nid = node
            if form[0] == rid and form[1] == 'a':
                a_nid = node
            if form[0] == -1:
                m_nid = node
    assert1_1 = obs(t_nid, rid, dg, 'E')
    assert1_2 = False
    if c_nid == -1:
        assert1_2 = True
    else:
        # 5秒内检查条件是否满足
        times = 0
        while True:
            if times >= 10:
                # 总共执行了5秒，退出循环
                print("条件超时不满足")
                break
            result = satisfy(c_nid, rid, dg)
            if result:
                # 如果函数A返回True，输出True并退出循环
                assert1_2 = True
                break
                # 否则等待0.5秒后再试一次
            times = times + 1
            time.sleep(0.5)
    if assert1_1 and assert1_2:
        assert1_3 = obs(a_nid, rid, dg, 'E', stopduration=5*60)
        if assert1_3:
            assert2 = obs(m_nid, -1, dg, 'E', stopduration=60)
            if assert2:
                assert3 = obs(a_nid, rid, dg, 'E', stopduration=5*60)
                if assert3:
                    raise ValueError("TAP bugs: mPRC!!!")


def mCE(dg, relist):
    rid = relist[0]
    t_nid, c_nid, a_nid = -1, -1, -1
    m_nid = -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid and form[1] == 't':
                t_nid = node
            if form[0] == rid and form[1] == 'c':
                c_nid = node
            if form[0] == rid and form[1] == 'a':
                a_nid = node
            if form[0] == -1:
                m_nid = node
    assert1_1 = E(c_nid, rid, dg)
    assert1_2 = obs(m_nid, -1, dg, 'E')
    #print(assert1_1, assert1_2)
    if (not assert1_1) and assert1_2:
        assert2_1 = E(c_nid, rid, dg)
        assert2_2 = obs(t_nid, rid, dg, 'E')
        print(assert2_1, assert2_2)
        if assert2_1 and assert2_2:
            raise ValueError("TAP bugs: mCE!!!")


def mCB(dg, relist):
    rid = relist[0]
    t_nid, c_nid, a_nid = -1, -1, -1
    m_nid = -1
    for node in dg.nodes():
        for form in dg.nodes[node]["form"]:
            if form[0] == rid and form[1] == 't':
                t_nid = node
            if form[0] == rid and form[1] == 'c':
                c_nid = node
            if form[0] == rid and form[1] == 'a':
                a_nid = node
            if form[0] == -1:
                m_nid = node
    assert1_1 = E(c_nid, rid, dg)
    assert1_2 = obs(m_nid, -1, dg, 'E')
    #print(assert1_1, assert1_2)
    if assert1_1 and assert1_2:
        assert2_1 = E(c_nid, rid, dg)
        assert2_2 = obs(t_nid, rid, dg, 'E')
        #print(assert2_1, assert2_2)
        if (not assert2_1) and assert2_2:
            raise ValueError("TAP bugs: mCE!!!")






