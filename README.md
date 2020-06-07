# bgg4py

bgg4py is a Boardgamegeek API wrapper.

<a href="https://pypi.org/project/bgg4py" target="_blank">
    <img src="https://badge.fury.io/py/bgg4py.svg" alt="Package version">
</a>

## Requirements

Python 3.7+

## Installation

```console
$ pip install bgg4py
```

## Example

### CLI

* Check Command Options
```
$ python -m bgg4py.cli
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  family-items
  forum-lists
  forums
  geeklist
  hot-items
  search
  thing
  threads
  user-collection
  users

```

* Check Subcommand Options
```
$ python -m bgg4py.cli users
Usage: cli.py users [OPTIONS]
Try 'cli.py users --help' for help.

Error: Missing option '--name'.
```

* Run!
```
$ python -m bgg4py.cli users --name hiroaqii

https://www.boardgamegeek.com/xmlapi2/user?name=hiroaqii&guilds=1&hot=1&top=1

{
    "id": 1422482,
    "name": "hiroaqii",
    "firstname": "hiro",
    "lastname": "aqii",
    "avatarlink": "N/A",
    "yearregistered": 2016,
    "lastlogin": "2020-06-06",
    "stateorprovince": "",
    "country": "",
    "webaddress": "",
    "xboxaccount": "",
    "wiiaccount": "",
    "psnaccount": "",
    "battlenetaccount": "",
    "steamaccount": "",
    "traderating": 0,
    "marketrating": 1
}
```

### Script

```Python
from bgg4py import api

ret = api.user_collection('hiroaqii')

# returns a dictionary representing the model as JSON Schem
print(ret.schema())

# output example
print(ret.item_list[0].image)
print(retret.item_list[0])
print(ret.item_list[0].status)
print(ret.item_list[0].status.lastmodified)
print("\n".join([item.name for item in ret.item_list]))

# output json
ret_json = json.dumps(ret.dict(), indent=4, ensure_ascii=False)
pritn(ret_json)


```