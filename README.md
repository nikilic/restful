DV : Nikola napisi kratak opis projekta i features, usage,test description koristeci **"Markdown language"** za Github

**Obavezno staviti link(ove) tutorijala koji su korisceni**, npr

https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3

Takodje __glavne izvode__ iz samog tutorijala:

**From Tutorial:**

__Implementation__


We will be creating a RESTful API that is used to store users details, which will have CRUD (Create, Read, Update, Delete) functions, allowing us to create new user, get details of existing user, update details of existing user and delete existing user.
Get:
The get method is used to retrieve a particular user details by specifying the name:

We will traverse through our users list to search for the user, if the name specified matched with one of the user in users list, we will return the user, along with 200 OK, else return a user not found message with 404 Not Found. Another characteristic of a well designed REST API is that it uses standard HTTP response status code to indicate whether a request is being processed successfully or not.

Post:
The post method is used to create a new user:

We will create a parser by using reqparse we imported earlier, add the age and occupation arguments to the parser, then store the parsed arguments in a variable, args (the arguments will come from request body in the form of form-data, JSON or XML). If a user with same name already exists, the API will return a message along with 400 Bad Request, else we will create the user by appending it to users list and return the user along with 201 Created.

Put:
The put method is used to update details of user, or create a new one if it is not existed yet.

Testing:
use Postman Chrome extension!
Example of each of thee API calls:
Get; http://.....
Post:....
PUT:.....
