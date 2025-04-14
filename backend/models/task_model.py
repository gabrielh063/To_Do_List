class Task:
    def __init__(self, id, title, desc, is_done=False):
        self.id = id
        self.title = title
        self.desc = desc
        self.is_done = is_done

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "desc": self.desc,
            "is_done": self.is_done,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['title'], data['desc'], data['is_done'])
