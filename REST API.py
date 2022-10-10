REST API:

TO make a valid request the client needs to include 4 things:
1. URL - uniform resource locator
2. method
3. list of headers
4. body

METHOD: 

This tells the server what kind of action the client wants the server to take. 
four common method: 
a) get:  ask the server to retrieve a resource
b) post: create
c) put: edit/update
d) delete: ask the server to delete the resource


you place an order by making a POST request to the server. 
if we want to make a change, then we send a PUT request to the server


HEADERS: 
-they provide meta information about a request. 
-websites on mobiles are specially formatted by using an HTTP header called "user-agent"

BODY: 

 A REQUEST CONSISTS OF A URL (HHTP://...), A METHOD (GET, POST,PUT, DELETE), A LIST OF HEADERS(USER-AGENT), AND A BODY(DATA)

RESPONSE CONSISTS OF A STATUS CODE (200,404...), A LIST OF HEADERS AND A BODY

The most common formats found in modern APIs are JSON( javascript object notation) and XML(extensible markup language)



JSON

