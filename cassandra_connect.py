import cassandra
import csv
from cassandra.cluster import Cluster
from cassandra.query import tuple_factory
from sql_queries import create_table_queries, drop_table_queries, insert_table_queries, select_table_queries, columnList

def create_keyspace():
    """This module creates the keyspace and a new session"""

    try:
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
    except Exception as e:
        print(e)

    try:
        session.execute("""CREATE KEYSPACE IF NOT EXISTS sparkify WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1}""")
    except Exception as e:
        print(e)

    # Set Keyspace and create a new session
    try:
        session.set_keyspace("sparkify")
    except Exception as e:
        print(e)
    return cluster,session

def drop_tables(session):
    """This module drop tables based on session handle received as parameters for the keyspace created"""

    for query in drop_table_queries:
        session.execute(query)

def create_tables(session):
    """This module creates tables based on session handle received as parameters for the keyspace created"""

    for query in create_table_queries:
        session.execute(query)
        
def insert_tables(session):
    """This module insert values into tables based on session handle received as parameters for the databse created"""
    
    file = 'event_datafile_new.csv'

    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            line[3] = int(line[3])
            line[8] = int(line[8])
            line[10] = int(line[10])
            i = 0
            for query in insert_table_queries:
                query = query + "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                #session.execute(query,(line[0],line[1],line[2],int(line[3]),line[4],float(line[5]),line[6],line[7],int(line[8]),line[9],int(line[10])))
                session.execute(query,(line[columnList[i][0]],line[columnList[i][1]],line[columnList[i][2]],line[columnList[i][3]],line[columnList[i][4]],line[columnList[i][5]],line[columnList[i][6]],float(line[columnList[i][7]]),line[columnList[i][8]],line[columnList[i][9]],line[columnList[i][10]]))
                i = i + 1
def select_queries(session):
    """This module fetches values from tables based on session handle received as parameters for the keyspace created"""

    for query in select_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)
        print("FETCHING RESULTS FOR QUERY " + query + "\n")
        session.row_factory = tuple_factory
        print(rows[:])
        print("\n")
        
def main():
    """This module calls appropriate modules to create keyspace, drop tables if they already exist and create the tables"""

    cluster, session = create_keyspace()

    drop_tables(session)
    create_tables(session)
    insert_tables(session)
    select_queries(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()