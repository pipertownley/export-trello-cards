import os
from trello import TrelloApi

try:
    trello = TrelloApi(os.environ['TRELLO_KEY'], token=os.environ['TRELLO_TOKEN'])
except:
    raise


def get_lists(board_id):
    lists = trello.boards.get_list(board_id)
    return [(item['id'], item['name']) for item in lists if item['closed'] == False]

def get_cards_from_list(list_id, fields=None):
    if fields is None:
        fields = "id,name,idChecklists"
    return trello.lists.get_card(list_id, fields=fields)

# default formatter
def __format_member(member):
    if member['idChecklists'] != []:
        idchecklist = member['idChecklists'][0]
        check_items = trello.checklists.get(idchecklist, checkItem_fields="name")
        checklist_items = [member['name']]
        for item in check_items['checkItems']:
            for term in ("keybase", "email"):
                if term in item['name'].lower():
                    checklist_items.append(item['name'].split("-")[1].strip())
        return checklist_items

def get_members(member_list_id, formatter_fn=None, fields=None):
    # set default formatter
    if formatter_fn is None:
        formatter_fn = __format_member
    data = get_cards_from_list(member_list_id, fields=fields)
    members = []
    for member in data:
        member = formatter_fn(member)
        members.append(member)
    return members
