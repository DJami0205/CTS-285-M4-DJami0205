class SetFull(Exception):
    pass


class MemoryBank:
    def __init__(self):
        self.members = []

    def add_problem(self, problem_id):
        if problem_id not in self.members:
            if len(self.members) >= 10:
                raise SetFull("A Memory Bank set holds up to 10 problems.")
            self.members.append(problem_id)