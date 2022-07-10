class Car(object):
    def __init__(self,model,color,company):
        self.color=color
        self.company=company
        self.model=model

    def start(self):
        print('started')