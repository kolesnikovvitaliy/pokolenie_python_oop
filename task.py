class TreeBuilder:
    def __init__(self):
        self.tree = []
        self.levels = {0: self.tree}
        self.level = 0

    def __enter__(self):
        print("ENTER-1",self.__dict__)
        self.level += 1
        self.knot = []
        self.tree.append(self.knot)
        self.tree = self.knot
        self.levels.setdefault(self.level, self.tree)
        print("ENTER-2",self.__dict__)
        return self

    def add(self, value):
        print("ADD-1",self.__dict__)
        self.tree.append(value)
        print("ADD-2",self.__dict__)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT-1",self.__dict__)
        self.level -= 1
        knot = self.tree
        self.tree = self.levels[self.level]
        if not knot:
            self.tree.remove(knot)
        del self.levels[self.level + 1]
        print("EXIT-2",self.__dict__)

    def structure(self):
        return self.levels[0]


tree = TreeBuilder()

tree.add(0)
print(tree.structure())

with tree:
    tree.add(1)
    with tree:
        tree.add(2)
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        pass

print(tree.structure())

with tree:
    tree.add(5)
    with tree:
        tree.add(6)
    with tree:
        tree.add(7)
        with tree:
            tree.add(8)

print(tree.structure())