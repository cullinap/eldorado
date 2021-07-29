
class Line:

    num_twrs = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def add_towers(cls, total):
        cls.num_twrs = total

class Tower:

    def __init__(self, legs, body, arms):
        self.legs = legs
        self.body = body
        self.arms = arms


class DeadEnd(Tower):

    def __init__(self, legs, body, arms):
        super().__init__(legs, body, arms)


class Tanget(Tower):

    def __init__(self, legs, body, arms):
        super().__init__(legs, body, arms)

