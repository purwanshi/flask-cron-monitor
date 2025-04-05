import os
from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
	return "hello world from  PURWANSHI MISHRA"

@app.route("/compute")
def compute():
	return str(fact(100))
 
def fact(n):
	if n==0:
		return 1
	result =1
	for i in range(1,n+1):
		result=result*i
	return result

if __name__ == '__main__':
 	app.run(debug=True,host="0.0.0.0")
