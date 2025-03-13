C = {'place':'Italy', 'name':'Sofiat', 'food':'pizza'}
print("Original Dictionary:", C)
del C[next(iter(C))]
del C[next(reversed(C))]
print("Updated Dictionary:", C)