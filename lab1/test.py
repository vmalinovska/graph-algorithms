from dimacs import *
from bfs import answer as answerbfs
from dfs import answer as answerdfs
from findunion import answer as answerfindunion
from dijkstra import answer as answerdijkstra
from os import listdir
from os.path import isfile, join

def test():
    mypath="/Users/yunanuna/Desktop/coding/graph-algorithms/lab1/graphs-lab1"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f!=".DS_Store"]
    for filename in onlyfiles:
        V,L=loadWeightedGraph(join(mypath, filename))
        answ=readSolution(join(mypath, filename))
        print(filename)
        print("bfs: " + str(answerbfs(V,L,1,2)))
        print("dfs: " + str(answerdfs(V,L,1,2)))
        print("find-union: " + str(answerfindunion(V,L,1,2)))
        print("dijkstra: " + str(answerdijkstra(V,L,1,2)))
        print("correct: ", answ, '\n')

test()