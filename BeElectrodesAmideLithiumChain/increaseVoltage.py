dv = 0.025    ########## <--- set voltage increment here
fin = open('vold','r')
vo = []
for line in fin:
  vo.append(line)
# TS.Voltage 0.2 eV
fin.close()
#print vo[0]
line2 = vo[0].split('TS.Voltage')
line3 = line2[1].split('eV')
currentVOLTS = float(line3[0])
newVOLTS=currentVOLTS + dv

fout = open('VOLTAGEnew.fdf','w')
fout.write( 'TS.Voltage '  + str(newVOLTS) + " eV" + "\n")
fout.write( vo[1].strip() + "\n")
fout.write( vo[2].strip() + "\n")
fout.write( vo[3].strip() + "\n")
fout.write( vo[4].strip() + "\n")
fout.write( vo[5].strip() + "\n")
fout.write( vo[6].strip() + "\n")

fout.close()
