import json
from flask import make_response
import mysql.connector
class user_model():
    def __init__(self):
        #connection establishiment code
        try:
          self.conn=mysql.connector.connect(host="localhost",user="root",password="password", database="flaskapi")
          self.cur = self.conn.cursor(dictionary=True)
          print("successfully connected")
        except:
            print("some error occured in your connection")
          
    def user_getall_model(self):
        
        #Query execution code
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
           return json.dumps(result)
        else:
            return "no data found"

    
    def user_addone_model(self, data):
        try:
            # Use parameterized query to avoid SQL injection
            query = "INSERT INTO users(id, name, email, phone, role, password) VALUES(%s, %s, %s, %s, %s, %s)"
            values = (5, data['name'], data['email'], data['phone'], data['role'], data['password'])
            self.cur.execute(query, values)
            self.conn.commit()  # Commit the transaction
            return make_response({"message": "CREATED_SUCCESSFULLY"}, 201)
        except Exception as e:
            # Log the error for debugging
            print(f"Error: {e}")
            # Return an error response
            return make_response({"message": "Error occurred while adding user"}, 500)
