#-*- coding: utf-8 -*-
'''
Created on 21 april 2016

@author: Alexandre Bruyant
'''

from clustering.kmeans.kmeans_clusterer import KMeanClusterer
from clustering.tests.normalizer import Normalizer
import clustering.kmeans.kmeans_clusterer as km
from django.test import TestCase
from test.inspect_fodder import spam


class Test(TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    
    def testKMean(self):
        print("**Test KMean observation classification**")
        
        # initialization
        k = 3
        norm = Normalizer()
        datafile = "../datasets/iris.csv"
        data = norm.load_csv(datafile)
        kmeancl = KMeanClusterer(k, data)
        kmeancl.performClustering()
        
        for i in range(k):
            print("Cluster "+str(1)+": ")
            cluster = kmeancl.getCluster(i)
            mostDeviant = cluster.getMostDeviantObservations()
            for observation in mostDeviant:
                print("    "+str(km.computeDistance(observation, cluster.getCentroid())))
            
            
    