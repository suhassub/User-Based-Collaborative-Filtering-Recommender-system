__author__ = 'suhas subramanya'

import sys
import math
import operator
import re

userRating={}
averagerating={}
def collabFilterMain():
    filename="C:\Users\\vatsa\PycharmProjects\Assignment3\\ratings-dataset.tsv"
    '''sys.argv[1]'''
    fil = open(filename, 'r')
    predictuser="\'Kluver\'"
    predictuser=re.sub('\'','',predictuser)
    '''sys.argv[2]'''
    predictmovie="The Fugitive"
    '''sys.argv[3]'''
    KNN=10
    '''int(sys.argv[4])'''
    validRatingTable=createValidRatingtable()
    for line in fil:
        splitrating=line.split("\t")
        if userRating.__contains__(splitrating[0]):
            movie=userRating.get(splitrating[0])
            splitrating[2]=re.sub('\n','',splitrating[2])
            movie[splitrating[2]]=splitrating[1]
            userRating[splitrating[0]]=movie
        else:
            movie={}
            movie[splitrating[2]]=splitrating[1]
            userRating[splitrating[0]]=movie
    k_nearest_neighbours=K_nearest_neighbours(predictuser,KNN)
    listofneighbours=[k for k, v in sorted(k_nearest_neighbours.iteritems(), key=lambda(k, v): (-v, k))]
    for i in range(0,KNN):
        key=listofneighbours[i]
        value=k_nearest_neighbours.get(key)
        print key +' '+str(value)
    prediction=Predict(predictuser,predictmovie,k_nearest_neighbours)
    print prediction



def pearson_correlation(user1,user2):
    user1Ratings=userRating.get(user1)
    user2Ratings=userRating.get(user2)
    numerator=0
    firstdenominator=0
    seconddenominator=0
    for eachRatingOfUser1 in user1Ratings.iteritems():
        if user2Ratings.__contains__(eachRatingOfUser1[0]):
            eachRatingOfUser2=user2Ratings.get(eachRatingOfUser1[0])
            numerator+=(float(eachRatingOfUser1[1])-averagerating.get(user1)) * (float(eachRatingOfUser2)-averagerating.get(user2))
            firstdenominator+=math.pow(float(eachRatingOfUser1[1])-averagerating.get(user1),2)
            seconddenominator+=math.pow(float(eachRatingOfUser2)-averagerating.get(user2),2)
    if firstdenominator==0 and seconddenominator==0:
        finalrating=0
    else:
        finalrating=numerator/(math.sqrt(firstdenominator) * math.sqrt(seconddenominator)*1.0)
    return finalrating


def K_nearest_neighbours(user1,knn):
    similaritytable={}
    knearestneighbours={}
    calculateaveragerating()
    for eachuser in userRating.iteritems():
        if eachuser[0]!=user1:
            finalrating=pearson_correlation(user1,eachuser[0])
            similaritytable[eachuser[0]]=finalrating
    listofneighbours=[k for k, v in sorted(similaritytable.iteritems(), key=lambda(k, v): (-v, k))]
    for i in range(0,knn):
        user=listofneighbours[i]
        knearestneighbours[user]=similaritytable.get(user)
    return knearestneighbours





def calculateaveragerating():
    for eachuser in userRating.iteritems():
        count=0
        sumrating=0
        for eachuserrating in eachuser[1].iteritems():
            count+=1
            sumrating+=float(eachuserrating[1])
        avgrating=sumrating/count;
        averagerating[eachuser[0]]=avgrating


def Predict(user1,item,k_nearest_neighbours):
    corratedusers={}
    for each_similar_neighbour in k_nearest_neighbours.iteritems():
        user1_rating=userRating.get(each_similar_neighbour[0])
        if user1_rating.__contains__(item):
            corratedusers[each_similar_neighbour[0]]=each_similar_neighbour[1]

    numerator=0
    denominator=0
    for eachuser in corratedusers.iteritems():
        items=userRating.get(eachuser[0])
        itemrating=items.get(item)
        numerator+=(float(eachuser[1])*float(itemrating))
        denominator+=float(eachuser[1])
    if denominator==0:
        prediction=0
    else:
        prediction=numerator/denominator
    return prediction


def createValidRatingtable():
    validRatingTable={}
    validRatingTable[0.5]=1
    validRatingTable[1.0]=1
    validRatingTable[1.5]=1
    validRatingTable[2.0]=1
    validRatingTable[2.5]=1
    validRatingTable[3.0]=1
    validRatingTable[3.5]=1
    validRatingTable[4.0]=1
    validRatingTable[4.5]=1
    validRatingTable[5.0]=1
    return validRatingTable

collabFilterMain()
