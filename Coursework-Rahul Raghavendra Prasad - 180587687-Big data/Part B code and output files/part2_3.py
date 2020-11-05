#from mrjob.step import MRStep

from mrjob.job import MRJob
from mrjob.step import MRStep
import time
import re
class Part2(MRJob):

    sector_table = {}

    def mapper1(self):
        with open("part2_2.txt") as f:
            for line in f:
                fields = line.split(",")
                key = fields[1]
                val = fields[2].strip()
                self.sector_table[key+val]=val

    def mapper2(self, _, line):
        fields = line.split(",")
        try:
            hash=fields[0]
            n=fields[2]
            if hash + n in self.sector_table:
                print(fields[3].strip()+','+fields[1].strip())
        except:
            pass

    def steps(self):
       return [MRStep(mapper_init=self.mapper1,
                     mapper=self.mapper2)]

if __name__ == '__main__':
    Part2.run()
