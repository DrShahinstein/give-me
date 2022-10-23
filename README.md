# Password Generator

A simple CLI tool helping users to copy what they need such as github tokens, google passwords and etc.

---

## Requirements

- [poetry](https://python-poetry.org/)

---

## Installation

```bash
$ git clone https://github.com/1TaylanOzturk/cboard.git
$ cd cboard/
$ poetry install
$ poetry run python3 -m cboard [OPTIONS] [ARGUMENTS]
```

---

## Build

```bash
$ poetry build
[dist]$ pip3 install cboard-0.1.0-py3-none-any.whl
```

```
$ python3 -m cboard [OPTIONS] [ARGUMENTS]
```

---

## Usage

First, let's create a new pair.

```
$ poetry run python3 -m cboard create github_password
What do you want github_password to represent?: MY_GITHUB_PASSWORD
github_password created successfully!
You can now cboard copy github_password it. # The command here shows up with a yellow color in the terminal
```

Let's see how it shows up in the list.

```
$ poetry run python3 -m cboard list
⸱ github_password: MY_GITHUB_PASSWORD # The pair name here shows up with a yellow color in the terminal
```

Well, let's try to copy `github_password` to the clipboard. After that, you will be able to CTRL+V this.

```
$ poetry run python3 -m cboard copy github_password
github_password copied! # The pair name here shows up with a yellow color in the terminal
```

Now, let's see how removing a pair works.

```
$ poetry run python3 -m cboard remove github_password
github_password removed successfully! # The pair name here shows up with a yellow color in the terminal
```

```
$  poetry run python3 -m cboard list
⸱ Not any pair.
```
