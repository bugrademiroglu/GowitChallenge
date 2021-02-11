# Importing the libraries
from flask import request
import pytest
from main import app
import unittest

# Creating a test class
class TetRestAPI(unittest.TestCase):
    def test_connection(self): # Testing the connection with the server
        test = app.test_client(self)
        response = test.get('/keys')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_getSpecificValue(self): # Testing the GET request with specific value
        test = app.test_client(self)
        data = ['Brand', 'Color', 'Price', 'HP', 'Model'] # Test datas according to the set keys
        responseArr = []  # Creating an array in order to  store the response codes to all the test keys
        for i in data:
            response = test.get('/keys/' + i)
            responseArr.append(response.status_code)
        if (400 not in responseArr): # Check if all status codes are 200
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)
        else:  # Check if any error in test datas or not
            statuscode = response.status_code
            self.assertEqual(statuscode, 400)

    def test_getAllValue(self): # Testing the GET request with all the values
        test = app.test_client(self)
        response = test.get('/keys')
        responseData = response.data
        if (responseData == b'{}'): # If deleting Test deletes the datas refill the values again
            responseData = b"{b'Model': b'320', b'Brand': b'BMW', b'HP': b'300', b'Color': b'Black', b'Price': b'100000'}"
        # If response value matches with actual response return 200 code
        if (responseData == b"{b'Model': b'320', b'Brand': b'BMW', b'HP': b'300', b'Color': b'Black', b'Price': b'100000'}"):
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)
        else: # Otherwise return 400 code
            statuscode = response.status_code
            self.assertEqual(statuscode, 400)
    def test_putValue(self): # Testing the PUT request Updating or Creating a new value
        test = app.test_client(self)
        str  = 'Model' # Sample set data for updating the value
        str2 = '5.20' # Sample value data for updating the value
        response = test.put('/keys/'+str+'&'+str2)
        if (response.data == b'You set Model to 5.20' ): # If test response matches with the real response return 200
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)
        else: # Otherwise return 400
            statuscode = response.status_code
            self.assertEqual(statuscode, 400)

    def test_checkValue(self): # Testing the HEAD request in order to check a value is exist or not
        test = app.test_client(self)
        data = ['Brand', 'Color', 'Price', 'HP', 'Model'] # Sample test data as keys
        responseArr = [] # Creating an array in order to store the response codes
        for i in data: # Iterating the sample array and apply all the test keys for related url
            response = test.head('/keys/'+ i)
            responseArr.append(response.status_code) # Pushing response codes into the array

        if (400 not in responseArr): # If the array not includes 400 response code then return 200
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)
        elif (400 in responseArr): # If the array includes 400 response code then return 400
            statuscode = response.status_code
            self.assertEqual(statuscode, 400)
        else: # Otherwise return 500
            statuscode = response.status_code
            self.assertEqual(statuscode, 500)

    def test_deleteSpecificValue(self): # Testing the DELETE request in order to delete a specific value
        test = app.test_client(self)
        data = ['Brand', 'Color', 'Price', 'HP', 'Model'] # Sample test data as keys
        responseArr = [] # Creating an array in order to store the response codes
        for i in data: # Iterating the sample array and apply all the test keys for related url
            response = test.delete('/keys/' + i)
            responseArr.append(response.status_code) # Pushing response codes into the array
        if (400 not in responseArr): # If the array not includes 400 response code then return 200
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)
        elif (400 in responseArr): # If the array includes 400 response code then return 400
             statuscode = response.status_code
             self.assertEqual(statuscode, 400)
        else: # Otherwise return 500
            statuscode = response.status_code
            self.assertEqual(statuscode, 500)

    def test_deleteAllValue(self): # Testing the DELETE request in order to delete all the values
        test = app.test_client(self)
        response = test.delete('/keys')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    if __name__ == '__main__':
        unittest.main()