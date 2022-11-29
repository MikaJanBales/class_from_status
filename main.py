class TreeStore:
    def __init__(self, items_task):
        self.items_task = items_task
        self.items_full = self.__create_items_full()
        self.parents_answer = []

    def __create_items_full(self):
        items_full = dict()
        for item in self.items_task:
            items_full[item["id"]] = {}
            items_full[item["id"]]["parent"] = item["parent"]
            if "type" in item:
                items_full[item["id"]]["type"] = item["type"]
            items_full[item["id"]]["children"] = []
            if item["parent"] != "root":
                items_full[item["parent"]]["children"].append(item["id"])
            # self.items_full[item['id']]['item_list_index'] = item['id'] - 1
        return items_full

    def __formater(self, list_before):
        answer = []
        for elem_list_before in list_before:
            answer.append(self.items_task[elem_list_before - 1])
        return answer

    def getAll(self):
        return self.items_task

    def getItem(self, id_elem):
        item_answer = {}
        item_answer["id"] = id_elem
        item_answer["parent"] = self.items_full[id_elem]["parent"]
        if "type" in self.items_full[id_elem]:
            item_answer["type"] = self.items_full[id_elem]["type"]
        return item_answer

    def getChildren(self, id_elem):
        children_answer = self.items_full[id_elem]["children"]
        return self.__formater(children_answer)

    def getAllParents(self, id_elem):
        parent = self.items_full[id_elem]['parent']
        self.parents_answer.append(self.getItem(parent))
        if parent != 'root':
            self.getAllParents(parent)
        else:
            return self.parents_answer


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
print(ts.getItem(7))
# print(ts.getChildren(4))
# print(ts.getAllParents(2))
