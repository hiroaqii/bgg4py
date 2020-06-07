from collections import OrderedDict
from .bgg import Bgg


class User(Bgg):
    id: int
    name: str
    firstname: str
    lastname: str
    avatarlink: str
    yearregistered: int
    lastlogin: str
    stateorprovince: str
    country: str
    webaddress: str
    xboxaccount: str
    wiiaccount: str
    psnaccount: str
    battlenetaccount: str
    steamaccount: str
    traderating: int
    marketrating: int

    @classmethod
    def create(cls, user: OrderedDict):
        return User(
            id=Bgg.parse_int(user.get("@id")),
            name=user.get("@name"),
            firstname=user.get("firstname", {}).get("@value"),
            lastname=user.get("lastname", {}).get("@value"),
            avatarlink=user.get("avatarlink", {}).get("@value"),
            yearregistered=Bgg.dict_value_to_int(user.get("yearregistered")),
            lastlogin=user.get("lastlogin", {}).get("@value"),
            stateorprovince=user.get("stateorprovince", {}).get("@value"),
            country=user.get("country", {}).get("@value"),
            webaddress=user.get("webaddress", {}).get("@value"),
            xboxaccount=user.get("xboxaccount", {}).get("@value"),
            wiiaccount=user.get("wiiaccount", {}).get("@value"),
            psnaccount=user.get("psnaccount", {}).get("@value"),
            battlenetaccount=user.get("battlenetaccount", {}).get("@value"),
            steamaccount=user.get("steamaccount", {}).get("@value"),
            traderating=Bgg.dict_value_to_int(user.get("traderating")),
            marketrating=Bgg.dict_value_to_int(user.get("marketrating")),
        )
