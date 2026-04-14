# (1) Create List1
List1 = [10, 14, 18, 22, 26, 30]

# (2) Create HalfList1 by dividing each element by 2
HalfList1 = []
for element in List1:
    HalfList1.append(element / 2)

# (3) Convert HalfList1 to a tuple called HalfTuple1
HalfTuple1 = tuple(HalfList1)

# (4) Use pop() to remove the element at index 2 and call that HalfList2
HalfList2 = HalfList1.copy()
HalfList2.pop(2)

# (5) Convert HalfList2 to a tuple called HalfTuple2
HalfTuple2 = tuple(HalfList2)

# Print results
print("List1:", List1)
print("HalfList1:", HalfList1)
print("HalfTuple1:", HalfTuple1)
print("HalfList2:", HalfList2)
print("HalfTuple2:", HalfTuple2)