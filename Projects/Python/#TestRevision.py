#Dictionary
Chantal = {'Place':'Italy','Food':'Quesadillas','City':'Dubai'}
print("Original dictionary: ",Chantal)
del Chantal[next(iter(Chantal))]
del Chantal[next(reversed(Chantal))]
print(f"Updated dictionary: ",Chantal)