import typer

from bible_cli.database import Verse, get_session

app = typer.Typer()


@app.command()
def about():
    print(
        "✝️ BIBLE_CLI is simple cli app to query bible text from many bible portuguese versions"
    )


@app.command()
def query(q: str):
    """
    Get a text using query:
    [book] [chapter]:[verse/range] [version]

    Examples:
        Eclesiastes 3:15
        Eclesiastes 3:15-16
        Eclesiastes 3:15 ARA
    """
    session = get_session()
    verses = session.query(Verse).all()
    for v in verses:
        print(v.text)


if __name__ == "__main__":
    app()
