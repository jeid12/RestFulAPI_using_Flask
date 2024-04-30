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

    
    def  user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users( name, email, phone, role, password) VALUES({data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')") 
        
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)     