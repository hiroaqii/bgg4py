import json
import click
import json

from bgg4py import api
from bgg4py.valueobject import Bgg


@click.group()
def cmd():
    pass


@cmd.command()
@click.option("--id", required=True, type=int)
@click.option("--stats", is_flag=True)
@click.option("--comments", is_flag=True)
@click.option("--ratingcomments", is_flag=True)
def thing(id: int, stats=True, marketplace=False, comments=False, ratingcomments=False):
    p(api.thing(id, stats, marketplace, comments, ratingcomments))


@cmd.command()
@click.option("--id", required=True, type=int)
def family_items(id: int):
    p(api.family_items(id))


@cmd.command()
@click.option("--id", required=True, type=int)
@click.option("--search_type", type=str)
def forum_lists(id: int, search_type: str):
    p(api.forum_lists(id, search_type))


@cmd.command()
@click.option("--id", required=True, type=int)
@click.option("--page", type=int)
def forums(id: int, page: int):
    p(api.forums(id, page))


@cmd.command()
@click.option("--id", required=True, type=int)
def threads(id: int):
    p(api.threads(id))


@cmd.command()
@click.option("--name", required=True, type=str)
@click.option("--page", type=int)
def users(name: str, page: int):
    p(api.users(name, page))


@cmd.command()
@click.option("--name", required=True, type=str)
def user_collection(name: str):
    p(api.user_collection(name))


@cmd.command()
def hot_items():
    p(api.hot_items())


@cmd.command()
@click.option("--id", required=True, type=int)
@click.option("--comments", is_flag=True)
def geeklist(id: int, comments=False):
    p(api.geeklist(id, comments))


@cmd.command()
@click.option("--query", required=True, type=str)
@click.option("--exact", is_flag=True)
def search(query: str, exact=False):
    p(api.search(query, exact))


def p(obj: Bgg):
    if obj is None:
        print("Not Found 🤔")
    else:
        print(json.dumps(obj.dict(), indent=4, ensure_ascii=False))


def main():
    cmd()


if __name__ == "__main__":
    main()
