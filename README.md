# Cryptopals

Completed challenges from [Cryptopals](https://cryptopals.com/).

## Progress

### Set 1

Challenge | Python | PyGolf | Rust | RsGolf
:---:|:---:|:---:|:---:|:---:
[1](https://cryptopals.com/sets/1/challenges/1) | ✅ | ✅ | ✅ | ✅
[2](https://cryptopals.com/sets/1/challenges/2) | ✅ | ✅ | ✅ | ✅

## Usage

### Setup

```bash
poetry install # install python dependencies
poetry shell # activate virtual environment
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh # install rust
cargo install maturin # install maturin
```

### Run challenge

```bash
maturin develop # deploy rust modules
poetry run app challenge <Set> <Challenge>
```

### Next challenge

```bash
poetry run app init <Set> <Challenge>
```
