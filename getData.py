import mindwave, time

headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo', '625f')
time.sleep(2)

print headset.status
headset.connect()
print "Connecting..."

time.sleep(1)
path = './neuroData.txt'

while True:
    time.sleep(0.5)
    attention = headset.attention
    meditation = headset.meditation
    print "Attention: %s, Meditation: %s" % (headset.attention, headset.meditation)
    with open(path, 'w') as fileToWrite:
        fileToWrite.write("%s %s" % (attention, meditation))