from mrjob.job import MRJob
from mrjob.step import MRStep
import time
import re
class Part2(MRJob):


    def mapper(self, _, line):
        fields = line.split(",")
        key = str(fields[0])
        value=float(fields[1])
        yield(key,value)

        def reducer(self,key,value):
            sorted_values = sorted(value,reverse=True,key=lambda x: x[1])[:10]
            a=0
            for i in sorted_values:
                x=sum(sorted_values)

                yield(x,'{}-{}'.format(str(i[0]),float(i[1])))



if __name__ == '__main__':
    Part2.run()
