#Set Operations
set1={0, 1, 2, 3, 4, 5, 6, 7, 99}
set2={0, 1, 3, 5, 7, 9}
set3={0, 2, 4, 6, 8}
print("The union of three sets: ", set1.union(set2, set3))
print("The intersection of three sets: ", set1.intersection(set2, set3))
print("The difference of three sets: ", set1.difference(set2, set3))
print("The symmetric difference of three sets: ", set1.symmetric_difference(set2))