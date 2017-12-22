import os

class party(object):
    def __init__(self, name):
        self.name = name
        self.circumscriptionList = []
        self.votes = {}
        self.seats = {}
        self.votes_evolution = {}


#______________________________________________________________________________________
    def set_circumscriptionList(self, circumsList):
        self.circumscriptionList = circumsList
        for c in self.circumscriptionList:
            self.votes[c[0]] = 0
            self.seats[c[0]] = 0


#______________________________________________________________________________________
    def update_votes(self, votes, circums):
        self.votes[circums] = votes
        self.seats[circums] = 0
        self.votes_evolution[circums] = votes


#______________________________________________________________________________________
    def update_seats(self, seats, circums):
        self.seats[circums] = seats


#______________________________________________________________________________________
    def reset(self):
        for c in self.circumscriptionList:
            self.votes_evolution[c[0]] = 0
            self.seats[c[0]] = 0
