# Slingshot Trie challenge documentation
Slingshot default takehome challenge.

## What it is
My submision for the take home challenge includes a:

- REST server (written in Python)

- A REST client (written in Python, with a Rust implementation)

- Documentation (written in Markdown)

## Installation
To use this, you only have to download the CLI. The REST API is hosted on a web server. The URL is: https://slingshot-trie.herokuapp.com/api

1. Clone this repository and cd into the `trie-client` directory.

2. Make sure you have python installed

3. Run `python client.py --keyword {keyword}`



## Usage
To use this, you have to use the `python` interpreter installed.

### Add a keyword
```Rust
$ python client.py --keyword {keyword}
Enter a function you would like to perform: add
```

### Delete a keyword
```Rust
$ python client.py --keyword {keyword}
Enter a function you would like to perform: delete
```

### Search for a keyword
```Rust
$ python client.py --keyword {keyword}
Enter a function you would like to perform: search
```

### Return autocomplete
```Rust
$ python client.py --keyword {keyword}
Enter a function you would like to perform: suggest
```

### Display trie
```Rust
$ python client.py --keyword {keyword}
Enter a function you would like to perform: display
```




