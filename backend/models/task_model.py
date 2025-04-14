class Task:
    def __init__(self, ID_TASK, TASK_TITLE, TASK_DESC, TASK_IS_DONE=False):
        self.ID_TASK = ID_TASK
        self.TASK_TITLE = TASK_TITLE
        self.TASK_DESC = TASK_DESC
        self.TASK_IS_DONE = TASK_IS_DONE

    def to_dict(self):
        return {
            "ID_TASK": self.ID_TASK,
            "TASK_TITLE": self.TASK_TITLE,
            "TASK_DESC": self.TASK_DESC,
            "TASK_IS_DONE": self.TASK_IS_DONE
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['ID_TASK'], data['TASK_TITLE'], data['TASK_DESC'], data['TASK_IS_DONE'])
