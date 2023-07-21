# Cryptopals

Completed challenges from [Cryptopals](https://cryptopals.com/).

## Usage

### Setup

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh # install rust
pyenv install 3.11.4 # install python
poetry env use python3.11 # create virtual environment
poetry shell # activate virtual environment
poetry install # install python dependencies
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

## Progress

### Set 1

Challenge | Python | PyGolf | Rust | RsGolf
:---:|:---:|:---:|:---:|:---:
[1](https://cryptopals.com/sets/1/challenges/1) | ✅ | ✅ | ✅ | ✅
[2](https://cryptopals.com/sets/1/challenges/2) | ✅ | ✅ | ✅ | ✅
[3](https://cryptopals.com/sets/1/challenges/3) | ✅ | ✅ | ✅ | ✅
[4](https://cryptopals.com/sets/1/challenges/4) |  |  |  | 
