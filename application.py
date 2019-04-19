#-------------------------------------------------------------------------------
# Name:        application.py ('application.py' is requied by AWS WSGI)
# Purpose:     Challenge 1
# Author:      Kuang.Lee
# Created:     18/04/2019
# Copyright:   (c) Kuang.Lee 2019
# Environment: Python37-64bit
#-------------------------------------------------------------------------------
import json

##import pyodbc
##conn = pyodbc.connect('Driver={SQL Server};'
##                      'Server=server_name;'
##                      'Database=db_name;'
##                      'Trusted_Connection=yes;')

class JsonToDictionary():

    def __init__(self, obj_in):
        obj = json.loads(obj_in)
        self.level = obj['level']
        self.x = obj['location']['x']
        self.y = obj['location']['y']
        self.size = obj['car']['size']
        self.license = obj['car']['license']
        self.color = obj['car']['color']
        self.status = obj['status']
        self.oversize = obj['oversize']

def go_update_sql_tables(record):
    """
    1. Assume this application will connec to sql server
    2. Install pyodbc package is needed
    3. Tables in SQL
        -SpatialMap (main table)
        -Level_Name (reference table)
        -Current_Status (reference table)
        -Oversize_Type (reference table)
        -Vehicle_Type (reference table)
    4. record to update example:
         {'level': '1', 'x': '1', 'y': '1', 'size': 'motorcycle',
          'license': 'USA001', 'color': 'blue', 'status': 'occupied',
          'oversize': 'N'}
    """
    ##the following steps need to be exectued in order to update the tables
    ##cursor = conn.cursor()
    ##cursor.execute('SELECT * FROM db_name.Table')
    success = False

    try:
        pass
        #. get the primary key by
            #selecting vechcile size from table Vechicle_Type where Name == 'motorcycle'

        #. get the primary key by
            #selecting oversize key from table Oversize_Type where Types == 'Fits design' becaseu oversize is N

        #. get the primary key by
            #selecting Current_Status_id from table Current_Status where Types == 'occupied'

        #. Update SpatialMap
            # current = 1 (occupied), vechile = 1 (motorcycle), Oversize = 1 (Fits design)
                # where level==1, x==1, y==1

        #conn.commit()
        success = True
    except:
        pass
        #conn.rollback()
    finally:
        pass
        #if cursor:
            #cursor.close()
            #del cursor

    return success

def main():
    """
    1. assume this will become an API using Flask in the future
    2. for this challenge 1, I made it as a program and read from a file
    3. regard reading a file as an API call from devices that scan the garage every 15 sec
    """
    with open('data9.json', 'r') as myfile:
        data = myfile.read()

    #parse file
    obj = json.loads(data)

    print("date: " + str(obj['date']))
    print("time: " + str(obj['time']))

    real_time_status = obj['condition']

    #transform json object
    try:
        for each in real_time_status:

            flat_dictionary = JsonToDictionary(json.dumps(each))

            if not go_update_sql_tables(flat_dictionary.__dict__):
                print("{0}: {1}".format('Error to update', flat_dictionary.__dict__))
            else:
                print("{0}: {1}".format('Updated successfully', flat_dictionary.__dict__))
    except:
        pass
    finally:
        pass
        #conn.close()

if __name__ == '__main__':
    main()
