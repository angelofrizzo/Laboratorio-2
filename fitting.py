import csv

lst = []

with open('resistenza2/resistenza2_0.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')