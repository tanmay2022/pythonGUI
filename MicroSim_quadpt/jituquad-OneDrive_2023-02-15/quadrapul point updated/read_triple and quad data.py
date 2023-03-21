import pickle
import matplotlib.pyplot as plt

tp_0 = open("triple_point_coordinates_3D.pkl", "rb")
overall_tp_triple = pickle.load(tp_0)

tp_0 = open("quadrapul_point_coordinates_3D.pkl", "rb")
overall_tp_quad = pickle.load(tp_0)

triple_point_count = []
quad_point_count = []
x_list = []
for alpha in range(11):
    x_list.append(10*alpha)
    triple_point_count.append(len(overall_tp_triple[alpha]))
    quad_point_count.append(len(overall_tp_quad[alpha]))

for i in range(11):
    print("triple point at time = ",10*i,",",triple_point_count[i])
    print("quad point at time = ",10*i,",",quad_point_count[i])

plt.scatter(x_list,triple_point_count,label="triple_point")
plt.scatter(x_list,quad_point_count,label="quad_point")
plt.xlabel('Time_stamp')
plt.ylabel('Number of points')
plt.legend()
plt.show()