import json
import os
import re
import time

import click
import cryptopals_rust

from . import *


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


@click.group()
def main():
    pass


@main.command()
def hello() -> None:
    """Show a little welcome message!"""
    print("Hello ! :wave:")


def format_time(t: int) -> None:
    """Format the time in a human readable format"""
    if t < (nd := 10**3):
        return f"{t}ns"
    s = f"{t%10**3}ns"
    if t < (nd := 10**3 * (d := nd)):
        return f"{t//d}µs {s}"
    s = f"{t//d%10**3}µs"
    if t < (nd := 10**3 * (d := nd)):
        return f"{t//d}ms {s}"
    s = f"{t//d%10**3}ms"
    if t < (nd := 60 * (d := nd)):
        return f"{t//d%60}s {s}"
    s = f"{t//d%60}s"
    if t < (nd := 60 * (d := nd)):
        return f"{t//d%60}min {s}"
    s = f"{t//d%60}min"
    if t < (nd := 24 * (d := nd)):
        return f"{t//d%24}h {s}"
    return f"{t//nd}j {t//d%24}h {s}"


def print_time(prefix: str, t: int, res: str) -> None:
    """Print the time in a human readable format and the result"""
    print(f"{bcolors.HEADER}{prefix: >6}: {format_time(t): <12} =>{bcolors.ENDC} {res}")


def check(expected, result):
    return f"{bcolors.OKGREEN}OK{bcolors.ENDC}" if expected == result else f"{bcolors.FAIL}KO{bcolors.ENDC}"


def get_path(s, c):
    s = "{:0>2}".format(int(s))
    c = "{:0>2}".format(int(c))
    path = f"set{s}/challenge{c}"
    return s,c,path


@main.command()
@click.argument("s")
@click.argument("c")
def challenge(s: str, c: str) -> None:
    """Launch the code of set S challenge C

    ex: app challenge 1 2"""

    s, c, path = get_path(s, c)

    with open(f"data/{path}.txt", "r") as f:
        data = f.read()

    expected = None
    if os.path.exists(f"result/{path}.txt"):
        with open(f"result/{path}.txt", "r") as f:
            expected = f.read()

    challenge = f"challenge{c}"
    golf = f"challenge{c}_golf"

    funcs = {
        "Python": (globals()[f"set{s}.challenge{c}"], challenge),
        "PyGolf": (globals()[f"set{s}.challenge{c}"], golf),
        "Rust": (cryptopals_rust, challenge),
        "RsGolf": (cryptopals_rust, golf),
    }

    results = {}
    times = {}
    for name, (module, func) in funcs.items():
        f = getattr(module, func)
        t = time.monotonic_ns()
        results[name] = f(data)
        times[name] = time.monotonic_ns() - t
        print_time(name, times[name], results[name])
        
    if expected:
        for n in results:
            print(f"{n: >6}", check(expected, results[n]))
    else:
        comparison = [(n1, n2) for n1 in results for n2 in results if n1 != n2]
        for n1, n2 in comparison:
            print(f"{n1: >6} == {n2: >6}", check(results[n1], results[n2]))


@main.command()
@click.argument("s")
@click.argument("c")
def init(s: str, c: str) -> None:
    """Create the files for set S challenge C

    ex: app init 1 2"""

    link = f"https://cryptopals.com/sets/{s}/challenges/{c}"
    header = f"\n### Set {s}\n\nChallenge | Python | PyGolf | Rust | RsGolf\n:---:|:---:|:---:|:---:|:---:\n"
    readme = f"[{c}]({link}) |  |  |  | \n"
    s, c, path = get_path(s, c)

    if os.path.exists(f"python/{path}.py"):
        print(f"Python set {s} challenge {c} already exists")
        return
    
    if os.path.exists(f"rust/{path}.rs"):
        print(f"Rust set {s} challenge {c} already exists")
        return
    
    if not os.path.exists(f"data/set{s}"):
        readme = header + readme
    
    os.makedirs(f"data/set{s}", exist_ok=True)
    with open(f"data/{path}.txt", "w") as f:
        pass
    
    os.makedirs(f"result/set{s}", exist_ok=True)
    with open(f"result/{path}.txt", "w") as f:
        pass

    os.makedirs(f"python/set{s}", exist_ok=True)
    with open(f"python/set{s}/__init__.py", "w") as f:
        pass

    with open(f"python/{path}.py", "w") as f:
        f.write(f"def challenge{c}(s: str) -> str:\n    return str()\n")
        f.write(f"\n\ndef challenge{c}_golf(s: str) -> str:\n    return str()\n")

    os.makedirs(f"rust/set{s}", exist_ok=True)

    with open(f"rust/{path}.rs", "w") as f:
        f.write(f"use pyo3::prelude::*;\n")
        f.write(f"\n#[pyfunction]\npub fn challenge{c}(s: String) -> PyResult<String> {{\n    Ok(String::from(\"\"))\n}}\n")
        f.write(f"\n\n#[pyfunction]\npub fn challenge{c}_golf(s: String) -> PyResult<String> {{\n    Ok(String::from(\"\"))\n}}\n")

    with open(f"README.md", "a") as f:
        f.write(readme)

    print("Done")
