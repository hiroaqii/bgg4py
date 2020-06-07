from typing import List, Union, Optional

from bgg4py.request import fetch_api
from bgg4py.valueobject import (
    HotItem,
    UserCollection,
    User,
    Forum,
    ForumList,
    FamilyItem,
    GeekList,
    Thread,
    Thing,
    Search,
)


def thing(
    id: Union[int, List[int]], stats=True, marketplace=False, comments=False, ratingcomments=False
) -> Optional[Thing]:

    if type(id) == int or len(str(id).split(",")) == 1:
        id = [str(id)]

    params = {"id": ",".join(id)}
    if stats:
        params["stats"] = 1
    if marketplace:
        params["marketplace"] = 1
    if comments:
        params["comments"] = 1
    if ratingcomments:
        params["ratingcomments"] = 1

    dic = fetch_api("thing", params)
    if dic.get("items", {}).get("item") is None:
        return None

    return Thing.create(dic["items"]["item"])


def family_items(id: Union[int, List[int]]) -> Optional[FamilyItem]:

    if type(id) == int or len(str(id).split(",")) == 1:
        id = [str(id)]

    params = {"id": ",".join(id)}
    dic = fetch_api("family", params)
    if dic.get("items", {}).get("item") is None:
        return None

    return FamilyItem.create(dic["items"]["item"])


def forum_lists(id: int, search_type: str = "thing") -> Optional[ForumList]:

    if search_type not in ["thing", "family"]:
        search_type = "thing"
    params = {"id": id, "type": search_type}

    dic = fetch_api("forumlist", params)
    if dic.get("forums", {}).get("forum") is None:
        return None

    return ForumList.create(dic["forums"])


def forums(id: int, page: int = 1) -> Optional[Forum]:

    params = {"id": id, "page": page}
    dic = fetch_api("forum", params)
    if dic.get("forum", {}).get("threads") is None:
        return None

    return Forum.create(dic["forum"])


def threads(id: int) -> Optional[Thread]:

    params = {"id": id}
    dic = fetch_api("thread", params)
    if dic.get("thread") is None:
        return None

    return Thread.create(dic["thread"])


def users(name: str, page: int = 1) -> Optional[User]:

    params = {"name": name, "guilds": 1, "hot": 1, "top": 1, "page": page}
    dic = fetch_api("user", params)
    if dic.get("user") is None:
        return None

    return User.create(dic.get("user"))


def user_collection(username: str, params: dict = {}) -> Optional[UserCollection]:

    params["username"] = username
    dic = fetch_api("collection", params)
    if dic.get("items", {}).get("item") is None:
        return None

    return UserCollection.create(dic["items"]["item"])


def hot_items(search_type: str = "boardgame") -> Optional[HotItem]:
    search_types = [
        "boardgame",
        "rpg",
        "videogame",
        "boardgameperson",
        "rpgperson",
        "boardgamecompany",
        "rpgcompany",
        "videogamecompany",
    ]

    if search_type not in search_types:
        search_type = "boardgame"

    dic = fetch_api("hot", {"type": search_type})
    if dic.get("items", {}).get("item") is None:
        return None

    return HotItem.create(dic["items"]["item"])


def geeklist(id: int, comments=False) -> Optional[GeekList]:

    params = {}
    if comments:
        params["comments"] = 1

    dic = fetch_api("geeklist/" + str(id), params)
    if dic.get("error"):
        return None

    if dic.get("geeklist") is None:
        return None

    return GeekList.create(dic["geeklist"])


def search(query: str, exact=False) -> Optional[Search]:

    params = {"query": query}
    if exact:
        params["exact"] = 1

    dic = fetch_api("search", params)
    if dic.get("items", {}).get("item") is None:
        return None

    return Search.create(dic["items"]["item"])
