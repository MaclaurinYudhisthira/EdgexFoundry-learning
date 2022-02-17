# env-1\Scripts\activate
# Set-ExecutionPolicy Unrestricted -Scope Process
# python app.py
# from flask import Flask, request
from flask import Flask,render_template, redirect, url_for, request, session, flash, abort, make_response, jsonify

# app object
app=Flask(__name__)


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

        print(request.data)
        return jsonify("Resp"), 200


if __name__ == "__main__":
    app.run(debug=True)
