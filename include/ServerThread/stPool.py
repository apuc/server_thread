class Pool:
    def __init__(self):
        self.pool = []

    def add(self, data):
        self.pool.append(data)

    def find(self, name):
        for thread in self.pool:
            if thread.id == name:
                return thread

        return None
