#-*- coding: utf-8 -*-

'''
Created on 8 avr. 2016

@author: Alexandre
'''

from random import Random
from math import sqrt, floor


class KMeanClusterer(object):    
    def __init__(self, k, data):
        self.k = k
        self.data = data
        self.clusters = []
        self.converged = False
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
        else:
            self.converged = True
        
    def assignment(self):
        for cluster in self.clusters:
            cluster.resetObservations()
        for row in self.data:
            closestCluster = self.clusters[0]
            smallestDistance = computeDistance(row, closestCluster.getCentroid())
            for cluster in self.clusters:
                distance = computeDistance(row, cluster.getCentroid())
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

    def getMostDeviantObservations(self, n = 10):
        # computing number of observations to extract
        to_ex = 0
        if len(self.observations) < n:
            to_ex = len(self.observations)
        else:
            to_ex = n
                    
        nbObs = len(self.observations)
        nbObs2e = floor(nbObs/to_ex)
        print(str(nbObs2e)+" observations to extract.")
        
        sorted_obs = sorted(self.observations, key= lambda obs : self.distanceToCentroid(obs))
        deviants = [self.observations[n] for n in range(nbObs2e)]
        return deviants
             
    def distanceToCentroid(self, obs):
        return computeDistance(self.centroid, obs)     

def computeDistance(vector1, vector2):
    temp = 0.0
    
    v1l = len(vector1)
    v2l = len(vector2)
    if v1l != v2l:
        return -1
    
    for i in range(len(vector1)):
        try:
            temp += pow(vector1[i] - vector2[i], 2)
        except TypeError:
            pass
    return sqrt(temp)
