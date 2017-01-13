---
title: Programming with Python
---

# This page still under construction

[Python](https://www.python.org/) is a beginner friendly text-based programming language. In order to use Python in Algorithmics, students will have to use [NetworkX](https://networkx.github.io/), a python library for manipulating graphs, as well as [matplotlib](http://matplotlib.org/) or some other NetworkX compatible rendering library.


An installation guide to networkX can be found in it's doccumentation [here](https://networkx.github.io/documentation/development/install.html). The reccomended installation method is via pip.

A [valuable resource from Monash University](https://www.alexandriarepository.org/module/appendix-from-edgy-to-python/) (Authors : Jason Nguyen, Steven Bird) is a doccument about transitioning from Edgy to Python. While those experienced with python may find most of the content unneccesary, the appendix does cover getting your environment set up, and provides a useful helper script used to render (show) the graphs you create with networkX. In the future, this site may publish it's own tutorials on graphing with python, but for the time being, this resource is extremely helpful.

If you're just here for the helper/renderer function, and prefer to learn from the [NetworkX docs](https://networkx.readthedocs.io/en/stable/tutorial/index.html), the function is below.

~~~ python
import networkx as nx
import matplotlib.pyplot as plot
from collections import deque
try:
    from Queue import PriorityQueue
except ImportError:
    from queue import PriorityQueue

def show(G, node_attribute = "id", edge_attribute = "label"):
    layout = nx.spring_layout(G)

    for v, data in G.nodes(data = True):
        if "x" in data:
            layout[v] = [data["x"], layout[v][1]]
        if "y" in data:
            layout[v] = [layout[v][0], data["y"]]

    node_colors = [G.node[v].get("color", "white") for v in G.nodes()]
    edge_colors = [G.edge[e[0]][e[1]].get("color", "black") for e in G.edges()]
    
    node_labels = dict((v, v if node_attribute == "id" else G.node[v].get(node_attribute, v))
        for v in G.nodes())
    edge_labels = dict((e, G.edge[e[0]][e[1]].get(edge_attribute, "")) for e in G.edges())    
    
    nx.draw(G, layout, node_color = node_colors, edge_color = edge_colors)
    nx.draw_networkx_labels(G, layout, node_labels)
    nx.draw_networkx_edge_labels(G, layout, edge_labels)
    
    plot.show()
~~~




Students who are familiar with text-based languages may wish to check out [Edgy](/programming/edgy), a text-based language that is also VCAA approved.

This is one of the three languages allowed for [2017](http://www.vcaa.vic.edu.au/Pages/vce/studies/algorithmics/algorithmics-approved-lists.aspx)


