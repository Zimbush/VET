import typer

app = typer.Typer()

@app.command()
def hello(name: str = 'World'):
    print(f"Hello {name} from installer!")


if __name__ == "__main__":
    app()