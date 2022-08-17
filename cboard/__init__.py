import click
import pyperclip as clip


@click.group()
def cli(): pass


@cli.command()
@click.argument("name")
def copy(name):
    """Copy something you want to the clipboard."""

    # TODO: Get the name and copy it to the clipboard.
    clip.copy()

    click.echo(f"{name} copied!")


@cli.command()
@click.argument("name")
def create(name):
    """Create a new representation representing what you are going to copy."""

    text = click.prompt(f"What do you want {name} to represent?")
    # TODO: Create a new representation.

    click.echo(f"`{name}` created successfully!")
    click.echo(f"You can now `cboard copy {name}` it.")


def main():
    cli()


if __name__ == "__main__":
    main()
