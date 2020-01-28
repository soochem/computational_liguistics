# File lower case maker

f = open("AFFreal_comma_txt_원본.txt", 'r')
g = open("AFFreal_comma_lowercase.txt", 'w')

lines = f.readlines()
for line in lines:
    line = line.lower()
    #print(line)
    g.write(line)
    
f.close()
g.close()
