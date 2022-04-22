import csv
from collections import Counter
with open('SOCR-HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    newdata.append(float(n_num))
n=len(newdata)
total=0
for x in newdata:
    total+=x
mean=total/n
print(mean)
n=len(newdata)
newdata.sort()
if n % 2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else :
    median=newdata[n//2]
print(median)
data=Counter(newdata)
mode_data_range={
    "50-60":0,
    "60-70":0,
    "70-80":0,
}
for height,occurence in data.items():
    if 50<float(height)<60:
        mode_data_range["50-60"]+=occurence
    elif 60<float(height)<70:
        mode_data_range["60-70"]+=occurence
    elif 70<float(height)<80:
        mode_data_range["70-80"]+=occurence

mode_range,mode_occurence=0,0
for range,occurence in mode_data_range.items():
    if occurence >mode_occurence:
        mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])] ,occurence

mode=float((mode_range[0]+mode_range[1])/2)
print(mode)          
