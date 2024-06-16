import networkx as nx
import matplotlib.pyplot as plt


# 构建潜在TAP漏洞模式

def testcase_ALorRR():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="motion detected", form=[], state=False)
    DG.add_node(1, id=1, op="switch on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    #print(DG.nodes[0]["form"])
    return DG, [0]


def testcase_CE():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="switched off", form=[], state=False)
    DG.add_node(1, id=1, op="motion detected", form=[], state=False)
    DG.add_node(2, id=2, op="turn off", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'c'])
    DG.nodes[2]["form"].append([0, 'a'])
    DG.add_node(10, id=10, op="door open", form=[], state=False)
    DG.add_node(11, id=11, op="close hibernate mode", form=[], state=False)
    DG.nodes[10]["form"].append([1, 't'])
    DG.nodes[11]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(1, 2, id=0, tag=0)
    DG.add_edge(10, 11, id=1, tag=0)
    DG.add_edge(11, 1, id=1, tag=1)
    return DG, [1, 0]

def testcase_CB():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="motion detected", form=[], state=False)
    DG.add_node(1, id=1, op="switched on", form=[], state=False)
    DG.add_node(2, id=2, op="turn off", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'c'])
    DG.nodes[2]["form"].append([0, 'a'])
    DG.add_node(10, id=10, op="turn on", form=[], state=False)
    DG.add_node(11, id=1, op="turn off", form=[], state=False)
    DG.nodes[10]["form"].append([1, 't'])
    DG.nodes[11]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(1, 2, id=0, tag=0)
    DG.add_edge(10, 11, id=1, tag=0)
    DG.add_edge(11, 1, id=1, tag=-1)
    return DG, [1, 0]


def testcase_RC():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="switched on", form=[], state=False)
    DG.add_node(1, id=1, op="turn on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'a'])
    DG.nodes[0]["form"].append([1, 't'])
    DG.add_node(2, id=1, op="turn off", form=[], state=False)
    DG.nodes[2]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    # print(DG.nodes[0]["form"])
    return DG, [0, 1]


def testcase_CBp():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="switched on", form=[], state=False)
    DG.add_node(1, id=1, op="switched on", form=[], state=False)
    DG.add_node(2, id=2, op="turn on", form=[], state=False)
    DG.add_node(3, id=3, op="tem below", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'c'])
    DG.nodes[2]["form"].append([0, 'a'])
    DG.nodes[0]["form"].append([1, 't'])
    DG.nodes[3]["form"].append([1, 'c'])
    DG.nodes[2]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(1, 2, id=0, tag=0)
    DG.add_edge(0, 3, id=0, tag=0)
    DG.add_edge(3, 2, id=0, tag=0)
    # print(DG.nodes[0]["form"])
    return DG, [0, 1]


def testcase_IL():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="switched on", form=[], state=False)
    DG.add_node(1, id=1, op="switched on", form=[], state=False)
    DG.add_node(2, id=2, op="turn off", form=[], state=False)
    DG.add_node(10, id=2, op="switched off", form=[], state=False)
    # DG.add_node(11, id=1, op="switched on", form=[], state=False)
    DG.add_node(12, id=0, op="turn on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    # DG.nodes[0]["form"].append([1, 'a'])
    DG.nodes[1]["form"].append([0, 'c'])
    DG.nodes[2]["form"].append([0, 'a'])
    DG.nodes[10]["form"].append([1, 't'])
    DG.nodes[1]["form"].append([1, 'c'])
    DG.nodes[12]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(1, 2, id=0, tag=0)
    DG.add_edge(10, 1, id=0, tag=0)
    DG.add_edge(1, 12, id=0, tag=0)
    DG.add_edge(2, 10, id=0, tag=0)
    DG.add_edge(2, 10, id=0, tag=1)
    DG.add_edge(12, 0, id=0, tag=1)
    return DG, [0, 1]


def testcase_AR():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="switched on", form=[], state=False)
    DG.add_node(1, id=1, op="set high sensitivity", form=[], state=False)
    DG.add_node(2, id=1, op="motion detected", form=[], state=False)
    DG.add_node(3, id=1, op="open hibernate mode", form=[], state=False)
    # DG.add_node(11, id=1, op="switched on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    # DG.nodes[0]["form"].append([1, 'a'])
    DG.nodes[1]["form"].append([0, 'a'])
    DG.nodes[2]["form"].append([1, 't'])
    DG.nodes[3]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(2, 3, id=0, tag=0)
    DG.add_edge(1, 2, id=0, tag=1)
    DG.add_edge(3, 1, id=0, tag=-1)
    return DG, [0, 1]


