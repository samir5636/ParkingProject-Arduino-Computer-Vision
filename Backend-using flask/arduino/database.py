import mysql.connector

def get_connection()->tuple:
    # Establish a connection
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="admin",
        database="parking"
    )
    # Create a cursor
    cursor = connection.cursor()
    return connection,cursor
def search_car_by_matricule(matricule):
    # Establish a connection to the database
    connection ,cursor = get_connection()
    try:
        # Execute the query to search for a car by matricule
        query = "SELECT id ,matricule ,is_in_parking ,model ,client_id , FROM Car WHERE matricule = %s"
        cursor.execute(query, (matricule,))
        # Fetch the result
        result = cursor.fetchone()

        if result:
            return result
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()