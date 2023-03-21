import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import pickle
import vtk

start = time.time()

timestep = 0.005
delta_x = 1
delta_y = 1
delta_z = 1
delta_x_sq = delta_x ** 2
delta_y_sq = delta_y ** 2
delta_z_sq = delta_z ** 2

WIDTH = 256
HEIGHT = 16
K = 3
H = 1
N = 16

def numpy_to_vtk(arr, filename):

    # create the image data

    img = vtk.vtkImageData()
    img.SetDimensions(arr.shape[1], arr.shape[0], 1)
    img.AllocateScalars(vtk.VTK_UNSIGNED_SHORT, 1)
    # copy the numpy array into the image data
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            img.SetScalarComponentFromFloat(j, i, 0, 0, arr[i, j])

    # save the image data to a vtk file

    writer = vtk.vtkXMLImageDataWriter()
    writer.SetFileName(filename)
    writer.SetInputData(img)
    writer.Write()

def configPlot(config,beta,i, N):
    X, Y = np.meshgrid(range(N), range(N))
    plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu)
    plt.title('Phase=' + str(beta) + ',' +'Time=' + str(i))
    plt.axis('tight')
    plt.show()
    # plt.savefig('Phase=' + str(beta) + ',' +'Time=' + str(i))

def configPlot_1(config,N1,N2):
    X, Y = np.meshgrid(range(N1), range(N2))
    plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu)
    # plt.title('State='+str(k)+','+'Final phase at time=%d'%i)
    plt.axis('tight')
    plt.show()
    # plt.savefig('State='+str(k)+','+'Final phase at time=%d'%i)

def configPlot_2(config,i,k, N):
    X, Y = np.meshgrid(range(N), range(N))
    plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu)
    plt.title('State='+str(k)+','+'Final modified phase at time=%d'%i)
    plt.axis('tight')
    # plt.show()
    plt.savefig('State='+str(k)+','+'Final modified phase at time=%d'%i)

CSVData = pd.read_csv("test_data.csv")
df = pd.DataFrame(CSVData)
arr = df.to_numpy()
# print(arr[46][7])

phase_list_total = [] # contains the number of phases present
set_list_total = [] # contains all the phase values
thiset_total = []
for a in range(256):
    for b in range(16):
        thiset_total.append(arr[a][b])
thiset_total = set(thiset_total)
thiset_1_total = len(thiset_total)
phase_list_total.append(thiset_1_total)
thiset_2_total = list(thiset_total)
set_list_total.append(thiset_2_total)


overall_tp_test = {}
start = time.time()
lst = []
for a in range(phase_list_total[0]):

    for j in range(256):
        for k in range(16):
            new_mat = arr.copy()
            u = set_list_total[0][a]

    for x in range(256):
        for y in range(16):
            if arr[x][y] == u:
                new_mat[x][y] = 1
            else:
                new_mat[x][y] = 0
    lst.append(new_mat)
    end = time.time() - start
    print(a,end)
    overall_tp_test[a] = new_mat

end = time.time() - start
print(end)

count = 0
for beta in range(phase_list_total[0]):
    for x1 in range(256):
        for y1 in range(16):
            count = count + lst[beta][x1][y1]

print("count = ",count)


matfile = open("matfile.pkl", "wb")
pickle.dump(overall_tp_test, matfile)
matfile.close()

time_ini = 0
overall_tp = {}
overall_tp1 = {}
overall_tp2 = {}
# updating time step
for tim in range(101):

    time_ini = time_ini + timestep
    if tim % 10 == 0:
        print(tim)
        time_taken = time.time()- start
        print("Time taken : ", time_taken)
    
    # # updating boundary condition
    # for beta in range(phase_list_total[0]):
    #     for x1 in range(256):
    #         for y1 in range(16):

    #             if y1 == 0:
    #                 lst[beta][x1][0] = lst[beta][x1][1]
                
    #             if y1 == 15:
    #                 lst[beta][x1][15] = lst[beta][x1][14]
                
    #             if x1%16 == 0:
    #                 lst[x1][y1] = lst[x1+1][y1]
                
    #             if x1%16 == 15:
    #                 lst[x1][y1] = lst[x1-1][y1]
        # lst[beta][0] = lst[beta][1]
        # lst[beta][WIDTH-1] = lst[beta][WIDTH-2]
        # lst[beta][:,0] = lst[beta][:,1]
        # lst[beta][:,HEIGHT-1] = lst[beta][:,HEIGHT-2]
