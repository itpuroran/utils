import sys
import re

f_in = open('l2-n3.dat', 'r', encoding='cp1252')
f_out = open('dump.txt', 'w', encoding='cp1252')
f_out.write('ITEM: TIMESTEP\n')
f_out.write('0 \n')
f_out.write('ITEM: NUMBER OF ATOMS\n')
f_out.write('5324\n')
f_out.write('ITEM: BOX BOUNDS pp pp pp \n')
count = 0
for line in f_in:
    count += 1
    line = re.split(r'\s', line)
    if count == 1:
        lboxx, lboxy, lboxz = line[3], line[4], line[5]
        f_out.write('0.0 ' + str(lboxx) + '\n')
        f_out.write('0.0 ' + str(lboxy) + '\n')
        f_out.write('0.0 ' + str(lboxz) + '\n')
        f_out.write('ITEM: ATOMS id type x y z vx vy vz \n')
    else:
        f_out.write(line[0] + ' ' + line[1] + ' ' + line[2] +
                    ' ' + line[3] + ' ' + line[4] + ' ' + line[5] + ' ' + line[6] + ' ' + line[7] + '\n')
f_in.close()
f_out.close()
