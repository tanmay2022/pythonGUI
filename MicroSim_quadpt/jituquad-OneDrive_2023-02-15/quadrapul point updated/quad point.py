import numpy as np
import pickle
import matplotlib.pyplot as plt

'''
Below we import the .pkl files generated in read mat2 file.
From each file for a given timestammp we generate the number of triple and quadrapul points
'''

'''
Sample algorithim for triple and quad points


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_0[i-1][j-1][k-1])
            thisset.append(data_0[i-1][j-1][k])
            thisset.append(data_0[i-1][j][k-1])
            thisset.append(data_0[i-1][j][k])
            thisset.append(data_0[i][j-1][k-1])
            thisset.append(data_0[i][j-1][k])
            thisset.append(data_0[i][j][k-1])
            thisset.append(data_0[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:                 # For triple point
                triple_point.append((i,j,k))
            if len(thisset) >= 4:                 # For quadrapul point
                quad_point.append((i,j,k))

overall_tp_quad[0] = quad_point
overall_tp_triple[0] = triple_point


'''

tp_0 = open("triple_data_0.pkl", "rb")
data_0 = pickle.load(tp_0)

tp_1 = open("triple_data_1.pkl", "rb")
data_1 = pickle.load(tp_1)

tp_2 = open("triple_data_2.pkl", "rb")
data_2 = pickle.load(tp_2)

tp_3 = open("triple_data_3.pkl", "rb")
data_3 = pickle.load(tp_3)

tp_4 = open("triple_data_4.pkl", "rb")
data_4 = pickle.load(tp_4)

tp_5 = open("triple_data_5.pkl", "rb")
data_5 = pickle.load(tp_5)

tp_6 = open("triple_data_6.pkl", "rb")
data_6 = pickle.load(tp_6)

tp_7 = open("triple_data_7.pkl", "rb")
data_7 = pickle.load(tp_7)

tp_8 = open("triple_data_8.pkl", "rb")
data_8 = pickle.load(tp_8)

tp_9 = open("triple_data_9.pkl", "rb")
data_9 = pickle.load(tp_9)

tp_10 = open("triple_data_10.pkl", "rb")
data_10 = pickle.load(tp_10)

overall_tp_triple = {}  #list where the triple points are stored for each time stamp
overall_tp_quad = {}    #list where the quadrapul points are stored for each time stamp

thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_0[i-1][j-1][k-1])
            thisset.append(data_0[i-1][j-1][k])
            thisset.append(data_0[i-1][j][k-1])
            thisset.append(data_0[i-1][j][k])
            thisset.append(data_0[i][j-1][k-1])
            thisset.append(data_0[i][j-1][k])
            thisset.append(data_0[i][j][k-1])
            thisset.append(data_0[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[0] = quad_point
overall_tp_triple[0] = triple_point

thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_1[i-1][j-1][k-1])
            thisset.append(data_1[i-1][j-1][k])
            thisset.append(data_1[i-1][j][k-1])
            thisset.append(data_1[i-1][j][k])
            thisset.append(data_1[i][j-1][k-1])
            thisset.append(data_1[i][j-1][k])
            thisset.append(data_1[i][j][k-1])
            thisset.append(data_1[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[1] = quad_point
overall_tp_triple[1] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_2[i-1][j-1][k-1])
            thisset.append(data_2[i-1][j-1][k])
            thisset.append(data_2[i-1][j][k-1])
            thisset.append(data_2[i-1][j][k])
            thisset.append(data_2[i][j-1][k-1])
            thisset.append(data_2[i][j-1][k])
            thisset.append(data_2[i][j][k-1])
            thisset.append(data_2[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[2] = quad_point
overall_tp_triple[2] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_3[i-1][j-1][k-1])
            thisset.append(data_3[i-1][j-1][k])
            thisset.append(data_3[i-1][j][k-1])
            thisset.append(data_3[i-1][j][k])
            thisset.append(data_3[i][j-1][k-1])
            thisset.append(data_3[i][j-1][k])
            thisset.append(data_3[i][j][k-1])
            thisset.append(data_3[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[3] = quad_point
overall_tp_triple[3] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_4[i-1][j-1][k-1])
            thisset.append(data_4[i-1][j-1][k])
            thisset.append(data_4[i-1][j][k-1])
            thisset.append(data_4[i-1][j][k])
            thisset.append(data_4[i][j-1][k-1])
            thisset.append(data_4[i][j-1][k])
            thisset.append(data_4[i][j][k-1])
            thisset.append(data_4[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[4] = quad_point
overall_tp_triple[4] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_5[i-1][j-1][k-1])
            thisset.append(data_5[i-1][j-1][k])
            thisset.append(data_5[i-1][j][k-1])
            thisset.append(data_5[i-1][j][k])
            thisset.append(data_5[i][j-1][k-1])
            thisset.append(data_5[i][j-1][k])
            thisset.append(data_5[i][j][k-1])
            thisset.append(data_5[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[5] = quad_point
overall_tp_triple[5] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_6[i-1][j-1][k-1])
            thisset.append(data_6[i-1][j-1][k])
            thisset.append(data_6[i-1][j][k-1])
            thisset.append(data_6[i-1][j][k])
            thisset.append(data_6[i][j-1][k-1])
            thisset.append(data_6[i][j-1][k])
            thisset.append(data_6[i][j][k-1])
            thisset.append(data_6[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[6] = quad_point
overall_tp_triple[6] = triple_point
thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_6[i-1][j-1][k-1])
            thisset.append(data_6[i-1][j-1][k])
            thisset.append(data_6[i-1][j][k-1])
            thisset.append(data_6[i-1][j][k])
            thisset.append(data_6[i][j-1][k-1])
            thisset.append(data_6[i][j-1][k])
            thisset.append(data_6[i][j][k-1])
            thisset.append(data_6[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[6] = quad_point
overall_tp_triple[6] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_7[i-1][j-1][k-1])
            thisset.append(data_7[i-1][j-1][k])
            thisset.append(data_7[i-1][j][k-1])
            thisset.append(data_7[i-1][j][k])
            thisset.append(data_7[i][j-1][k-1])
            thisset.append(data_7[i][j-1][k])
            thisset.append(data_7[i][j][k-1])
            thisset.append(data_7[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[7] = quad_point
overall_tp_triple[7] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_8[i-1][j-1][k-1])
            thisset.append(data_8[i-1][j-1][k])
            thisset.append(data_8[i-1][j][k-1])
            thisset.append(data_8[i-1][j][k])
            thisset.append(data_8[i][j-1][k-1])
            thisset.append(data_8[i][j-1][k])
            thisset.append(data_8[i][j][k-1])
            thisset.append(data_8[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[8] = quad_point
overall_tp_triple[8] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_9[i-1][j-1][k-1])
            thisset.append(data_9[i-1][j-1][k])
            thisset.append(data_9[i-1][j][k-1])
            thisset.append(data_9[i-1][j][k])
            thisset.append(data_9[i][j-1][k-1])
            thisset.append(data_9[i][j-1][k])
            thisset.append(data_9[i][j][k-1])
            thisset.append(data_9[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[9] = quad_point
overall_tp_triple[9] = triple_point


thisset = []
triple_point = []
quad_point = []
for i in range(1,16):
    for j in range(1,16):
        for k in range(1,16):
            thisset = []
            thisset.append(data_10[i-1][j-1][k-1])
            thisset.append(data_10[i-1][j-1][k])
            thisset.append(data_10[i-1][j][k-1])
            thisset.append(data_10[i-1][j][k])
            thisset.append(data_10[i][j-1][k-1])
            thisset.append(data_10[i][j-1][k])
            thisset.append(data_10[i][j][k-1])
            thisset.append(data_10[i][j][k])
            thisset = set(thisset)

            if len(thisset) >= 3:
                triple_point.append((i,j,k))
            if len(thisset) >= 4:
                quad_point.append((i,j,k))

overall_tp_quad[10] = quad_point
overall_tp_triple[10] = triple_point

print(overall_tp_triple[10])


tp_file_triple = open("triple_point_coordinates_3D.pkl", "wb")  #storing triple point
pickle.dump(overall_tp_triple, tp_file_triple)
tp_file_triple.close()

tp_file_quad = open("quadrapul_point_coordinates_3D.pkl", "wb") #storing quadrapul point
pickle.dump(overall_tp_quad, tp_file_quad)
tp_file_quad.close()

triple_point_count = []
quad_point_count = []
x_list = []
for alpha in range(11):
    x_list.append(10*alpha)
    triple_point_count.append(len(overall_tp_triple[alpha]))
    quad_point_count.append(len(overall_tp_quad[alpha]))

plt.scatter(x_list,triple_point_count,label="triple_point")
plt.scatter(x_list,quad_point_count,label="quad_point")
plt.xlabel('Time_stamp')
plt.ylabel('Number of points')
plt.legend()
plt.show()
