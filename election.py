import os, operator
import party

class election(object):
    def __init__(self, name):
        self.name = name
        self.parties = {}
        self.circumscriptionsList = []

        self.printCircumscriptions = False


#______________________________________________________________________________________
    def __str__(self):
        sumseats = {}
        toprint = str(self.name) + "\n\n"
        for c,_ in self.circumscriptionsList:
            if self.printCircumscriptions:
                toprint += c + ":\n"
            for p in self.parties.keys():
                if self.printCircumscriptions:
                    toprint += "  - " + self.parties[p].name + ": " + str(self.parties[p].seats[c]) + "\n"
                if p not in sumseats.keys():
                    sumseats[p] = self.parties[p].seats[c]
                else:
                    sumseats[p] += self.parties[p].seats[c]
            if self.printCircumscriptions:
                toprint += "\n"

        toprint += "Total:\n"
        for p in self.parties.keys():
            toprint += "  - " + self.parties[p].name + ": " + str(sumseats[p]) + "\n"
        toprint += "\n"
        return str(toprint)


#______________________________________________________________________________________
    def reset(self):
        for p in self.parties.keys():
            self.parties[p].reset()


#______________________________________________________________________________________
    def add_circumscriptions(self, circumsList):
        self.circumscriptionsList = circumsList


#______________________________________________________________________________________
    def add_party(self, party):
        self.parties[party.name] = party
        self.parties[party.name].set_circumscriptionList(self.circumscriptionsList)


#______________________________________________________________________________________
    def update_votes(self, votes):
        '''
        votes is a dict {partyName: {circumscription : votes}} for a particular circumscription
        '''
        for pName in votes.keys():
            for circums in votes[pName].keys():
                self.parties[pName].update_votes(votes=votes[pName][circums], circums=circums)


#______________________________________________________________________________________
    def run_dHondt(self, debug=False):
        debugText = ""
        for c in self.circumscriptionsList:
            name = c[0]
            totalSeats = c[1]
            for i in range(totalSeats):
                if debug:
                    debugText += str("\nEsco %d\n"%(i+1))
                dict_evolution_votes = {}
                for p in self.parties.keys():
                    dict_evolution_votes[p] = self.parties[p].votes_evolution[name]
                    if debug:
                        debugText += str("%s - %d - %d\n" % (p, dict_evolution_votes[p], self.parties[p].seats[name]))
                max_party = max(dict_evolution_votes.iteritems(), key=operator.itemgetter(1))
                self.parties[max_party[0]].seats[name] = self.parties[max_party[0]].seats[name]+1
                self.parties[max_party[0]].votes_evolution[name] = self.parties[max_party[0]].votes[name]/(self.parties[max_party[0]].seats[name]+1)

                if debug:
                    debugText += str(max_party) + "\n"
                    print debugText


#______________________________________________________________________________________
    def run_FractionCircumscriptions(self, debug=False):
        debugText = ""
        for c in self.circumscriptionsList:
            name = c[0]
            totalSeats = c[1]
            sumVotesAll = 0
            for p in self.parties.keys():
                sumVotesAll += self.parties[p].votes[name]
            for p in self.parties.keys():
                self.parties[p].seats[name] = int(round(float(totalSeats)*float(self.parties[p].votes[name]/float(sumVotesAll)), 0))

