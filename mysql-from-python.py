import os
import datetime
import pymysql 

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'fred']
        # prep string with same num of placeholders of in list
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names) 
        connection.commit()
        
        # Note that the above will still display a warning (not error) if the
        # table already exists
    """
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    # with connection.cursor() as cursor: # open connetion to create cursor + use connection to  create cursor 
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor: 
            print(row)
    """
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()