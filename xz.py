from trello import TrelloApi

api_key = "6c54798bbf5305fffb0524746c5fb908"
token = "4eee1e882c74f1578206146c8a1dd7bb512ec6c5fa85021c62f9c6383ac342b0"
trello = TrelloApi(api_key, token)
response = trello.boards.new("Created with API")
# print(response)
board_id = response['id']
for column in trello.boards.get_list(board_id):
    print(column['name'])
for column in trello.boards.get_list(board_id):
    if "Нужно" in column['name']:
        list_id = column['id']
        print(trello.lists.get_card(list_id))
card = trello.cards.new("Научится использовать Trello API", list_id)
print(card)