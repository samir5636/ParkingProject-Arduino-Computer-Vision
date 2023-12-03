import serial
import cv2
import pytesseract
import time

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
        query = "SELECT id ,matricule ,is_in_parking ,model ,client_id  FROM car WHERE matricule = %s"
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
def search_abonement_by_car_id(car_id):
    # Establish a connection to the database
    connection ,cursor = get_connection()
    try:
        # Execute the query to search for a car by matricule
        query = "SELECT id ,sold  FROM abonement WHERE car_id = %s"
        cursor.execute(query, (car_id,))
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
def change_sold_abonemt_by_id_car(car_id, ticket):
    # Establish a connection to the database
    connection, cursor = get_connection()
    try:
        # Execute the query to update the sold value for a given car_id
        update_query = "UPDATE abonement SET sold = sold - %s WHERE car_id = %s"
        cursor.execute(update_query, (ticket, car_id,))
        connection.commit()  # Commit the changes to the database
        print("updated !!!")
        # After updating, retrieve the updated abonnement information
        select_query = "SELECT id, sold FROM abonement WHERE car_id = %s"
        cursor.execute(select_query, (car_id,))
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
def change_is_in_parking_by_id_car(car_id,is_in_parking):
    # Establish a connection to the database
    connection, cursor = get_connection()
    try:
        # Execute the query to update the sold value for a given car_id
        update_query = "UPDATE car SET is_in_parking = %s WHERE id = %s"
        cursor.execute(update_query, (is_in_parking, car_id,))
        print("updated !!!")
        connection.commit()  # Commit the changes to the database
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()
ticket=3.5
def main(serial_port: str):
    # Initialize the serial connection
    try:
        ser = serial.Serial(serial_port, baudrate=9600, timeout=1)
        print(f"Serial connection established on port {serial_port}")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return
    ser.write(b"C")
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
            matricule:str = pytesseract.image_to_string(frame)
            matricule=matricule.strip()
            try:
                existing_car = search_car_by_matricule(matricule)
            except Exception as e:
                existing_car = False
                print(f"Error searching for car: {e}")

            # Display the text on the frame
            cv2.putText(frame, f"Matricule: {matricule}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(existing_car)
            print(f"matricule : {matricule}")
            if existing_car:
                print("Car exist.")
                car_id, matricule, is_in_parking, model, client_id = existing_car
                if is_in_parking:
                    ser.write(b'o')
                    print("o")#serial
                    # print("Car exists and is in the parking. Open door before user enters.")
                    cv2.putText(frame, "Car in parking - Open door before user enters", (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    change_is_in_parking_by_id_car(car_id,False)
                    ser.write(b'C')
                    print("c")#serial
                else:
                    abonement_car=search_abonement_by_car_id(car_id)
                    if abonement_car:
                        id_aboenemnt,sold=abonement_car
                        if(sold>=ticket):
                            change_sold_abonemt_by_id_car(car_id,ticket)
                            change_is_in_parking_by_id_car(car_id,True)
                            print("O")#serial
                            ser.write(b'O')
                            ser.write(b'C')
                            print("c")#serial
                            # print("Car exists but is not in the parking. Open door after user exits.")
                        else:
                            print("s")#Serial : sold insuffisant
                    cv2.putText(frame, "Car not in parking - Open door after user exits", (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                time.sleep(2)    
            else:
                print("n")#serial
                ser.write(b'n')
                # print("Car not found. Not a client.")
                cv2.putText(frame, "Car not found - Not a client", (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 0, 255), 2)

            # Display the frame
            cv2.imshow('Camera Test', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Camera closed.")



if __name__ == "__main__":
    main("/dev/ttyACM0")  # Change "COM1" to the correct serial port on your system

