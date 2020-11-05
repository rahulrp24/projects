
from mrjob.job import MRJob
import re

class rw(MRJob):
    def mapper(self, _, line):
        try:
            fields = line.split(",")
            #if (len(fields)==5):
            a=fields[0]
            if (a == '12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw'):
                print(a+','+float(fields[1]))
        except:
            pass
if __name__ == '__main__':
    rw.run()
