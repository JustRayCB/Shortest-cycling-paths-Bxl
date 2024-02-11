"""Main module. Entry point of the application.

:Author: Rayan Contuliano Bravo
:Date: 07/02/2024
:Description: This module is the entry point of the application. It is responsible for starting the application and 
loading the main window.
"""

from analyse_path import AnalysePath
from dijkstra import Dijkstra
from graph import BuildingGraph

DATA_DIR = "data/plans/Solbosch/"
BUILDINGS = ["P1"]


def main():
    """Main function. Entry point of the application."""

    graphs = {
        building: BuildingGraph(f"{DATA_DIR}{building}/{building}.json") for building in BUILDINGS
    }
    while True:
        # ask_building = input(f"Enter a building name, available buildings are {graphs.keys()}: ")
        ask_building = "P1"
        if ask_building == "exit":
            return
        assert ask_building in graphs, f"Building {ask_building} not found."
        graph = graphs[ask_building]
        while True:
            # ask_start = input(f"Enter a start node, available nodes are {graph.nodes()}: ")
            ask_start = "H1_01"
            if ask_start == "exit":
                return
            assert ask_start in graph.nodes(), f"Node {ask_start} not found."
            while True:
                # ask_end = input(f"Enter an end node, available nodes are {graph.nodes()}: ")
                ask_end = "E214_03"
                if ask_end == "exit":
                    return
                assert ask_end in graph.nodes(), f"Node {ask_end} not found."
                d = Dijkstra(graph, ask_start, ask_end)
                our_path = d.path
                networkx_path = graph.default_dijkstra(ask_start, ask_end)
                assert our_path == networkx_path, "The paths are different."
                d.show_shortest_path()
                a = AnalysePath(graph, our_path)
                a.analyse()
                return


if __name__ == "__main__":
    main()