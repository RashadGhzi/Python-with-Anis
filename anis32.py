
studentid = {
    10: "Anisul Islam",
    20: "Jakir Naik",
    30: "Jahangir Kabir"
}
studentid2 = studentid.copy()
studentid2[50] = "Harry"
studentid2[100] = "Carry on bro"
print(studentid2[50])
#print(studentid)
#print(studentid2)
del studentid2[10]
print(studentid2)
print(studentid2.get(60, "It's an invalid keyword."))
