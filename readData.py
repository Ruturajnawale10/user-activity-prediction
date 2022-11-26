#script used to read data from dataset and extract it.

x_train = []
y_train = []

for k in range(1, 10):
    path2 = "data/a0" + str(k) + "/p"
    for j in range(1, 7):
        path1 = path2 + str(j) + "/s"
        for i in range(1, 10):
            path = path1 + "0" + str(i) + ".txt"
            with open(path) as f:
                lines = f.readlines()
                for line in lines:
                    arr = line.split(",")
                    arr = [float(measurement) for measurement in arr]
                    x_train.append(arr)
                    y_train.append(k)     #end numeric appended is activity label

        for i in range(10, 61):
            path = path1 + str(i) + ".txt"
            with open(path) as f:
                lines = f.readlines()
                for line in lines:
                    arr = line.split(",")
                    arr = [float(measurement) for measurement in arr]
                    x_train.append(arr)
                    y_train.append(k)
                    
for k in range(10, 20):
    path2 = "data/a" + str(k) + "/p"
    for j in range(1, 7):
        path1 = path2 + str(j) + "/s"
        for i in range(1, 10):
            path = path1 + "0" + str(i) + ".txt"
            with open(path) as f:
                lines = f.readlines()
                for line in lines:
                    arr = line.split(",")
                    arr = [float(measurement) for measurement in arr]
                    x_train.append(arr)
                    y_train.append(k)

        for i in range(10, 61):
            path = path1 + str(i) + ".txt"
            with open(path) as f:
                lines = f.readlines()
                for line in lines:
                    arr = line.split(",")
                    arr = [float(measurement) for measurement in arr]
                    x_train.append(arr)
                    y_train.append(k)