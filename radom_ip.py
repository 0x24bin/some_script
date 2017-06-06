from random import randrange
import sys
def getip(count):
    count = int(count)
    not_valid = [10,127,169,172,192]
    for i in range(0,count):
        first = randrange(1,256)
        while first in not_valid:
            first = randrange(1,256)
        ip = ".".join([str(first),str(randrange(1,256)),
        str(randrange(1,256)),str(randrange(1,256))])
        print ip

if __name__=="__main__":
    getip(sys.argv[1])
