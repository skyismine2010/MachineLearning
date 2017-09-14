import json
from pandas import DataFrame, Series
import pandas as pd; import numpy as np

def main():
    path = ".\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt"

    records = [json.loads(line) for line in open(path)]

    # time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    # print(type(time_zones))

    frame = DataFrame(records)
    #print(frame)
    print(frame['tz'].value_counts())


if __name__ == '__main__':
    main()

