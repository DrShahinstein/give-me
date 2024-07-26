# give-me

`give_me` is a cli program to help with password management.

## Features

- Create new passwords
- Edit existing passwords
- Remove passwords
- List all passwords
- Copy passwords to clipboard
- Option to show passwords in plain text or hidden text
- Passwords are stored encrypted

## Installation

[poetry](https://python-poetry.org/docs/#installing-with-pipx) tool is required.

```bash
$ git clone https://github.com/DrShahinstein/give-me.git
$ cd give-me/
$ poetry install
$ poetry run python -m give_me [...] # run
```

## Build

```bash
$ poetry build
$ cd dist/
[dist]$ pip install give_me-0.1.0-py3-none-any.whl
```

```
$ give_me <command_or_password_name>
```

## Example

```bash
give_me list
No passwords available

give_me create
Enter name for password: ghtoken
Password:
ghtoken created successfully!

give_me list
ghtoken: ****************************************

give_me create
Enter name for password: anyother
Password:
anyother created successfully!

give_me list
ghtoken: ****************************************
anyother: ***

give_me list --no-private
ghtoken: '!%(=!%some=!)(%)'github)'=!()='!token!(%)='()'
anyother: 123

give_me anyother
anyother copied!

give_me remove anyother
anyother removed successfully!

give_me list
ghtoken: ****************************************
```
