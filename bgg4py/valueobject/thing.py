from collections import OrderedDict
from typing import Dict, List, Optional, Union
from .bgg import Bgg


class Link(Bgg):
    type: str
    id: int
    value: str

    @classmethod
    def create_list(cls, links: OrderedDict) -> List:

        if links is None:
            return links

        _links = []
        lst = [links] if type(links) == OrderedDict else links
        for x in lst:
            link = Link(id=int(x["@id"]), type=x["@type"], value=x["@value"])
            _links.append(link)

        return _links


class Poll(Bgg):
    suggested_numplayers: Dict[str, Dict[str, int]]
    suggested_playerage: Dict[str, int]
    language_dependence: Dict[str, int]

    @classmethod
    def create(cls, poll: OrderedDict):

        if poll is None:
            return None

        poll_dic = {}
        for p in poll:
            if p.get("@totalvotes") != "0":
                poll_dic[p["@name"]] = p["results"]

        suggested_playerage = {}
        if poll_dic.get("suggested_playerage"):
            for ret in poll_dic["suggested_playerage"]["result"]:
                suggested_playerage[ret["@value"]] = int(ret["@numvotes"])

        language_dependence = {}
        if poll_dic.get("language_dependence"):
            for ret in poll_dic["language_dependence"]["result"]:
                language_dependence["level_{0}".format(ret["@level"])] = int(ret["@numvotes"])

        suggested_numplayers = {}
        if poll_dic.get("suggested_numplayers"):
            suggested_numplayers = {}
            for results in poll_dic["suggested_numplayers"]:
                suggested_votes = {}
                for ret in results["result"]:
                    suggested_votes[ret["@value"]] = int(ret["@numvotes"])
                    suggested_numplayers["numplayers_{0}".format(results["@numplayers"])] = suggested_votes

        return Poll(
            language_dependence=language_dependence,
            suggested_playerage=suggested_playerage,
            suggested_numplayers=suggested_numplayers,
        )


class Rank(Bgg):
    id: int
    type: str
    name: str
    friendlyname: str
    value: str
    bayesaverage: float


class Statistics(Bgg):
    usersrated: int
    average: float
    bayesaverage: float
    stddev: float
    median: float
    owned: int
    trading: int
    wanting: int
    wishing: int
    numcomments: int
    numweights: int
    averageweight: float
    ranks: List[Rank]

    @classmethod
    def create(cls, statistics: OrderedDict):

        if statistics is None:
            return None

        ratings = statistics["ratings"]
        ranks = []
        lst = []
        if ratings.get("ranks") and ratings["ranks"].get("rank"):
            obj = ratings["ranks"]["rank"]
            lst = [obj] if type(obj) == OrderedDict else obj

        for x in lst:
            rank = Rank(
                id=int(x["@id"]),
                type=x["@type"],
                name=x["@name"],
                friendlyname=x["@friendlyname"],
                value=int(x["@value"]),
                bayesaverage=float(x["@bayesaverage"]),
            )
            ranks.append(rank)

        return Statistics(
            usersrated=int(ratings["usersrated"]["@value"]),
            average=float(ratings["average"]["@value"]),
            bayesaverage=float(ratings["bayesaverage"]["@value"]),
            stddev=float(ratings["stddev"]["@value"]),
            median=float(ratings["median"]["@value"]),
            owned=int(ratings["owned"]["@value"]),
            trading=int(ratings["trading"]["@value"]),
            wanting=int(ratings["wanting"]["@value"]),
            wishing=int(ratings["wishing"]["@value"]),
            numcomments=int(ratings["numcomments"]["@value"]),
            numweights=int(ratings["numweights"]["@value"]),
            averageweight=float(ratings["averageweight"]["@value"]),
            ranks=ranks,
        )


class Comment(Bgg):
    username: str
    rating: Optional[float]
    comment: Optional[str]

    @classmethod
    def create_list(cls, comments: OrderedDict) -> List:

        if comments is None:
            return None

        _comments = []
        for cmnt in comments.get("comment", []):
            rating = cmnt.get("@rating")
            if rating is None or rating == "N/A":
                rating = None
            else:
                rating = float(rating)

            comment = Comment(username=cmnt.get("@username"), comment=cmnt.get("@value"), rating=rating)
            _comments.append(comment)

        return comments


class Marketplacelistings(Bgg):
    listdate: str
    price: float
    currency: str
    condition: str
    notes: str
    link: str

    @classmethod
    def create_list(cls, marketplacelistings: OrderedDict) -> List:

        if marketplacelistings is None:
            return None

        listings = marketplacelistings.get("listing", [])
        lst = []

        for x in listings:
            mkpc = Marketplacelistings(
                listdate=x["listdate"]["@value"],
                price=float(x["price"]["@value"]),
                currency=x["price"]["@currency"],
                condition=x["condition"]["@value"],
                notes=x["notes"]["@value"],
                link=x["link"]["@href"],
            )
            lst.append(mkpc)

        return lst


class Item(Bgg):
    id: int
    type: str
    thumbnail: Optional[str]
    image: Optional[str]
    name: Optional[str]
    description: Optional[str]
    yearpublished: Optional[int]
    minplayers: Optional[int]
    maxplayers: Optional[int]
    playingtime: Optional[int]
    minplaytime: Optional[int]
    maxplaytime: Optional[int]
    minage: Optional[int]
    poll: Optional[Poll]
    links: Optional[List[Link]]
    comments: Optional[List[Comment]]
    marketplacelistings: Optional[List[Marketplacelistings]]
    statistics: Optional[Statistics]


class Thing(Bgg):
    items: List[Item]

    @classmethod
    def create(cls, items: OrderedDict):

        if type(items) == OrderedDict:
            lst = [items]
        else:
            lst = items

        ret = []
        for x in lst:
            lnks = Link.create_list(x.get("link"))
            poll = Poll.create(x.get("poll"))
            statistics = Statistics.create(x.get("statistics"))
            comments = Comment.create_list(x.get("comments"))
            marketplacelistings = Marketplacelistings.create_list(x.get("marketplacelistings"))

            item = Item(
                id=int(x["@id"]),
                type=x["@type"],
                thumbnail=x.get("thumbnail"),
                image=x.get("image"),
                name=Bgg.get_primary_name(x.get("name")),
                description=x.get("description"),
                yearpublished=x.get("yearpublished", {}).get("@value"),
                minplayers=x.get("minplayers", {}).get("@value"),
                maxplayers=x.get("maxplayers", {}).get("@value"),
                playingtime=x.get("playingtime", {}).get("@value"),
                minplaytime=x.get("minplaytime", {}).get("@value"),
                maxplaytime=x.get("maxplaytime", {}).get("@value"),
                minage=x.get("minage", {}).get("@value"),
                links=lnks,  # TODO
                marketplacelistings=marketplacelistings,
                statistics=statistics,
                comments=comments,
                poll=poll,
            )
            ret.append(item)
        return Thing(items=ret)
