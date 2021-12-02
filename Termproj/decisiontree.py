import csv

data=[]
count = 0
with open('/Users/yu/Desktop/OSS/Termproj/test.csv','r')as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            try:
                data.append([float(i) for i in line[1:3]])
            except:
                continue
f.close()

with open('/Users/yu/Desktop/OSS/Termproj/test2.csv','w') as fw:
    csv_writer = csv.writer(fw)
    for line in data:
        star = line[0]
        review = line[1]
        if star >=4.0:
            if review>=20:
                csv_writer.writerow([star,review,'A'])
            else:
                csv_writer.writerow([star,review,'B'])
        elif star >=3.0:
            if review>=30:
                csv_writer.writerow([star,review,'A'])
            else:
                csv_writer.writerow([star,review,'B'])
        else:
            csv_writer.writerow([star,review,'C'])
