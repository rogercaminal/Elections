import os, party, election


elect = election.election("Eleccions2017")

circumscriptions = []
circumscriptions.append(["Barcelona", 85])
circumscriptions.append(["Girona", 17])
circumscriptions.append(["Lleida", 15])
circumscriptions.append(["Tarragona", 18])
elect.add_circumscriptions(circumscriptions)

elect.add_party(party.party("JxCAT"))
elect.add_party(party.party("ERC"))
elect.add_party(party.party("Cs"))
elect.add_party(party.party("PSC"))
elect.add_party(party.party("CComu"))
elect.add_party(party.party("PP"))
elect.add_party(party.party("CUP"))

votes = {}
votes["JxCAT"] = {"Barcelona": 618653, "Girona":148794, "Lleida":77695, "Tarragona": 94460}
votes["ERC"]   = {"Barcelona": 673285, "Girona":88012,  "Lleida":63852, "Tarragona": 104258}
votes["Cs"]    = {"Barcelona": 862300, "Girona":79181,  "Lleida":40608, "Tarragona": 120010}
votes["PSC"]   = {"Barcelona": 494693, "Girona":34969,  "Lleida":21618, "Tarragona": 51689}
votes["CComu"] = {"Barcelona": 274565, "Girona":16349,  "Lleida":9218,  "Tarragona": 23463}
votes["PP"]    = {"Barcelona": 141803, "Girona":11476,  "Lleida":10839, "Tarragona": 19990}
votes["CUP"]   = {"Barcelona": 142195, "Girona":21551,  "Lleida":12052, "Tarragona": 17554}
elect.update_votes(votes)

elect.run_dHondt(debug=False)
result_dHondt = str(elect)

elect.reset()

elect.run_FractionCircumscriptions(debug=False)
result_FractionCircumscriptions = str(elect)

elect.reset()

elect.run_FractionAll(debug=False)
result_FractionAll = str(elect)

elect.printCircumscriptions = False

print result_dHondt
print result_FractionCircumscriptions
print result_FractionAll
