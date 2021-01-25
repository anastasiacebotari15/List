with open ('listaclasei1.txt', 'r') as f:
    a=str(f.read())
with open ('listaclasei2.txt', 'w') as f:
    f.write(str(sorted(a.split())))

