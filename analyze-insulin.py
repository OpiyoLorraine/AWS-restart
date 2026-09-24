#manually analyzing the insulin sequence and breaking down the amino acids
sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print(len(sequence))
#characters 1 to 24
print(sequence[:24])
#the following is commented out for the next print from 24 to 54 to run
#sequence = "malwmrllpllallalwgpdpaaa"
#print(len(sequence)), confirms the number of characters in the string
#characters 25 to 54
print(sequence[24:54])
#sequence = "fvnqhlcgshlvealylvcgergffytpkt"
#print(len(sequence))
print(sequence[54:89])
#sequence = "rreaedlqvgqvelgggpgagslqplalegslqkr"
#print (len(sequence))
print(sequence[89:110])
sequence = "giveqcctsicslyqlenycn"
print(len(sequence))
