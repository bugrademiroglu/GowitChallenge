
# Importing the libraries
from flask import Flask, jsonify, redirect
from flask import request, Response
import redis
import json
import os, sys

app = Flask(__name__) # Setting up the rest API
# Initialize the redis package setting credentials
r = redis.Redis(
    host='redis-14779.c239.us-east-1-2.ec2.cloud.redislabs.com',
    port='14779',
    password='9oMwXuLwhULbef48e6XshWbGYTOKpegT'
)

# Setting key-field values
carInfo = {'Brand':'BMW','Model':'320','HP':'300','Color':'Black','Price':'100000'}
r.hmset('Car',carInfo)

# This method stands for getting all the values from set
def gettingAllValues():
    return r.hgetall('Car')
# This method stands for getting specific value from set
def gettingSpecificValue(id):
    if (id == ""): # If user request contains nothing then display a message
        return 'Not Exist! You can try to search Model, Color, Price etc.'
    return r.hget('Car',id)
# This method stands for checking the searched values is exist or not
def checkTheValue(id):
    confirmFlag = '' # Defines whether the value is true or false
    if (r.hexists('Car',id)):
        confirmFlag = 'True'
    else:
        confirmFlag = 'False'
    return confirmFlag
# This method stands for handling with PUT request.
# Can update the existing value or create a new one
def setValue(str,str2):
    return r.hset('Car',str,str2)
# This method stands for deleting a specific value from set
def deleteSpecificValue(id):
    return r.hdel('Car',id)
# This method stands for clearing the set
def deleteAllValues():
    return r.delete('Car')

# Getting specific value from request ID
@app.route('/keys/<id>', methods=['GET','HEAD'])
def getValue(id):
    if (request.method == 'HEAD'): # If the request type is HEAD then checks the value

        returnValue = checkTheValue(id)
        if (returnValue == 'True'):

            return {"status": "Pass"}, 200 # If the value is exist then redirect to relevant URL with 200
        else:
            return {"status": "Fail"}, 400 # If the value is not exist then redirect to relevant URL with 400
    elif (request.method == 'GET'): # If the request type is GET then get the value which is searching for
        returnValue = gettingSpecificValue(id)
        return f'{returnValue}'

# Getting all the values from keys
@app.route('/keys', methods=['GET'])
def getAllValue():
    returnValue = gettingAllValues()
    return f'{returnValue}'
# Update the value or if the value is not exist create a new one
@app.route('/keys/<str>&<str2>',methods=['PUT'])
def putValue(str,str2):
    setValue(str,str2)
    return f'You set {str} to {str2}'

# This route delete a specific key from set
@app.route('/keys/<id>',methods=['DELETE'])
def deleteValue(id):
    deleteSpecificValue(id)
    return f'You deleted the value {id}.'
# This route clear the set with deleting all.
@app.route('/keys', methods=['DELETE'])
def deleteAllValue():
    deleteAllValues()
    return 'You deleted all the values.'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.getenv('PORT', 5000), debug=True)
