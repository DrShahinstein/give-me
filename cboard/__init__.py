import click
import pyperclip as clip
from .manage import create_new, get
from .utils import hide, zip_json, is_empty, pop


@click.group()
def cli(): pass


@cli.command()
@click.argument("pair")
def copy(pair):
    """Copy something you want to the clipboard."""

    content = get(pair)

    if content is None:
        click.echo(f"{pair} not found.")
    else:
        clip.copy(content)
        pair = click.style(pair, fg="bright_red")
        click.echo(f"{pair} copied!")


@cli.command()
@click.argument("pair")
def create(pair):
    """Create a new pair."""

    content = click.prompt(f"What do you want {pair} to represent?")
    create_new(pair, content)

    pair = click.style(pair, fg="bright_red")
    click.echo(f"{pair} created successfully!")
    click.echo(f"You can now cboard copy {pair} it.")


@cli.command()
@click.argument("pair")
def remove(pair):
    """Delete a pair."""

    if get(pair) is not None:
        pop(pair)
        pair = click.style(pair, fg="bright_red")
        click.echo(f"{pair} removed successfully!")

    else:
        pair = click.style(pair, fg="bright_red")
        click.echo(f"{pair} not found.")


@cli.command()
@click.option("--private/--no-private", is_flag=True, default=False)
def list(private):
    """List all pairs."""

    z_json = zip_json()
    empty = is_empty(zip_json())

    if empty:
        click.echo("⸱ Not any pair.")

    elif private:
        for pair, value in z_json:
            click.echo(f"⸱ {pair}: {hide(value)}")

    else:
        for pair, value in z_json:
            click.echo(f"⸱ {pair}: {value}")


def main():
    cli()


if __name__ == "__main__":
    main()
