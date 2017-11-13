class sample:
    def returnval(self):
        i=10
        return i

    def value(self):
        self.returnval()

samp = sample()
samp.value()
    
