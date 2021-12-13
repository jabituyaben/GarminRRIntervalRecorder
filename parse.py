import fitparse
import pandas as pd
import sys

fitfile = fitparse.FitFile(sys.argv[1])

#fitfile = fitparse.FitFile("2021-12-12-16-27-48.fit")

intervals = []

for record in fitfile.get_messages("record"):
    for data in record:
        if data.name == "RR":
            intervalArray = data.value
            for x in intervalArray:
                if x is not None:
                    intervals.append(x)

df = pd.DataFrame(intervals)
df.to_csv('RR.csv', index=False, header=False)

print("interval count ", len(intervals))
