REST
====

REST stands for REpresentational State Transfer. REST is an architecture style for designing networked applications. It is based on stateless, client-server, cacheable communications protocol. Although not based on http, in most cases, the HTTP protocol is used.  In contrast to what some others write or say, REST is not a *standard*.


RESTful applications use HTTP requests to:

* post data: while creating and/or updating it,
* read data: while making queries, and
* delete data.

Hence REST uses HTTP for the four CRUD operations:

* Create
* Read
* Update
* Delete

.. list-table:: HTTP Methods
   :widths: 10 10 10 10 10
   :header-rows: 1

   * - URL
     - GET
     - PUT
     - POST
     - DELETE
   * - http://.../resources/
     - List the URIs and perhaps other details of the collection's members.
     - Replace the entire collection with another collection. 
     - Create a new entry in the collection. The new entry's URI is assigned automatically and is usually returned by the operation. 
     - Delete the entire collection.
   * - http://.../resources/item17
     - Retrieve a representation of the addressed member of the collection, expressed in an appropriate Internet media type. 
     - Replace the addressed member of the collection, or if it does not exist, create it. 
     - Not generally used. Treat the addressed member as a collection in its own right and create a new entry within it.
     - Delete the addressed member of the collection.

Source: https://en.wikipedia.org/wiki/Representational_state_transfer

