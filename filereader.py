class Filereader:

    def __init__(self, mypath):
        self.path = mypath
        self.data = []

    def search(self):
        with open(f"{self.path}.txt", 'r') as f:
            data0 = f.readlines()
            for i in data0:
                numbers = i.rstrip('\n')
                if len(numbers) == 11:
                    self.data.append(numbers)
                else:
                    print('errors :' + numbers)

            return self.data
