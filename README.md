# uvicorn-server

This is a python based server that utilizes fastAPI to deploy an API that provides access to data about indian banks and their branches. From the data that was provided in the sql document, a postgres database was set up. The sql document was used to populate the postgres database with the data. Once this was done, a config file containing the credentials for accessing the database was created and this config file was utilized to create a connection from within the script. Then, as per instruction, two functions were created: One was for accessing the list of names of all banks and the other was to list the details of a particular branch(the user has to provide the ifsc code for this function).

These functions were implemented as API calls and the API itself is hosted on uvicorn. In order to call the API, paste the following urls in your browser or use postman:
Get the list of all banks:
http://127.0.0.1:8000/banks

Get the details of a particular branch by providing its IFSC code:
http://127.0.0.1:8000/branches/YOUR_IFSC_CODE

The API was hosted on railway.app because heroku was a paid option and I didnt have money.


Time taken to complete task:
2-3 hours