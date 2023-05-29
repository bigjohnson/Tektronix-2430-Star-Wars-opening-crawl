#Tektronix 2430 Star Wars opening crawl
#you need a National Instrumente GPIB adapter and cable
#ni-488, ni-visa installed

import pyvisa
import time
#ritardo = .08
ritardo = .01
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
    lunghezza = len(space) - (len(sentences[y]))
    #finale = ' ' * lunghezza
    print(sentences[y])
    print(lunghezza)
    start = lunghezza // 2
    print(start)
    end = lunghezza - start
    print(end)
    #lines[line] = sentences[y] + finale
    
    inizio = ' ' * start
    fine = ' ' * end
    lines[line] = inizio + sentences[y] + fine
    print(inizio + sentences[y] + fine)
    for x in range (0, len(sentences[y])+1):
        #command = 'message ' + str(line+1) +':"' + sentences[y][0:x] + finale + '"'
        command = 'message ' + str(line+1) +':"' + inizio + sentences[y][0:x] + fine + '"'
        my_instrument.write(command)
        time.sleep(ritardo)
    line-=1
#                    "                                        "
#                      

#while True:
#  pass

while punto < len(sentences):

    for t in range(15,0,-1):
        #print(t)
        lines[t] = lines[t-1]
        command = 'message ' + str(t+1) +':"' + lines[t] + '"'
        my_instrument.write(command)

    command = 'message 1:"                                        "'
    my_instrument.write(command)
    #punto+=1
    #finale = ' ' * (len(space) - (len(sentences[punto])))
    #lines[0] = sentences[punto] + finale
    lunghezza = len(space) - len(sentences[punto])
    start = lunghezza // 2
    end = lunghezza - start
    inizio = ' ' * start
    fine = ' ' * end
    lines[0] = inizio + sentences[punto] + fine
    for x in range (0, len(sentences[punto])):
        #command = 'message 1:"' + sentences[punto][0:x] + finale + '"'
        command = 'message 1:"' + inizio + sentences[punto][0:x] + fine + '"'
        my_instrument.write(command)
        time.sleep(ritardo)
    punto+=1


input("Press Enter to continue...")
quit()
