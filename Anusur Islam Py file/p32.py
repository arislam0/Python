studentId = {
    "101" : "Anisul Islam",
    102 : "Sita Rani Nath",
    "103" : "Elora Baura",
    "104" : "Nahidul Islam",
}
print(studentId['101'])
print(studentId.get("104"))
print(studentId.get("106","Not a valid key"))

print(studentId.get("103","Not a valid key"))
print(studentId.get(102,"Not a valid key"))


