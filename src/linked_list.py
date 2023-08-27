class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data=None, next_node=None):
        # Set data
        self.data = data

        # устанавливает следующее поле так, чтобы оно указывало на данный узел списка
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self, head=None):
        self.head = head

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        # Создали новый узел, который хранит новые данные
        new_node = Node(data)

        # Атрибут next объекта new_node указывает на объект,
        # на который указывала переменная head
        new_node.next_node = self.head

        # Head теперь указывает на новый объект
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        # Создали новый узел, который хранит новые данные
        new_node = Node(data)

        # Если пустой список, первым становится новый объект
        if self.head is None:
            self.head = new_node

        tail = self.head
        while tail.next_node:
            tail = tail.next_node
        tail.next_node = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self):
        ll_list = []

        node = self.head
        while node:
            ll_list.append(node.data)
            node = node.next_node

        return ll_list

    def get_data_by_id(self, id_to_find):
        node = self.head
        nl = {}
        try:
            while node:
                if node.data['id'] == id_to_find:
                    nl = node.data
                node = node.next_node
            return nl

        except TypeError:
            return 'Данные не являются словарем или в словаре нет id.'


            # except TypeError:
            # try:
            #     if node.data['id'] == id_to_find:
            #         return node.data

