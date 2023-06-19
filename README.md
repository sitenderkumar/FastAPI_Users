Create/Read/Update/Delete Users using Fast API Endpoints, Mongo DB, Okta Auth01 Token

In order to run the example you need to have python3 (any version higher than 3.6) and pip3 installed, you'll also need an Auth0 account, any DB to store the value of users persistently, in my case, I have used Mongo DB local installatable.

FastAPI for Python : Web API framework used in the program
Uvicorn : Web Server compoment used in the program
MongoDB : Used in the programto store the value of users
Okta Autho0: Authentication method/servie used in the program
=============Steps followed in the program=====
Following are the steps that has been followed, for a visual representationn of the flow/design, please refer architecture_design file
Install Python 3.6 or higher
Install Uvicorn
Install MongoDB on local system
Subscribe to Okta Autho0, crate an API and token which will be used for authentication.

Details of the endpoints creatd for this program
a) createuser
b)getuser
c)updateuser
d)deleteuser
