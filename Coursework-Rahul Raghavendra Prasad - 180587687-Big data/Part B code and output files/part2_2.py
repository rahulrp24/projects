#from mrjob.step import MRStep

from mrjob.job import MRJob
from mrjob.step import MRStep
import time
import re
class Part2(MRJob):

    sector_table = {}

    def mapper1(self):
        # load companylist into a dictionary
        # run the job with --file input/companylist.tsv
        with open("part2_1.txt") as f:
            for line in f:
                fields = line.split(",")
                key = fields[0]
                #val = fields[3]
                self.sector_table[key]=key

    def mapper2(self, _, line):
        fields = line.split(",")
        try:
            tx_id=fields[0]
            if tx_id in self.sector_table:
                print(fields[0]+','+fields[1]+','+fields[2])
        except:
            pass


    def steps(self):
       return [MRStep(mapper_init=self.mapper1,
                       mapper=self.mapper2)]
if __name__ == '__main__':
    Part2.run()
