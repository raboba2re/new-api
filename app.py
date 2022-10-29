from flask import Flask,request, json 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/create_user', methods = ["POST"])
def post_request():
    name = request.json["name"]
    email = request.json["email"]
    age = request.json["age"]
    phone_number = request.json["phoneNumber"]
    
    return {"name":name,
            "email":email, 
            "age": age, 
            "phoneNumber":phone_number
            }
    
    
@app.route('/get_user', methods = ["GET"])
def get_request():
    user = {"name":"rab0",
            "email":"rabobature@gmail.com",
            "age": 28, 
            "phone_number": +2348100561772
            }
    return user 
 
if __name__ == ("__main__"):
    app.run(debug = True)
    
 
     
