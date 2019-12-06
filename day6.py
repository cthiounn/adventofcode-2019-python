import networkx as nx

with open("data/my_input/day6-input.file", "r") as f:
    orbits = dict(reversed(o.strip().split(")")) for o in f.read().splitlines())

# code heavily inspired from /u/j29h and /u/Hakan_Lundvall
def part1():
    G = nx.DiGraph()
    for n in open("data/my_input/day6-input.file").readlines():
        G.add_edge(*[x.strip() for x in n.split(")")])
    print(nx.transitive_closure(G).size())
    print(nx.shortest_path_length(G.to_undirected(), "YOU", "SAN") - 2)


# code heavily inspired from /u/zedrdave
def part1Alt(orbits):
    calculate_dist_to_root = (
        lambda n: 1 + calculate_dist_to_root(orbits[n]) if n in orbits else 0
    )

    print(sum(calculate_dist_to_root(n) for n in orbits))
    prevNodes = (
        lambda n: prevNodes(orbits[n]).union([orbits[n]]) if n in orbits else set()
    )
    print(len(prevNodes("YOU") ^ prevNodes("SAN")))


part1()
part1Alt(orbits)
