# export-trello-cards

Export cards from Trello lists

## Background
My local chapter of a social club stores membership info in Trello cards.
This allows for easier exporting lists of cards as CSV or JSON.

## Install
Create virtualenv
```
python3 -m venv my-env
```
Activate virtualenv
```
source my-env/bin/activate
```
Clone repository
```
git clone http://github.com/pipertownley/export-trello-cards && cd export-trello-cards
```
Install requirements
```
pip install -r requirements.txt
```

## Usage

```
usage: export_trello_cards.py [-h] [--export EXPORT_LIST_ID] [-o OUTPUT_FILE] [-f {CSV,JSON}] [-l]
                              [-b BOARD_ID] [-c CONF]

Export member data from Trello

optional arguments:
  -h, --help            show this help message and exit
  --export EXPORT_LIST_ID
                        Trello list id
  -o OUTPUT_FILE        Output file; default output.csv
  -f {CSV,JSON}, --format {CSV,JSON}
                        Output file format; default 'CSV'
  -l, --list            Show exportable lists

General Options:
  -b BOARD_ID           Trello Board ID
  -c CONF, --conf CONF  Config file
```

## Maintainers

[@pipertownley](https://github.com/pipertownley)

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2021 Piper Townley
