## SW Saga Visualizations

Quick repo to handle scraping from data from a SW Saga Wiki and perform a few quick visualizations.

### Setup

This project was created and ran on Windows 10 using Python 3.9 (64 bit).

#### PyGraphViz

PyGraphViz provides the wonderful visualization capabilities used.

https://graphviz.org/download/

Unfortunately, installing PyGraphViz on Windows can be a little painful.

I did [this](https://github.com/pypa/pipenv/issues/3119) to get it to work with PipEnv once installed.

Inside of PyCharm, running the scripts did not detect GraphViz but setting the below env vars (and then restarting
PyCharm) in the PyCharm env var configuration let it work.

```shell
LDFLAGS='-LC:\Program Files\Graphviz\lib' 
CFLAGS='-IC:\Program Files\Graphviz\include' 
pipenv install graphviz
```

You can of course change the locations to match whereever you installed GraphViz on your system.

If you run into any weird issues once you've installed GraphViz, make sure that the version of Python (i.e. 32 vs 64
bit) matches the version of GraphViz you installed.

#### Python

This project was setup in PyCharm using pipenv and Python 3.9. If you are using PyCharm, import should be quickly doable
via GUI.

If you are running via CLI, please install PipEnv and then run the following.

```shell
pipenv sync
```

### Usage

#### Talents

##### Heroic Talents

Pull the current Heroic Talents by running the below (with cwd in ./class_talents).

```shell
python scrape_talents.py
```

You can create visualizations per class and of the system as a whole by running the below.

```shell
python class_talents_vis.py
```

You should expect a raw data dump in class_talents.csv and files per class with a messy, combined graph.