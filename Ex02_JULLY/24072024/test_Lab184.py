# Request Module -
# Module -> Package or library contains fucntions which you can use #easily
# math, os, csv, allure, , pytest

# To make the HTTP - Methods
# Request - Module
# GET, POST, PUT, PATCH, DELETE, OPTIONS.... HTTP Methods
# URL, Auth, Cookies, Verification with pytest.

# GET Request - Booking ID

# Request (Client - Server)

# URL -> https://restful-booker.herokuapp.com/booking
# Auth? -> X
# Payload - X
# Content-Type - or Header -> X
# Query Param? -> X
# Path Param - Yes - 1

# Response

# Body -> Verify - Assert. , # Keys, Values
# Status Code -> Verify
# Time
# JSON Schema , XML Schema



import pytest
import allure
import requests

@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#1 - Verify the GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Rohit")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    assert responseData.status_code == 200



@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#2 - Verify the GET Request with Invalid ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert responseData.status_code == 404


@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#3 - Verify the GET Request with ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_negative1():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    assert responseData.status_code != 200




























