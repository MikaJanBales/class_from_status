class TreeStore:
    def __init__(self, items_task):
        self.items_task = items_task
        self.items_full = self.__create_items_full()

    def __create_items_full(self):
        items_full = dict()
        for index, item in enumerate(self.items_task):
            if not items_full.get(item['id']):
                items_full[item['id']] = {
                    'parent': item['parent'],
                    'children': [],
                    'item_list_index': index,
                }
            else:
                items_full[item['id']].update(
                    {
                        'parent': item['parent'],
                        'item_list_index': index,
                    }
                )

            if item['parent'] != 'root':
                if items_full.get(item['parent']):
                    (
                        items_full[item['parent']]['children']
                        .append(item['id'])
                    )
                else:
                    items_full[item['parent']] = {
                        'children': [item['id']]
                    }
        return items_full

    def getAll(self):
        return self.items_task

    def getItem(self, id_elem):
        try:
            item_list_index = self.items_full[id_elem]['item_list_index']
            return self.items_task[item_list_index]
        except KeyError:
            return 'Not Found'

    def getChildren(self, id_elem):
        try:
            result = []
            children = self.items_full[id_elem]['children']
            for child in children:
                child_index = self.items_full[child]['item_list_index']
                result.append(self.items_task[child_index])
            return result
        except KeyError:
            return 'Not Found'

    def getAllParents(self, id_elem):
        try:
            parents_answer = []
            while self.items_full[id_elem]['parent'] != 'root':
                parent = self.items_full[id_elem]['parent']
                parent_index = self.items_full[parent]['item_list_index']
                parents_answer.append(self.items_task[parent_index])
                id_elem = parent
            return parents_answer
        except KeyError:
            return 'Not Found'


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

# print(ts.getAll())
# print(ts.getItem(7))
# print(ts.getChildren(2))
# print(ts.getAllParents(7))
