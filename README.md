
# NurtureLabs Assignment

## Backend Assignment (Python)
### APIs using Django (or any other Python-based Web framework) for an advisor network where users can come and book an advisor for a call.
### The following roles should be allowed

## Admin
### API: Add an advisor
#### Method:
* POST
#### Authentication
* Not needed for this assignment
#### Endpoint: 
* /admin/advisor/
#### Request:
* Advisor name
* Advisor Photo URL
##### Response:
* No Response
* Just return 200_OK if the request is successful
* Return 400_BAD_REQUEST if any of the above fields are missing

## User
### API: Can register as a user
#### Method:
* POST
#### Endpoint: 
* /user/register/
#### Request:
* Name
* Email
* Password
#### Response:
##### Body:
* JWT Authentication Token
* User id
##### Status
* 200_OK if the request is successful
* 400_BAD_REQUEST if any of the above fields are missing
### API: Can log in as a user
#### Method:
* POST
#### Endpoint: 
* /user/login/
#### Request:
* Email
* Password
#### Response:
##### Body:
* JWT Authentication Token
* User id
##### Status
* 200_OK if the request is successful
* 400_BAD_REQUEST if any of the above fields are missing
* Return 401_AUTHENTICATION_ERROR if the email/password combination was wrong
### API: Get the list of advisors
#### Method:
* GET
#### Endpoint: 
* /user/<user-id>/advisor
#### Request:
* None
#### Response:
##### Body:
* An array of advisor objects with each object having
* Advisor Name
* Advisor Profile Pic
* Advisor Id
##### Status
* 200_OK if the request is successful
### API: Can book call with an advisor
#### Method:
* POST
#### Endpoint: 
* /user/<user-id>/advisor/<advisor-id>/
#### Request:
* Booking time (a DateTime string)
#### Response:
##### Body:
* None
##### Status
* 200_OK if the request is successful
### API: Can get all the booked calls
#### Method:
* GET
#### Endpoint: 
* /user/<user-id>/advisor/booking/
#### Request:
* None
#### Response:
##### Body:
* An array of advisor objects with each object having
* Advisor Name
* Advisor Profile Pic
* Advisor Id
* Booking time
* Booking id
##### Status
* 200_OK if the request is successful


