# Slingshot Trie challenge documentation
Slingshot default takehome challenge.

## What it is
My submision for the take home challenge includes a:

- REST server (written in Python)

- A REST client (written in Rust)

- Documentation (written in Markdown)

## Installation
To use this, you only have to download the CLI. The REST API is hosted on a web server. The URL is: https://slingshot-trie.herokuapp.com/api

1. Clone this repository and cd into the `trie-client` directory.

2. Make sure you have rustup installed. If not, you can install here [rustup](https://rustup.rs/)

3. You can access the binary by running `cargo build --release`. The binary is in the `target/release` folder, and is called `trie-client`.

4. If you are on windows, you need to do `.\trie-client.exe` instead of `./trie-client`.

## Usage
To use this, you have to use the `cargo` tool installed with Rustup. This is a wrapper around the Rust compiler that makes it easy to run executables.

### Add a keyword
```Rust
$ ./trie-client {keyword}
```

### Delete a keyword
```Rust
$ ./trie-client {keyword}
```

### Search for a keyword
```Rust
$ ./trie-client {keyword}
```

### Return autocomplete
```Rust
$ ./trie-client {keyword}
```

### Display trie
```Rust
$ ./trie-client --display
```




