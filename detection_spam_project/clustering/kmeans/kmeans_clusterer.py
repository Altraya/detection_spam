'''
Created on 8 avr. 2016

@author: Alexandre
'''

from random import Random
from math import sqrt

class KMeanClusterer(object):
    def __init__(self, k, data):
        self.k = k
        self.data = data
        self.clusters = []
        samples = set()
        randy = Random()
        
        for _ in range(k):
            rand = randy.randint(0, len(self.data)-1)
            while rand in samples:
                rand = randy.randint(0, len(self.data)-1)
            samples.add(rand)
        
        for _ in range(k):
            temp = samples.pop()
            self.clusters.append(Cluster(len(self.data[0]), self.data[temp]))

    def performClustering(self):
        oldCentroids = []
        for cluster in self.clusters:
            oldCentroids.append(cluster.getCentroid())
        
        self.assignment()
        self.update()
        
        newCentroids = []
        for cluster in self.clusters:
            newCentroids.append(cluster.getCentroid())

        diffs = [True]*self.getClusterNumber()
        for i in range(self.getClusterNumber()):
            diffs[i] = oldCentroids[i] == newCentroids[i]
        
        if False in diffs:
            self.performClustering()    
        
    def assignment(self):
        for cluster in self.clusters:
            cluster.resetObservations()
        for row in self.data:
            closestCluster = self.clusters[0]
            smallestDistance = self.computeDistance(row, closestCluster.getCentroid())
            for cluster in self.clusters:
                distance = self.computeDistance(row, cluster.getCentroid())
                if(distance < smallestDistance):
                    smallestDistance = distance
                    closestCluster = cluster
            closestCluster.addObservation(row)
            
    def update(self):
        length = len(self.data[0])
        for cluster in self.clusters:
            means = [0.0]*length
            observations = cluster.getObservations()
            nbObs = len(observations)
            for obs in observations:
                for i in range(length):
                    try:
                        means[i] += obs[i]
                    except TypeError:
                        pass # field not numeric
            for i in range(length):
                try:
                    means[i] = means[i]/nbObs
                except TypeError:
                    pass # same
            cluster.centroid = means
            
            
    def getClusterNumber(self):
        return self.k
    
    def getCluster(self, i):
        return self.clusters[i]
    
    def computeDistance(self, observation, centroid):
        temp = 0
        for i in range(len(observation)):
            try:
                temp += pow(observation[i] - centroid[i], 2)
            except TypeError:
                pass
        return sqrt(temp)
    
class Cluster(object):
    def __init__(self, nbDimensions, sample):
        self.nbDimensions = nbDimensions
        self.centroid = [0] * nbDimensions
        self.observations = []
        for i in range(len(sample)-1):
            self.centroid[i] = sample[i]
    def getCentroid(self):
        return self.centroid
    
    def addObservation(self, observation):
        self.observations.append(observation)
        
    def getObservations(self):
        return self.observations
    
    def resetObservations(self):
        self.observations = []