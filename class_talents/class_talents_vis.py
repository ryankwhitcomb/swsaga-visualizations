import networkx as nx
import pandas as pd

"""

Usage:

Once class talents have been scraped via running scrape_talents.py, the resulting CSV can be used in this script
to generate graphs dumping into the ./class_talents/ dir. 

References:

https://stackoverflow.com/questions/12680754/split-explode-pandas-dataframe-string-entry-to-separate-rows
https://stackoverflow.com/questions/13517614/draw-different-color-for-nodes-in-networkx-based-on-their-node-value
https://networkx.org/documentation/stable/reference/drawing.html
https://stackoverflow.com/questions/39657395/how-to-draw-properly-networkx-graphs
https://stackoverflow.com/questions/27760956/setting-colour-of-nodes-in-pygraphviz

"""

if __name__ == "__main__":
    talents = pd.read_csv("class_talents.csv")
    CLASS_USAGE = "CLASS USAGE"

    talents[CLASS_USAGE] = talents[CLASS_USAGE].str.split(",")
    exploded = talents.explode([CLASS_USAGE])
    exploded[CLASS_USAGE] = exploded[CLASS_USAGE].str.strip()

    # Visualize By Class
    classes = exploded[CLASS_USAGE].unique()
    for unique_class in classes:
        class_talents = exploded.where(exploded[CLASS_USAGE] == unique_class)
        class_talents.dropna(inplace=True)
        graph = nx.convert_matrix.from_pandas_edgelist(class_talents, source="CLASS USAGE", target="TALENT TREE",
                                                       create_using=nx.DiGraph())
        agraph = nx.drawing.nx_agraph.to_agraph(graph)
        agraph.layout("dot")
        agraph.draw(f"./{unique_class.lower()}_class_talents.png")

    # Draw the Huge Tangled Mess
    graph = nx.convert_matrix.from_pandas_edgelist(exploded, source="CLASS USAGE", target="TALENT TREE",
                                                   create_using=nx.DiGraph())
    agraph = nx.drawing.nx_agraph.to_agraph(graph)
    agraph.node_attr["style"] = "filled"
    agraph.layout("fdp")
    agraph.draw(f"./all_class_talents.png")
