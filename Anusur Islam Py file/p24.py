subjects = ["c","c++","java","python","basic"]

print(len(subjects))

subjects.append("toc")

print(subjects)

subjects.insert(2,"os")
print(subjects)

subjects.remove("basic")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)
subjects2= subjects.copy()
print(subjects2)

pos= subjects.index("c++")
print(pos)

print(subjects.count("c++"))


subjects.clear()
print(subjects)