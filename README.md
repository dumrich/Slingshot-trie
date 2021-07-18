# Slingshot Trie challenge documentation
Slingshot default takehome challenge.

## What it is
My submision for the take home challenge includes a:

- REST server (written in Python)

- A REST client (written in Rust)

- Documentation (written in Markdown)

## Installation
To use this, you only have to download the CLI. The REST API is hosted on a web server. The URL is: {insert-url-here}.

1. Clone this repository and cd into the `trie-client` directory.

2. Make sure you have rustup installed. If not, you can install here [rustup](https://rustup.rs/)

3. You can access the binary by running `cargo run --release`. The binary is in the target/release folder, but you can continue to use cargo to access it.

## Usage
To use this, you have to use the `cargo` tool installed with Rustup. This is a wrapper around the Rust compiler that makes it easy to run executables.

### Add a keyword
```Rust
cargo run --add {keyword}
```

### Delete a keyword
```Rust
cargo run --delete {keyword}
```

### Search for a keyword
```Rust
cargo run --find {keyword}
```

### Return autocomplete
```Rust
cargo run --suggest {keyword}
```

### Display trie
```Rust
cargo run --display {keyword}
```




