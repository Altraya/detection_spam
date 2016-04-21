# -*- coding: utf-8 -*-
'''
Created on 21 april 2016

@author: Alexandre Bruyant
'''

from clustering.kmeans.kmeans_clusterer import KMeanClusterer
from clustering.tests.normalizer import Normalizer
import clustering.kmeans.kmeans_clusterer as km
from django.test import TestCase
from test.inspect_fodder import spam
import math


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
            cluster = kmeancl.getCluster(i)
            percentToExtract = 10
            mostDeviant = cluster.getMostDeviantObservations(percentToExtract)
            # ensure that we got the expected number of observations
            expectedDeviants = max(math.floor(len(cluster.getObservations()) / percentToExtract), 1)
            
            self.assertTrue(len(mostDeviant) == expectedDeviants, "Expected " + str(expectedDeviants)
                                + " values, only received " + str(len(mostDeviant)))
            
            
    
