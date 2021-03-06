# Server documentation
This is the documentation for the web server

## How the server is hosted
The server is hosted on Heroku. It is built with Python, or more specifically fastapi.

I wrote a REST API in order to make my server accessible to the public.

## How the client works
My client interacts with the server using various `http requests`. The endpoints for these requests are hard coded into the cli, but you can also interact with the endpoints directly.

## How the server works
The server has a basic trie data type stored in memory. The trie is represented using the basic list data structure. Each keyword is split up into characters, and a search goes down into the trie to match these characters. It determines if there is a match like this.

## Tests
The tests are located in the `trie-server/tests.py` file.

## Endpoints
You can access the endpoints as such:

### Add
`https://slingshot-trie.herokuapp.com/api/add`
It accepts a POST Request with the name of a keyword.

### Delete
`https://slingshot-trie.herokuapp.com/api/delete`
It accepts a POST Request with the name of a keyword.

### Search
`https://slingshot-trie.herokuapp.com/api/search`
It accepts a get request with the name of a keyword.

### Suggest
`https://slingshot-trie.herokuapp.com/api/suggest`
Accepts get request with name of keyword

### Display
`https://slingshot-trie.herokuapp.com/api/display`
Accepts get request.
