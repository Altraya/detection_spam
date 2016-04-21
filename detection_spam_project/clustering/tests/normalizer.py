'''
Created on 1 avr. 2016

@author: Alexandre
'''
import csv



class Normalizer(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.data = []
        
        
    def load_csv(self, file):
        minArr = [0]*4
        maxArr = [0]*4
        
        rawData = open(file, 'r')
        reader = csv.reader(rawData)
        
        firstLine = True
        rowLen = 0
        
        # lecture des données
        for row in reader:
            if firstLine:
                firstLine = False
                rowLen = len(row)
            elif (len(row) == rowLen):
                self.data.append(row)
                # calcul des max et min
                for i in range(0, 4):
                    temp = float(row[i])
                    if temp < minArr[i]:
                        minArr[i] = temp
                    if temp > maxArr[i]:
                        maxArr[i] = temp
        
        # normalisation
        for row in self.data:
            for i in range(0, 4):
                row[i] = (2 * (float(row[i]) - minArr[i]) / (maxArr[i] - minArr[i])) - 1
            # 1 of N
            if row[4] == "Iris-setosa":
                del row[4]
                row.append([1, 0, 0])
            elif row[4] =="Iris-versicolor":
                del row[4]
                row.append([0, 1, 0]) 
            elif row[4] =="Iris-virginica":
                del row[4]
                row.append([0, 0, 1])
                
        return self.data
    
    
    def printDataSet(self):
        for line in self.data:
            print(line)
            
if __name__ == '__main__':
    norm = Normalizer()
    norm.load_csv("../datasets/iris.csv")
    norm.printDataSet()
        