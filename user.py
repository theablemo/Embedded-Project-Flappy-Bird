class User:
    users = {}

    def __init__(self, id) -> None:
        self.id = id
        self.max_score = 0
        self.users[id] = self

    @classmethod
    def get_user_by_id(cls, id):
        print(cls.users)
        if id in cls.users.keys():
            return True, cls.users.get(id)
        else:
            return False, None
