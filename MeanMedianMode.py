import csv
def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += i
    mean = total / n
    print("Mean (Average) is -> ", mean)

def median(data):
    n = len(data)
    data.sort()
    if n%2==0:
        median1 = float(data[n//2])
        median2 = float(data[n//2-1])
        median = (median1+median2)/2
    else:
        median = float(data[n//2])
    print("Median is -> ", median)

def mode(data):
    data = Counter(newdata)
    mode_data_for_range = {
        "75-85":0,
        "85-95":0,
        "95-105":0,
        "105-115":0,
        "115-125":0,
        "125-135":0,
        "135-145":0,
        "145-155":0,
        "155-165":0,
        "165-175":0,
    }
    for height,occurance in data.items():
        if 50 < float(height) < 60:
            mode_data_for_range["50-60"]+=occurance
        elif 60 < float(height) < 70:
            mode_data_for_range["60-70"]+=occurance
        else:
            mode_data_for_range["70-80"]+=occurance
    mode_range, mode_occurence = 0,0
    for range, occurance in mode_data_for_range.items():
        if occurance > mode_occurence:
            mode_range,mode_occurence = [int (range.split("-")[0]),int (range.split("-")[1])],occurance
    mode = float((mode_range[0]+mode_range[1]))/2
    print(mode)

with open("height-weight.csv",newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
    
filedata.pop(0)

data = []
for i in range(len(filedata)):
    n_num = filedata[i][2]
    data.append(float(n_num))

mean(data)
median(data)
mode(data)