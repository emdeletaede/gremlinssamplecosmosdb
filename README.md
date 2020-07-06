---
page_type: sample
languages:
- python
products:
- azure-cosmosdb 
description: "This sample demonstrates a Python application that will download the graph sample of neo4J sample to use with cosmosdb  "

---
# use the neo4J sample data with azure cosmosdb 

## About this sample

> This sample demostrate how to load the CSV file in cosmosdb provide by neo4 J for sample 

### Overview

This sample demonstrates a Python application that will load a graph based on CSV samples 

1. a python loader will load 2 CSV in a graph database ( one for the edges , one for the vertex )  



## How to run this sample

To run this sample, you'll need:

> - [Python 2.7+](https://www.python.org/downloads/release/python-2713/) or [Python 3+](https://www.python.org/downloads/release/python-364/)

> - An Azure cosmosdb account 


### Step 1:  Clone or download this repository

From your shell or command line:

```Shell
git clone https://github.com/emdeletaede/gremlinssamplecosmosdb/.git
```

or download and extract the repository .zip file.

> Given that the name of the sample is quite long, you might want to clone it in a folder close to the root of your hard drive, to avoid file name length limitations when running on Windows.

### Step 2:  install the pre-requisite python library 


- You will need to install dependencies using pip as follows:
```Shell

$ Python -m pip install azure-cosmos
$ Python -m pip install gremlin_python


```

change the db name , the key and endpoint of your cosmosdb . 
### Step 3:  Run the application  

```Shell
$ python connect.py


```


in addition a word with more information will arrive in the future 


