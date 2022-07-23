class Athlete:
    athlete_id=None
    first_name=None
    last_name=None
    height=None
    weight=None

    def __init__(self, athlete_id, first_name, last_name, height, weight):
        self.athlete_id = athlete_id
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self. weight = weight

    def __str__(self):
        return str(self.__dict__)

class Todos:
    todo_id = None
    todo_title= None
    todo_description = None
    priority = None

    def __init__(self, todo_id, todo_title, todo_description, priority, status, create_at, update_at):
        self.todo_id = todo_id
        self.todo_title = todo_title
        self.todo_description = todo_description
        self.priority = priority
        self.status = status
        self.create_at = create_at
        self.update_at = update_at

    def __str__(self):
        return str(self.__dict__)