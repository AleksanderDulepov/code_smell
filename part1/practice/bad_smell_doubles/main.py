class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def get_sorting_list(self, is_reversed=False):
        return sorted(self.lst, reverse=is_reversed)


if __name__ == "__main__":
    some_inst = SomeClass()
    print(some_inst.get_sorting_list())