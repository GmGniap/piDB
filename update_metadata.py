import glob
import markdown
import os 
import json 
import urllib
import sqlite_utils
import sys 


def run():
    databases = {}
    tables = {}

    metadata = {
    "title": "piDB",
    "license": "Non-commercial",
    "about": "Personal Database",
    "source": "Credit to original owners",
    "databases" : databases
    }
    for filepath in glob.glob("./*/README.md"):
        filepath = filepath[len("./") :] # getting true file path
        topdir = filepath.split("\\")[0]

        # Render Markdown to HTML
        markdown_txt = open(os.path.join(".", filepath)).read()
        title = None 
        lines = markdown_txt.split("\n")
        if lines[0].startswith("# "):
            title = lines[0].lstrip("#").strip()
            markdown_txt = "\n".join(lines[1:]).strip()
        html = markdown.markdown(
            markdown_txt, extensions=["markdown.extensions.tables"]
        )
        html = html.replace("Data Source", "This table data is getting from ")

        for db_filepath in glob.glob("./{}/*.db".format(topdir)): # if topdir isn't added , repeated extra times
            # print(db_filepath)
            folder = db_filepath.split("\\")[0]
            # print(folder)
            db_name = db_filepath.split("\\")[1].split(".")[0]
            print("DB Name: {}".format(db_name))
            
            databases[db_name] = {
                "title": title,
                "tables": {}
                }
            
            for csv_filepath in glob.glob("{}/*.csv".format(folder)):
                #print("CSV Path: {}".format(csv_filepath))
                table_name = csv_filepath.split("\\")[1].split(".")[0]
                print("Table Name: {}".format(table_name))
                metadata["databases"][db_name]["tables"][table_name] = {
                    "description_html": html,
                }
                if title:
                    metadata["databases"][db_name]["tables"][table_name]["title"] = "{}: {}".format(
                        title, table_name
                )
    open("metadata.json", "w").write(json.dumps(metadata, indent=4))

if __name__ == "__main__":
    run()    