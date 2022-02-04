import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 8) : 
    gender,race_ethnicity,parental_levelofeducation,lunch,test_preparation_course,math_score,reading_score,writing_score = datalist

    # print intermediate key-value pairs to standard output
    print(parental_levelofeducation,"\t",reading_score)

    