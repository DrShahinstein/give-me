import click
import pyperclip as clip
from .manage import create_new, get, remove
from .utils import hide, zip_json


@click.group()
def cli(): pass


@cli.command()
@click.argument("representing_name")
def copy(representing_name):
    """Copy something you want to the clipboard."""

    content = get(representing_name)

    if content is None:
        click.echo(f"`{representing_name}` not found.")
    else:
        clip.copy(content)
        click.echo(f"{representing_name} copied!")


@cli.command()
@click.argument("representing_name")
def create(representing_name):
    """Create a new representation representing what you are going to copy."""

    content = click.prompt(f"What do you want {representing_name} to represent?")
    create_new(representing_name, content)

    click.echo(f"`{representing_name}` created successfully!")
    click.echo(f"You can now `cboard copy {representing_name}` it.")


@cli.command()
@click.argument("representing_name")
def remove(representing_name):
    """Delete a representation representing what you are going to copy."""

    if get(representing_name) is not None:
        remove(representing_name)
        click.echo(f"`{representing_name}` removed successfully!")

    else:
        click.echo(f"`{representing_name}` not found.")


@cli.command()
@click.option("--private/--no-private", is_flag=True, default=True)
def list(private):
    """List the entire representations with their contents privately or non-privately."""

    if private:
        for representation, content in zip_json():
            click.echo(f"⸱ {representation}: {hide(content)}")

    else:
        for representation, content in zip_json():
            click.echo(f"⸱ {representation}: {content}")


def main():
    cli()


if __name__ == "__main__":
    main()
