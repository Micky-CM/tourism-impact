import csv

def read_csv(path):
    with open(path, 'r') as scvfile:
        reader = csv.reader(scvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            tourism_dict = {key: value for key, value in iterable}
            data.append(tourism_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./tourism_data.csv')
    print(data[0])