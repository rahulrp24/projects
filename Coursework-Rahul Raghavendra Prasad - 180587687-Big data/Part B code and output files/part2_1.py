#from mrjob.step import MRStep

from mrjob.job import MRJob
import re

class Part2(MRJob):
    def mapper(self, _, line):
        try:
            fields = line.split(",")
            #if (len(fields)==5):
            a=fields[3]
            if (a=='{1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v}'):
                print(fields[0]+','+fields[1]+','+fields[2]+','+a)
        except:
            pass
if __name__ == '__main__':
    Part2.run()