# updating the new list
    new_lst = []
    for beta in range(phase_list_total[0]):
        new_lst.append(np.zeros((256,16)))
    
    lamda_lst = []
    lamda_lst.append(np.zeros((256,16)))

    lamda_lst_final = []
    lamda_lst_final.append(np.zeros((256,16)))

    # sum = 0
    # for beta in range(phase_list_total[0]):
    for x in range(16,240):
        for y in range(1,15):
            for beta in range(phase_list_total[0]):
                # print(beta)
                t_term = lst[beta][x][y]
                # sum = sum + t_term
                # if x ==57 and y==5:
                #     print(beta,t_term)

                if x%16 != 0 and x%16 != 15:
                    #along y_axis
                    row_swip = K*(lst[beta][x][y+1]+lst[beta][x][y-1] - 2*t_term)/(delta_y_sq)
                    #along x_axis
                    column_swip = K*(lst[beta][x+1][y]+lst[beta][x-1][y] - 2*t_term)/(delta_x_sq)
                    #along z_axis
                    height_swip = K*(lst[beta][x+16][y]+lst[beta][x-16][y] - 2*t_term)/(delta_z_sq)
                    #potential well term
                    func_term = 2*H*(t_term)*(t_term-1)*(2*t_term-1)
                    #final expession
                    new_lst[beta][x][y] = t_term + timestep*(row_swip+column_swip+height_swip-func_term)
                    # new_lst[beta][x][y] = t_term + timestep*(row_swip+column_swip-func_term)
                    # if x == 46 and y == 7:
                    #     print("at time",time_ini,"beta = ",beta,"value=",new_lst[beta][x][y])
    # print("sum = ", sum)
    for x in range(16,240):
        for y in range(1,15):
            for beta in range(phase_list_total[0]):
                lamda_lst[0][x][y] = lamda_lst[0][x][y]+new_lst[beta][x][y]
    
    for x in range(1,255):
        for y in range(1,15):
            for beta in range(phase_list_total[0]):
                lamda_lst[0][x][y] = lamda_lst[0][x][y]+new_lst[beta][x][y]
            
    lamda_lst_final[0] = (lamda_lst[0] -1)/phase_list_total[0]
            # print(beta , x, y, lamda_lst_final[0][x][y])
    
    for beta in range(phase_list_total[0]):
        new_lst[beta] = new_lst[beta] - lamda_lst_final[0]
        
    for x in range(16):
        for y in range(16):
            for beta in range(phase_list_total[0]):
                new_lst[beta][x][y] = lst[beta][x+16][y]
        
    for x in range(240,256):
        for y in range(16):
            for beta in range(phase_list_total[0]):
                new_lst[beta][x][y] = lst[beta][x-16][y]
        
    for x in range(16,240):
        for y in range(16):
            for beta in range(phase_list_total[0]):
                if x%16 == 0:
                    new_lst[beta][x][y] = lst[beta][x+1][y]
                if x%16 == 15:
                    new_lst[beta][x][y] = lst[beta][x-1][y]

    for x in range(256):
        for beta in range(phase_list_total[0]):
            new_lst[beta][x][0] = lst[beta][x][1]
            new_lst[beta][x][15] = lst[beta][x][14]

    # updating old list
    for beta in range(phase_list_total[0]):
        lst[beta] = new_lst[beta]
    
    if tim%10==0:
        new_mat_1 = np.zeros((256,16))
        for i in range(phase_list_total[0]):
            # print(new_mat_1[46][7])
            for x in range(256):
                for y in range(16):
                    new_mat_1[x][y] += (i)*(lst[i][x][y])

        overall_tp[tim] = new_mat_1    #updating list for a given time stamp to remove diffused regions with dominating region

        new_mat_2 = np.zeros((256,16))
        new_mat_3 = np.zeros((256,16))
        for x in range(256):
            for y in range(16):
                best = 0
                for j in range(phase_list_total[0]):
                    if lst[j][x][y]>best:
                        best = lst[j][x][y]
                        new_mat_2[x][y]= set_list_total[0][j]
                        new_mat_3[x][y]= j

        
        overall_tp1[tim] = new_mat_2 #generating matrix for timestammps without diffused regions
        overall_tp2[tim] = new_mat_3
        

# tp_file = open("tp.pkl", "wb")
# pickle.dump(overall_tp, tp_file)
# tp_file.close()

tp_file2 = open("updated matrix (mat2) with set_list_total.pkl", "wb")
pickle.dump(overall_tp1, tp_file2)
tp_file2.close()

tp_file3 = open("updated matrix (mat3) with j.pkl", "wb")
pickle.dump(overall_tp2, tp_file3)
tp_file3.close()