from gremlin_python.driver import client, serializer
import sys
import traceback
import csv


def readload_graph():
    with open('nodes_companies.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile,delimiter=';', quoting=csv.QUOTE_NONE)
     for row in reader:
        print(row['companyId'], row['name'])
        str1 = "g.addV('company').property('id', '"
        str2 =  "' ).property('name','"
        str3 = "')"
        query = str1 + row['companyId'] + str2 + row['name'] + str3
        print (query)
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tInserted this vertex:\n\t{0}\n".format(
                callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(query))



def loadverti_graph():
    with open('edges_director_duration.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile,delimiter=';', quoting=csv.QUOTE_NONE)
     for row in reader:
        print(row['START_ID'], row['years_served'], row['END_ID'])
        str1 = "g.V('"
        str2 =  "').addE('"
        str3 =  "').to(g.V('"
        str4 = "')) "
        query = str1 + row['START_ID'] + str2 + row['years_served'] + str3 + row['END_ID'] + str4  
        print (query)
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tInserted this vertex:\n\t{0}\n".format(
                callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(query))


_gremlin_cleanup_graph = "g.V().drop()"

_gremlin_count_vertices = "g.V().count()"


}


def cleanup_graph(client):
    print("\tRunning this Gremlin query:\n\t{0}".format(
        _gremlin_cleanup_graph))
    callback = client.submitAsync(_gremlin_cleanup_graph)
    if callback.result() is not None:
        print("\tCleaned up the graph!")
    print("\n")


def count_vertices(client):
    print("\tRunning this Gremlin query:\n\t{0}".format(
        _gremlin_count_vertices))
    callback = client.submitAsync(_gremlin_count_vertices)
    if callback.result() is not None:
        print("\tCount of vertices: {0}".format(callback.result().one()))
    else:
        print("Something went wrong with this query: {0}".format(
            _gremlin_count_vertices))
    print("\n")



    for key in _gremlin_traversals:
        print("\t{0}:".format(key))
        print("\tRunning this Gremlin query:\n\t{0}\n".format(
            _gremlin_traversals[key]))
        callback = client.submitAsync(_gremlin_traversals[key])
        for result in callback.result():
            print("\t{0}".format(str(result)))
        print("\n")


def execute_drop_operations(client):
    for key in _gremlin_drop_operations:
        print("\t{0}:".format(key))
        print("\tRunning this Gremlin query:\n\t{0}".format(
            _gremlin_drop_operations[key]))
        callback = client.submitAsync(_gremlin_drop_operations[key])
        for result in callback.result():
            print(result)
        print("\n")


try:
    client = client.Client('wss://xxxxx.gremlin.cosmosdb.azure.com:443/', 'g',
                           username="/dbs/xxxx/colls/yyy",
                           password="mykeyxxxxxx",
                           message_serializer=serializer.GraphSONMessageSerializer()
                           )

    print("Welcome to Azure Cosmos DB + Gremlin on Python loading neo4 J information!")


    execute_drop_operations(client)


    # Drop the entire Graph
    input("We're about to drop whatever graph is on the server. Press any key to continue...")
    cleanup_graph(client)
    
    input("Let's insert some vertices into the graph. Press any key to continue...")
    readload_graph()


    # Insert all vertices
    input("Let's insert some vertices into the graph. Press any key to continue...")
    loadverti_graph()
  

except Exception as e:
    print('There was an exception: {0}'.format(e))
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)

print("\nAnd that's all! Sample load")
input("Press Enter to continue...")
