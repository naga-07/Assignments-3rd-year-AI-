def AND(a, b):
    return all([a, b])
def OR(a, b):
    return any([a, b])
def NOT(a):
    return not a
def XNOR(a, b):
    return not (a ^ b)
def XOR(a, b):
    return a ^ b
def NOR(a, b):
    return not any([a, b])
def NAND(a, b):
    return not all([a, b])  
# Output the truth table
print("A\tB\tAND\tOR\tNOT\tXNOR\tXOR\tNOR\tNAND")
for a in [0, 1]:
    for b in [0, 1]:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(a, b, AND(a,b), OR(a,b), NOT(a), XNOR(a,b), XOR(a,b), NOR(a,b), NAND(a,b)))
