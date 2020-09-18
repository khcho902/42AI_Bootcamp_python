import sys

x = sys.argv

if len(x) == 1:
    sys.exit()
elif len(x) != 2:
    res = "ERROR"
elif not x[1].isdigit():
    res = "ERROR"
elif int(x[1]) == 0:
    res = "I'm Zero."
elif int(x[1]) % 2 == 0:
    res = "I'm Even."
elif int(x[1]) % 2 != 0:
    res = "I'm Odd."

print(res)
