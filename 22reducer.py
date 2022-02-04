import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split("\t")
  if (len(datalist) == 2) : 
    parental_levelofeducation, reading_score = datalist

    if parental_levelofeducation != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = parental_levelofeducation 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(reading_score)

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)