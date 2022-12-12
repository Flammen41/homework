###Task1
class User:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if not self.email or '@' not in self.email:
            raise ValueError('Please provide a valid email address.')
##Task2
class Boss:
    def __init__(self):
        self.name = 'Boss'
        self.company = 'Company'
        self._workers = []

    def get_workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
            worker.set_boss(self)

class Worker:
    def __init__(self):
        self._boss = None
        self.name = 'Vasya'
        self.company = 'Company'

    def get_boss(self):
        return self._boss

    def set_boss(self, boss):
        if isinstance(boss, Boss):
            self._boss = boss