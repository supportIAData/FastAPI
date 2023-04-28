
class AddUser:
    def __init__(self, users):
        self.users = users
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if  self.count  == len(self.users):
            raise StopIteration
        
        user = self.users[ self.count ]
        self.count += 1

        return  user['name'], user['description']