def testcase_PRC():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="switched on", form=[], state=False)
    DG.add_node(1, id=1, op="turn off", form=[], state=False)
    DG.add_node(2, id=2, op="motion detected", form=[], state=False)
    DG.add_node(3, id=1, op="turn on", form=[], state=False)
    # DG.add_node(11, id=1, op="switched on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    # DG.nodes[0]["form"].append([1, 'a'])
    DG.nodes[1]["form"].append([0, 'a'])
    DG.nodes[2]["form"].append([1, 't'])
    DG.nodes[3]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(2, 3, id=0, tag=0)
    #DG.add_edge(1, 2, id=0, tag=1)
    DG.add_edge(3, 1, id=0, tag=-1)
    return DG, [0, 1]


def testcase_RP():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="switched on", form=[], state=False)
    DG.add_node(1, id=1, op="turn off", form=[], state=False)
    DG.add_node(2, id=1, op="switched on", form=[], state=False)
    DG.add_node(3, id=2, op="turn on", form=[], state=False)
    # DG.add_node(11, id=1, op="switched on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    # DG.nodes[0]["form"].append([1, 'a'])
    DG.nodes[1]["form"].append([0, 'a'])
    DG.nodes[2]["form"].append([1, 't'])
    DG.nodes[3]["form"].append([1, 'a'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(2, 3, id=0, tag=0)
    # DG.add_edge(1, 2, id=0, tag=1)
    DG.add_edge(1, 2, id=0, tag=-1)
    return DG, [0, 1]


def testcase_mPRC():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="motion detected", form=[], state=False)
    DG.add_node(1, id=1, op="turn on", form=[], state=False)
    DG.add_node(2, id=1, op="turn off", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'a'])
    DG.nodes[2]["form"].append([-1, 't'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(2, 1, id=0, tag=-1)
    return DG, [0]


def testcase_mCE():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="motion detected", form=[], state=False)
    DG.add_node(1, id=1, op="switched on", form=[], state=False)
    DG.add_node(2, id=2, op="set heat mode", form=[], state=False)
    DG.add_node(3, id=1, op="turn on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'c'])
    DG.nodes[2]["form"].append([0, 'a'])
    DG.nodes[3]["form"].append([-1, 't'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(1, 2, id=0, tag=0)
    DG.add_edge(3, 1, id=0, tag=1)
    return DG, [0]


def testcase_mCB():
    DG = nx.DiGraph()
    DG.add_node(0, id=0, op="motion detected", form=[], state=False)
    DG.add_node(1, id=1, op="switched off", form=[], state=False)
    DG.add_node(2, id=2, op="set heat mode", form=[], state=False)
    DG.add_node(3, id=1, op="turn on", form=[], state=False)
    DG.nodes[0]["form"].append([0, 't'])
    DG.nodes[1]["form"].append([0, 'c'])
    DG.nodes[2]["form"].append([0, 'a'])
    DG.nodes[3]["form"].append([-1, 't'])
    DG.add_edge(0, 1, id=0, tag=0)
    DG.add_edge(1, 2, id=0, tag=0)
    DG.add_edge(3, 1, id=0, tag=-1)
    return DG, [0]



def show(dg):
    edge_colors = []
    for u, v, d in dg.edges(data=True):
        if d['tag'] == 0:
            edge_colors.append('blue')  # 或者使用 cmap 映射到具体颜色
        elif d['tag'] == 1:
            edge_colors.append('black')
        elif d['tag'] == -1:
            edge_colors.append('red')  # 举例使用红色和蓝色

    nx.draw(dg, with_labels=True, edge_color=edge_colors, node_color='g', node_size=1000)
    plt.show()


def con_graph(bug_type):
    if bug_type == "AL" or bug_type == "RR":
        return testcase_ALorRR()
    if bug_type == "CE":
        return testcase_CE()
    if bug_type == "CB":
        return testcase_CB()
    if bug_type == "RC":
        return testcase_RC()
    if bug_type == "CBp":
        return testcase_CBp()
    if bug_type == "IL":
        return testcase_IL()
    if bug_type == "AR":
        return testcase_AR()
    if bug_type == "PRC":
        return testcase_PRC()
    if bug_type == "RP":
        return testcase_RP()
    if bug_type == "mPRC":
        return testcase_mPRC()
    if bug_type == 'mCE':
        return testcase_mCE()
    if bug_type == 'mCB':
        return testcase_mCB()


if __name__ == '__main__':
    show(testcase_mCE()[0])

    print("start server success...")
