class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None
        self.count = 0

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.head is None:
            return None

        # продвигает фронт к следующему узлу
        temp = self.head
        self.head = self.head.next_node

        # уменьшает количество узлов на 1
        self.count -= 1

        # вернуть удаленный элемент
        return temp.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ''
        elif self.count == 1:
            return f'{self.head.data}'
        elif self.count == 2:
            return f'{self.head.data}\n{self.head.next_node.data}'
        else:
            return f'{self.head.data}\n{self.head.next_node.data}\n' \
                   f'{self.head.next_node.next_node.data}'
