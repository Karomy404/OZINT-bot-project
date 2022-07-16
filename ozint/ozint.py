"""Main entry point for the ozint module"""
import typer
import domains

app = typer.Typer(help="Awesome CLI app")
state = {"verbose": False}


@app.command("whois")
def whois(domain: str):
    """Whois a domain"""
    typer.echo(f"Whois {domain}")
    dom = domains.OzintDomain(domain=domain)
    print(dom.whois())


@app.command("echo")
def echo(text: str):
    """Echo text"""
    typer.echo(text)


if __name__ == "__main__":
    app()
