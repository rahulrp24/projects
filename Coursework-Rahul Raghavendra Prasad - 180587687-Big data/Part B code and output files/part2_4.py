#from mrjob.step import MRStep

from mrjob.job import MRJob
from mrjob.step import MRStep
import time
import re
class Part2(MRJob):


    def mapper(self, _, line):
        fields = line.split(",")
        key = str(fields[0])
        value=float(fields[1])
        yield(1,(key,value))

    def reducer(self,key,value):
        sorted_values = sorted(value,reverse=True,key=lambda x: x[1])[:10]
        count=0
        for i in sorted_values:
            count+=1
            yield(count,'{}-{}'.format(str(i[0]),float(i[1])))



if __name__ == '__main__':
    Part2.run()
