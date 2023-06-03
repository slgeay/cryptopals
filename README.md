# Cryptopals

Completed challenges from [Cryptopals](https://cryptopals.com/).

## Progress

### Set 1

Challenge | Python | PyGolf | Rust | RsGolf
:---:|:---:|:---:|:---:|:---:
[1](https://cryptopals.com/sets/1/challenges/1) | ✅ | ✅ | ✅ | ✅

## Usage

### Setup

```bash
poetry install
poetry shell
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