# Cryptopals

Completed challenges from [Cryptopals](https://cryptopals.com/).

## Usage

### Setup

#### Linux

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh # install rust
curl https://pyenv.run | bash # install pyenv
pyenv install 3.11.4 # install python
curl -sSL https://install.python-poetry.org | python3 - # install poetry
poetry env use python3.11 # create virtual environment
poetry shell # activate virtual environment
poetry install # install python dependencies
```

#### Windows
```powershell
rustup-init.exe # install rust
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1" # install pyenv-win
pyenv install 3.11.4 # install python
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - # install poetry
poetry env use python3.11 # create virtual environment
poetry shell # activate virtual environment
poetry install # install python dependencies
[System.Environment]::SetEnvironmentVariable('LIBCLANG_PATH', "$(poetry env info --path)\Lib\site-packages\clang\native", [System.EnvironmentVariableTarget]::User) # set LIBCLANG_PATH

```

##### Windows additional dependencies
* [Netwide Assembler (NASM)](https://www.nasm.us/)

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
[4](https://cryptopals.com/sets/1/challenges/4) | ✅ | ✅ | ✅ | 
[5](https://cryptopals.com/sets/1/challenges/5) |  |  |  | 
