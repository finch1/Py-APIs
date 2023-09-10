import time
import sqlalchemy as db

class MySQLDataAccess():

    # implement reconnect if DB is down
    while True:
        try:
            connection_string = "mysql+mysqlconnector://root:simple@localhost:3306/posts"
            # echo set to True, so you can see the SQL statements that SQLAlchemy sends to your database.
            engine = db.create_engine(connection_string, echo=True)
            conn = engine.connect()
            break # break from while if connection established

        except Exception as error:
            print("Failed connecting to database!")
            print("Error: ", error)
            time.sleep(2) # seconds

    conn