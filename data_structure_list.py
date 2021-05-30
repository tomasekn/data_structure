# Zaimplementuj w języku `Python`, korzystając z filozofii TDD, listę jednokierunkową z następującymi operacjami:
# * `insert` - wstawiającą element do listy
# * `delete` - usuwającą element z listy
# * `isempty` – sprawdzającą czy lista jest pusta;
# * `findMTF` – sprawdzająca czy podany element jest na liście i w przypadku jego znalezienia przesuwający go na przód listy;
# * `findTRANS` – sprawdzająca czy podany element jest na liście i w przypadku jego znalezienia przesuwający go o jedno miejsce do przodu listy.

class Node:
    def __init__(self, reference_index, value):
        self.reference_index = reference_index
        self.value = value

    def __repr__(self):
        return f"{self.value} {self.reference_index}"


class StructureList:
    def __init__(self):
        self.last = None
        self.first = None

    def add(self, value):
        element = Node(None, value)
        if self.first is None:
            self.first = element
            self.last = element
        else:
            self.last.reference_index = element
            self.last = element

    def insert(self, value, before_value):

        if self.is_empty():
            return f"This list is empty"
        else:
            current = self.first
            while True:
                if current.reference_index == None:
                    print(f"{before_value} isn't instanced in this list")
                    break
                elif current.value == before_value:
                    element = Node(current, value)
                    self.first = element
                    break
                elif current.reference_index.value == before_value:
                    element = Node(current.reference_index, value)
                    current.reference_index = element
                    break

                # elif current.value == before_value:

                current = current.reference_index

    def findMTF(self, wanted_value_on_the_list):
        if self.is_empty():
            return f"This list is empty"
        else:
            current = self.first
            while True:
                if current.value == wanted_value_on_the_list:
                    break
                elif current.reference_index is None:
                    print(f"{wanted_value_on_the_list} isn't instanced in this list")
                    break
                elif current.reference_index.value == wanted_value_on_the_list:
                    temp = current.reference_index.reference_index
                    change = current.reference_index
                    if temp is None:
                        self.last = current
                    current.reference_index = temp
                    old_firs = self.first
                    self.first = change
                    self.first.reference_index = old_firs
                    break
                current = current.reference_index

    def findTRANS(self, wanted_value_on_the_list):
        if self.is_empty():
            return f"This list is empty"
        else:
            current = self.first
            next = self.first.reference_index
            while True:
                if self.first.value == wanted_value_on_the_list:
                    break
                elif self.first.reference_index.value == wanted_value_on_the_list:
                    # change = current.reference_index
                    current.reference_index = next.reference_index
                    next.reference_index = current
                    self.first = next
                    break
                elif next.reference_index.value == wanted_value_on_the_list:
                    change = next.reference_index
                    next.reference_index = next.reference_index.reference_index
                    if next.reference_index is None:
                        self.last = next
                    change.reference_index = next
                    current.reference_index = change

                    break
                current = next
                next = next.reference_index

    def delete(self):
        element = self.first
        self.first = element.reference_index
        if self.first is None:
            self.last = None
        return element.value

    def is_empty(self):
        if self.first is None:
            return True
        return False

    def __repr__(self):
        return f"{self.first} {self.last}"


if __name__ == '__main__':
    my_list = StructureList()
    for i in range(5):
        my_list.add(i)
        print(my_list)

    my_list.insert(10, 4)
    print(my_list)
    my_list.insert(10, 0)
    print(my_list)
    my_list.insert(10, 1)
    print(my_list)
    my_list.add(100)
    print(my_list)
    for i in range(5):
        my_list.delete()
    print(my_list)
    my_list.findMTF(1)
    print()
    print(my_list)
    my_list.findMTF(100)
    print(my_list)
    my_list.findMTF(100)
    print(my_list)
    my_list.findMTF(1000)
    print(my_list)
    my_list.findTRANS(10)
    print(my_list)
