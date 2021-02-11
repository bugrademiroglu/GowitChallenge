# Gowit Coding Challenge Assignment
## About
It's a simple key-value store application end point. It's provide a Rest API in order to set, get, check and delete a key-value pair.
## How it works
Accepts HTTP GET, HEAD, PUT or DELETE
* get a value (GET /keys/{id})
* get all values (GET /keys)
* set a value (PUT /keys)
* check if a value exists (HEAD /keys/{id})
* delete a value (DELETE /keys/{id})
* delete all values (DELETE /keys)

In this project there is predefined key-value hash.

```python
carInfo = {'Brand':'BMW','Model':'320','HP':'300','Color':'Black','Price':'100000'}
```
1. To getting a specific key you can request (for exp BMW)
* http://localhost:5000/keys/BMW
2. To getting all the keys you can request
* http://localhost:5000/keys
3. To making a PUT request and updating or creating a new value you can
* http://localhost:5000/keys/Color&Red (As a PUT Request) (/st1&str2])
4. To checking a value is exist or not you can make a HEAD request with specific value
* http://localhost:5000/keys/Price
5. To deleting a specific value you can make a DELETE request
* http://localhost:5000/keys/Price
6. To deleting all the values you can make a DELETE request
* http://localhost:5000/keys/Price
#Requirements
* At least Python version of 3.2
* redis~=3.5.3
* Flask~=1.1.2
* Docker
##Technologies
In this project, Python was used as a backend language and Flask framework was used a web service and Redis.

The reason why I chose Flask framework is it's easy to setting up and running. You can use the facilities and libraries provided by the Python language.

##Installation and Run
To run the code:

###### On terminal:
 ```bash
cd GowitChallenge
pip install -r requirements.txt
python main.py
```

###### On Docker compose: 
```bash
docker-compose up
```
######View
```bash
http://localhost:5000
```
######Stop
```bash
docker-compose stop
```
###### To running with Docker file on your host: 
```bash
docker build --tag <Enter a tag name> .
```
Then,
```bash
docker run --rm -i -t <Your tag name> (This path run the code on your)
```
If you want to map the port and acces on your local machine:
```bash
docker run -rm -i -t -p 8080:5000 <Your tag name>(This path run the code on your)
```
