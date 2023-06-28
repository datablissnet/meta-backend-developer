class P:
    def __init__(self):
        self.a = 7


class C(P):
    pass


c = C()
print(c.a)
