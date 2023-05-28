#Tektronix 2430 Star Wars opening crawl
#you need a National Instrumente GPIB adapter and cable
#ni-488, ni-visa installed

import pyvisa
import time
rm = pyvisa.ResourceManager()
#print(rm.list_resources())
#Check instrument adress
my_instrument = rm.open_resource('GPIB0::2::INSTR')
for x in range(16, 0, -1):
  
  command = 'message ' + str(x) + ':"                                        "'
  #print(command)
  my_instrument.write(command)
space = '                                        '
#print(len(space))
punto = 16
#            "                                        "
sentences = ['A long time ago, in a galaxy',
             'far, far away...',
             '',
             'It is a period of civil war.',
             'Rebel spaceships, striking',
             'from a hidden base, have won',
             'their first victory against',
             'the evil Galactic Empire.',
             '',
             'During the battle, Rebel',
             'spies managed to steal secret',
             'plans to the Empire\'s.',
             'ultimate weapon, the DEATH',
             'STAR, an armored space',
             'station with enough power to',
             'destroy an entire planet.',
             '',
             'Pursued by the Empire\'s',
             'sinister agents, Princess',
             'Leia races home aboard her',
             'starship, custodian of the',
             'stolen plans that can save',
             'her people and restore',
             'freedom to the galaxy....'
             ]
  
lines = [" "] * 16
#print(len(sentences[0]))

line = 15
for y in range (0, punto):
    finale = ' ' * (len(space) - (len(sentences[y])))
    lines[line] = sentences[y] + finale
    for x in range (0, len(sentences[y])+1):
        command = 'message ' + str(line+1) +':"' + sentences[y][0:x] + finale + '"'
        my_instrument.write(command)
        time.sleep(.08)
    line-=1
#                    "                                        "
#                      

while punto < len(sentences):

    for t in range(15,0,-1):
        #print(t)
        lines[t] = lines[t-1]
        command = 'message ' + str(t+1) +':"' + lines[t] + '"'
        my_instrument.write(command)

    command = 'message 1:"                                        "'
    my_instrument.write(command)
    #punto+=1
    finale = ' ' * (len(space) - (len(sentences[punto])))
    lines[0] = sentences[punto] + finale
    for x in range (0, len(sentences[punto])):
        command = 'message 1:"' + sentences[punto][0:x] + finale + '"'
        my_instrument.write(command)
        time.sleep(.08)
    punto+=1


input("Press Enter to continue...")
quit()
