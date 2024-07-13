import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open("data1.csv",'r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[2])
plt.bar(x,y,color='g',width=0.70,label="Age")
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("Ages of different persons")
plt.legend()
plt.show()

# import matplotlib.pyplot as plt
# import csv
# x=[]
# y=[]
# with open("Student_performance_data.csv",'r') as csvfile:
#     plots=csv.reader(csvfile,delimiter=',')
#     for row in plots:
#         x.append(row[0])
#         y.append(row[13])
# plt.bar(x,y,color='g',width=0.72,label="GPA")
# plt.xlabel("Roll No.")
# plt.ylabel("Grade")
# plt.title("Student performance")
# plt.legend()
# plt.show()