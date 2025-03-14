class Kadam_Tur:
    def __init__(self, name, location):
        self.name = name
        self.location = location


    def func(self):
        print(f'{self.name:<20} {self.location:>5}')


class Tourist:
    def __init__(self, name, contact_num, start_date=None):
        self.name = name
        self.contact_num = contact_num
        self.start_date = start_date


    def calculate_cost(self):
        return 'You have the membership card to redeem'

