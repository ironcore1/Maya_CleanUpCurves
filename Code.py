import pymel.core as pm

#get selection
currentSelectionNames = pm.ls(selection=True)[0]

#Frame Range set by animator
frameRangeMin = pm.playbackOptions(query=True,minTime=True)
frameRangeMax = pm.playbackOptions(query=True,maxTime=True)

#get all keyable controls
currentSelectKeyable = pm.listAttr(currentSelectionNames, keyable=1)

eachGraphKeyedValues = None

listOfValues = []
listOfValuesTimes = []


#Go through the selected controllers graph values visible within in the channel box
for eachAttribute in currentSelectKeyable:

    #Check number of keys on each frame
    numberOfKeys = pm.keyframe(currentSelectionNames+'.'+eachAttribute, time=(frameRangeMin,frameRangeMax), query=True, keyframeCount=True)

    #EachAttributes graphs keyframe values
    eachGraphKeyedValues = pm.keyframe(currentSelectionNames+'.'+eachAttribute, time=(frameRangeMin,frameRangeMax), query=True, valueChange=True)
    #EachAttributes graphs keyframe times
    eachGraphKeyedTimes = pm.keyframe(currentSelectionNames+'.'+eachAttribute, query=True,time=(frameRangeMin,frameRangeMax))

    print 'NOK', numberOfKeys, eachAttribute, 'value', eachGraphKeyedValues

    #place all the graph values in the public variable listOfValues
    listOfValues.append(eachGraphKeyedValues)
    #place all the graph times in the public variable listOfValuesTimes
    listOfValuesTimes.append(eachGraphKeyedTimes)


zippedTimeValues = zip(listOfValuesTimes,listOfValues)

    #create an enum to go through each list of the individual values



#remove keys which are not needed
'''
pm.cutKey( currentSelectionNames, time=(56), attribute='translateX', option="keys" )
'''

