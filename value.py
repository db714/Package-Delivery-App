class Value:

    def __init__(self, pID, address, city, state, zip, deadline, weight, note):
        self.pID = pID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.note = note

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.pID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.note)


    def ReturnValue(self):

        print(self.pID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.note)

        return