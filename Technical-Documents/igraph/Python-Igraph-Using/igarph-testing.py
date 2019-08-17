import igraph as ig

def test():
    print("igraph的版本信息为：", ig.__version__)
    g = ig.Graph()
    print(g)
    g.add_vertices(30)
    g.add_edges([(0,1), (1,2)])
    g.add_edges([(2,3),(3,4),(4,5),(5,3), (3,5)])
    print(g.community_infomap())   #调用infomap算法
    print(g)



if __name__ == "__main__":
    test()
