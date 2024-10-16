import ndspy.soundArchive
import sys
import zlib

test = ndspy.soundArchive.SDAT.fromFile(sys.argv[1])
print(test)
for bnk in test.sequences:
    if(bnk[1]):
        print("%s:%s"%(bnk[0],hex(zlib.crc32(bnk[1].eventsData))))
