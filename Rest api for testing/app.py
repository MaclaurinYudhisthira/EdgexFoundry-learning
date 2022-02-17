# env-1\Scripts\activate
# Set-ExecutionPolicy Unrestricted -Scope Process
# python app.py
# from flask import Flask, request
from flask import Flask,render_template, redirect, url_for, request, session, flash, abort, make_response, jsonify

import requests

token_url="https://mobility366-dsom-rest.trybmc.com/api/jwt/login"
data_push_url="https://mobility366-dsom-rest.trybmc.com/api/arsys/v1/entry/"
form_name="FUS:PeopleCount"

# app object
app=Flask(__name__)

def Create(data):
    # Generating token
    response=requests.post(token_url,data={'username':'Allen','password':'Password_1234'})
    token=response.text
    # print(token)

    # Pushing data into form
    url=f"{data_push_url}{form_name}/"
    print("Sending to Remedy...")

    data=dict(data)
    js={
        "values":{
            "DeviceName":data['deviceName'],
            "PeopleCount":data['readings'][0]['value'],
            "Payload":data
        }
    }
    response=requests.post(url,headers={'Authorization':f"AR-JWT {token}"},json=js)
    # print(response.status_code)

# Routes
@app.route("/")
@app.route("/get")
def home():
    return {"Msg":"ping pong"}

@app.route("/post",methods=['POST'])
def post():
    if request.method=='POST':
        f = open("datafile.txt", "a")
        f.write("newline \n")
        f.write(f"{request.data}")
        f.write("\n")
        f.close()

        # print(request.data)
        Create(request.data)
        return jsonify("Resp"), 200


if __name__ == "__main__":
    app.run(debug=True)