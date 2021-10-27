import glob, csv
import matplotlib.pyplot as plt

def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:     # Construct a file object
            csv_reader = csv.reader(f) # Construct a CSV reader object
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'): # If 'line' is valid and not a header
                    data.append([int(val) for val in line])      # Append 'line' to 'data' as numbers
            all_data = all_data + data                           # Merge 'data' to 'all_data'
    return all_data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # Derive miterm, final, and total scores
    midtm_kr = [row[0] for row in class_kr]
    final_kr = [row[1] for row in class_kr]
    total_kr = [row[0]*40/125 + row[1]*60/100 for row in class_kr]
    midtm_en = [row[0] for row in class_en]
    final_en = [row[1] for row in class_en]
    total_en = [row[0]*40/125 + row[1]*60/100 for row in class_en]

    # Plot midterm/final scores as points
    plt.figure()
    plt.plot(midtm_kr, final_kr, 'r.',label = 'kr class')
    plt.plot(midtm_en,final_en,'b.',label = 'en class')
    plt.grid(True)
    plt.axis([0,125,0,100])
    plt.xlabel('midterm')
    plt.ylabel('final')
    plt.legend()
    
    # Plot total scores as a histogram
    plt.figure()
    plt.hist(total_kr,range=(0,100),bins = 20,color='r',label = 'kr class',histtype='step')
    plt.hist(total_en,range=(0,100),bins = 20,color='b',label = 'en class',histtype='bar')
    plt.xlabel('total score')
    plt.ylabel('students')
    plt.legend()

    plt.show()   
    
    


