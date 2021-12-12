"""

Usage:

Run the script and find the output in the respective .csv file locations.

References:

https://pbpython.com/pandas-html-table.html
https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259

https://swse.fandom.com/wiki/5th-Degree_Droid_Talent_Tree
https://swse.fandom.com/wiki/4th-Degree_Droid_Talent_Tree
https://swse.fandom.com/wiki/3rd-Degree_Droid_Talent_Tree
https://swse.fandom.com/wiki/2nd-Degree_Droid_Talent_Tree
https://swse.fandom.com/wiki/1st-Degree_Droid_Talent_Tree

"""

import pandas as pd

if __name__ == "__main__":

    dump_loc_to_wiki_uri = {
        "class_talents.csv": "https://swse.fandom.com/wiki/Talents",
        # "force_talents.csv": "https://swse.fandom.com/wiki/Force_Talents", # TODO Later :)
    }


    def dump_tables(wiki_uri: str, out_location: str):
        tables = pd.read_html(wiki_uri)
        merged_tables = pd.concat(tables)
        merged_tables.to_csv(out_location, index=False)


    for (out_file_name, wiki_uri) in dump_loc_to_wiki_uri.items():
        dump_tables(wiki_uri, out_file_name)
