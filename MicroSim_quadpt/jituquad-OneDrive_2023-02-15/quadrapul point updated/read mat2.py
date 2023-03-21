import numpy as np
import pickle
import matplotlib.pyplot as plt

# tp_file = open("updated matrix (mat2) with set_list_total.pkl", "rb")
tp_file = open("updated matrix (mat3) with j.pkl", "rb")
data = pickle.load(tp_file)

def configPlot_1(config,N1,N2):
    X, Y = np.meshgrid(range(N1), range(N2))
    plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu)
    # plt.title('State='+str(k)+','+'Final phase at time=%d'%i)
    plt.axis('tight')
    plt.show()


'''
Below for every timestammp we generate a .pkl file containing the 3d array of the phase field 
'''

lst_0 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[0][row+x][y]
    lst_0.append(temp_mat)

tp_file_0 = open("triple_data_0.pkl", "wb")
pickle.dump(lst_0, tp_file_0)
tp_file_0.close()

lst_1 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[10][row+x][y]
    lst_1.append(temp_mat)

tp_file_1 = open("triple_data_1.pkl", "wb")
pickle.dump(lst_1, tp_file_1)
tp_file_1.close()

lst_2 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[20][row+x][y]
    lst_2.append(temp_mat)

tp_file_2 = open("triple_data_2.pkl", "wb")
pickle.dump(lst_2, tp_file_2)
tp_file_2.close()

lst_3 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[30][row+x][y]
    lst_3.append(temp_mat)

tp_file_3 = open("triple_data_3.pkl", "wb")
pickle.dump(lst_3, tp_file_3)
tp_file_3.close()

lst_4 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[40][row+x][y]
    lst_4.append(temp_mat)

tp_file_4 = open("triple_data_4.pkl", "wb")
pickle.dump(lst_4, tp_file_4)
tp_file_4.close()

lst_5 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[50][row+x][y]
    lst_5.append(temp_mat)

tp_file_5 = open("triple_data_5.pkl", "wb")
pickle.dump(lst_5, tp_file_5)
tp_file_5.close()

lst_6 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[60][row+x][y]
    lst_6.append(temp_mat)

tp_file_6 = open("triple_data_6.pkl", "wb")
pickle.dump(lst_6, tp_file_6)
tp_file_6.close()

lst_7 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[70][row+x][y]
    lst_7.append(temp_mat)

tp_file_7 = open("triple_data_7.pkl", "wb")
pickle.dump(lst_7, tp_file_7)
tp_file_7.close()

lst_8 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[80][row+x][y]
    lst_8.append(temp_mat)

tp_file_8 = open("triple_data_8.pkl", "wb")
pickle.dump(lst_8, tp_file_8)
tp_file_8.close()

lst_9 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[90][row+x][y]
    lst_9.append(temp_mat)

tp_file_9 = open("triple_data_9.pkl", "wb")
pickle.dump(lst_9, tp_file_9)
tp_file_9.close()

lst_10 = []
for i in range(16):
    temp_mat = np.zeros((16,16))
    # print(lst[i])
    row = 16*i
    for x in range(16):
        for y in range(16):
            temp_mat[x][y] = data[100][row+x][y]
    lst_10.append(temp_mat)

tp_file_10 = open("triple_data_10.pkl", "wb")
pickle.dump(lst_10, tp_file_10)
tp_file_10.close()