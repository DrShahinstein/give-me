import click
import pyperclip as clip
from .password import Password
from .utils import init_json, zip_json, is_empty, write_to_json


@click.group(invoke_without_command=True)
@click.pass_context
@click.argument("password")
@click.option("--private/--no-private", is_flag=True, default=True, help="Hide or unhide passwords while viewing list")
def cli(ctx, password, private):
    ctx.ensure_object(dict)
    ctx.obj["PRIVATE"] = private

    if not password in cli.commands and ctx.invoked_subcommand is None:
        content = Password.get(password)

        if content is None:
            click.echo(f"{password} not found")
        else:
            clip.copy(content)
            colorized = click.style(password, fg="yellow")
            click.echo(f"{colorized} copied!")
    else:
        # incoming value from the user is actually a command (eg. give-me list)
        command = password
        ctx.invoke(cli.commands[command])


@cli.command()
def create():
    """Create a new password"""

    pw_name = click.prompt("Enter the name for your password")
    pw_value = click.prompt("Password", hide_input=True)
    password = {pw_name: pw_value, }

    colorized_pw = click.style(pw_name, fg="yellow")
    colorized_command = click.style(
        f"give-me {pw_name}", fg="yellow")

    write_to_json(password)

    click.echo(f"{colorized_pw} created successfully!")
    click.echo(f"You can now `{colorized_command}` it")


@cli.command()
def remove():
    """Delete a password"""

    pw_removal = click.prompt("Enter the name for your password to be removed")
    colorized_pw = click.style(pw_removal, fg="yellow")

    if Password.get(pw_removal) is not None:
        Password.pop(pw_removal)
        click.echo(f"{colorized_pw} removed successfully!")

    else:
        click.echo(f"{colorized_pw} not found.")


@cli.command()
@click.pass_context
def list(ctx):
    """List all passwords"""

    private = ctx.obj["PRIVATE"]
    z_json = zip_json()
    empty = is_empty(zip_json())

    if empty:
        click.echo("* No password available")
        return

    for pw, value in z_json:
        colorized_pw = click.style(f"{pw}", fg="yellow")

        if private:
            value = Password.hide(value)

        click.echo(f"=> {colorized_pw}: {value}")


@init_json
def main():
    cli()


if __name__ == "__main__":
    main()
