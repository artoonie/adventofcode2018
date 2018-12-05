total = 0
with open('input.txt', 'r') as f:
    for line in f:
        val = int(line)
        total += val
print "Sum", total

def two():
    x = set()
    total = 0
    while True:
        with open('input.txt', 'r') as f:
            for line in f:
                val = int(line)
                total += val
                if total in x:
                    print "First frequency reached twice", total
                    return
                x.add(total)
two()
