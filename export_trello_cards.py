import argparse


def uppercase_option(string):
    return string.upper()

parser = argparse.ArgumentParser(description='Export member data from Trello')
parser.add_argument('--export', dest="EXPORT_LIST_ID", type=str, help="Trello list id")
parser.add_argument('-o', dest='output_file',
                    help="Output file; default output.csv",
                    default="output.csv")
parser.add_argument('-f', '--format', dest='output_format',
                    help="Output file format; default 'CSV'",
                    choices=['CSV', 'JSON'], type=uppercase_option,
                    default='CSV')
parser.add_argument('-l','--list', action="store_true", help="Show exportable lists", default=False)

general = parser.add_argument_group('General Options')
general.add_argument('-b', dest="BOARD_ID", type=str, help="Trello Board ID")
general.add_argument('-c', '--conf', type=str, help="Config file")

args = parser.parse_args()

if __name__ == '__main__':
    from trellolib import get_members, get_lists

    BOARD_ID = args.BOARD_ID

    LISTS = get_lists(BOARD_ID)
    if args.list:
        for l in LISTS:
            print("{}: {}".format(*l))
        exit()

    # Check if the specified list id is in the lists for this board.
    def check_in_list(id):
        for l in LISTS:
            if l[0] == id:
                return True
        return False

    # Export list
    if args.EXPORT_LIST_ID:
        if check_in_list(args.EXPORT_LIST_ID):
            try:
                members = get_members(args.EXPORT_LIST_ID)
            except:
                raise

            if args.output_format == 'JSON':
                import json
                print("args.output_file", args.output_file)
                with open(args.output_file, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(members, ensure_ascii=False))

            if args.output_format == 'CSV':
                import csv
                with open(args.output_file, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(members)
