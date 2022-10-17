import click
import pyperclip as clip
from .manage import create_new, get, delete
from .utils import hide, zip_json, is_empty


@click.group()
def cli(): pass


@cli.command()
@click.argument("pair_name")
def copy(pair_name):
    """Copy something you want to the clipboard."""

    content = get(pair_name)

    if content is None:
        click.echo(f"`{pair_name}` not found.")
    else:
        clip.copy(content)
        pair_name = click.style(pair_name, fg="bright_red")
        click.echo(f"{pair_name} copied!")


@cli.command()
@click.argument("pair_name")
def create(pair_name):
    """Create a new pair."""

    content = click.prompt(f"What do you want {pair_name} to represent?")
    create_new(pair_name, content)

    pair_name = click.style(pair_name, fg="bright_red")
    click.echo(f"`{pair_name}` created successfully!")
    click.echo(f"You can now `cboard copy {pair_name}` it.")


@cli.command()
@click.argument("pair_name")
def remove(pair_name):
    """Delete a pair."""

    if get(pair_name) is not None:
        delete(pair_name)
        pair_name = click.style(pair_name, fg="bright_red")
        click.echo(f"`{pair_name}` removed successfully!")

    else:
        pair_name = click.style(pair_name, fg="bright_red")
        click.echo(f"`{pair_name}` not found.")


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
