# give-me

A simple CLI program to help copy-pasting.

---

## Requirements

- [poetry](https://python-poetry.org/)

---

## Installation

```bash
$ git clone https://github.com/DrShahinstein/give-me.git
$ cd give-me/
$ poetry install
$ poetry run python -m give_me [OPTIONS] [ARGUMENTS]
```

---

## Build

```bash
$ poetry build
$ cd dist/
[dist]$ pip install give_me-0.1.0-py3-none-any.whl
```

```
$ give_me [password_name | any_command]
```

---

## Usage

First, let's create a new password.

```
$ poetry run python -m give_me create
Enter the name for your password: my_google_password
Password: # this is being typed out in here privately as it is a password
my_google_password created successfully!
You can now `give-me my_google_password` it
```

Let's see how it shows up in the list.

```
$ poetry run python -m give_me list
=> my_google_password: ***
```

If you'd like to view passwords visibly, add `--no-private` option
```
$ poetry run python -m give_me --no-private list
=> my_google_password: 123
```

Well, let's try to copy `my_google_password` to the clipboard.

```
$ poetry run python -m give-me my_google_password
'github_password' copied!
```

Now, let's see how removing a password works.

```
$ poetry run python -m give-me remove
Enter the name for your password to be removed: my_google_password
`my_google_password` removed successfully!
```

```
$  poetry run python -m give-me list
* No password available
```
