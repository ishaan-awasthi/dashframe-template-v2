import csv
import random
from datetime import datetime
import time

counter = 0

# Generate the data
def heart_data():
    global counter
    if counter == 0:
        return random.uniform(77.0, 83.0)
    else:
        return random.uniform(67.0, 73.0)
def spo2_data():
    return random.uniform(97.0, 100.0)


def update_heart(heart_file_path):
    global counter
    data = heart_data()

    if counter == 0:
        counter +=1
    else: counter -=1

    with open(heart_file_path, 'a', newline='') as csvfile:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        writer = csv.writer(csvfile)
        writer.writerow([current_time] + [data])
    print("Update csv file with random data: " + str(data))

def update_spo2(spo2_file_path):
    data = spo2_data()

    with open(spo2_file_path, 'a', newline='') as csvfile:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        writer = csv.writer(csvfile)
        writer.writerow([current_time] + [data])
    
    print("Updated csv file with random data: " + str(data))


def update_main(heart_file_path, spo2_file_path):
    while True:
        update_heart(heart_file_path)
        update_spo2(spo2_file_path)
        time.sleep(10)

heart_file_path = '../data/heart.csv'
spo2_file_path = '../data/spo2.csv'
update_main(heart_file_path, spo2_file_path)



