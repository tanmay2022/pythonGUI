import pickle
import csv
import matplotlib.pyplot as plt

tp_1 = open("triple_point_coordinates_3D.pkl", "rb")
overall_tp_triple = pickle.load(tp_1)

for a in range(11):
    b = overall_tp_triple[a]
    c = ['x','y','z']
    filename = ("triple_point_at time=%d.csv"%(10*a))
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(c)
        csvwriter.writerows(b)


tp_0 = open("quadrapul_point_coordinates_3D.pkl", "rb")
overall_tp_quad = pickle.load(tp_0)

for a in range(11):
    b = overall_tp_quad[a]
    c = ['x','y','z']
    filename = ("quad_point_at time=%d.csv"%(10*a))
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(c)
        csvwriter.writerows(b)