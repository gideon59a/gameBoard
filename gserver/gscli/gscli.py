import click

@click.group()
def gscli():  # The highest level, no need to enter it in the cli
    click.echo(f"gscli done")

@gscli.group()
def admin():
    click.echo(f"admin commands done")

@admin.group()
def game():
    click.echo(f"game commands done")

@game.command()
def list():
    click.echo(f"game list done")

@game.command()
@click.argument('id', nargs=-1 )
def delete(id):
    for ii in id:
        click.echo(f"game delete {ii} done")


if __name__ == "__main__":
    gscli()

