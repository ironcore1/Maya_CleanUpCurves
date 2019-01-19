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


#Go through the selected controllers graph values and times visible within in the channel box and place these in variables which are manageable
for eachAttribute in currentSelectKeyable:

    #Check number of keys on each frame
    numberOfKeys = pm.keyframe(currentSelectionNames+'.'+eachAttribute, time=(frameRangeMin,frameRangeMax), query=True, keyframeCount=True)

    #EachAttributes graphs keyframe values
    eachGraphKeyedValues = pm.keyframe(currentSelectionNames+'.'+eachAttribute, time=(frameRangeMin,frameRangeMax), query=True, valueChange=True)
    #EachAttributes graphs keyframe times
    eachGraphKeyedTimes = pm.keyframe(currentSelectionNames+'.'+eachAttribute, query=True,time=(frameRangeMin,frameRangeMax))

    #print 'NOK', numberOfKeys, eachAttribute, 'value', eachGraphKeyedValues

    #place all the graph values in the public variable listOfValues
    listOfValues.append(eachGraphKeyedValues)
    #place all the graph times in the public variable listOfValuesTimes
    listOfValuesTimes.append(eachGraphKeyedTimes)



'''
Zip both the time and values together so they are more manageable to read
'''

# place both the time of each keyframes and values in the same list side by side
groupChannelTimeAndValues = []
increment = 0

# check how many channels which are aviable to the animator
channelSize = len(currentSelectKeyable)

# place both the time and values with the groupChannelTimeAndValues variable
while increment != channelSize:

    timeNValues = zip(listOfValuesTimes[increment], listOfValues[increment])
    groupChannelTimeAndValues.append(timeNValues)
    increment = increment + 1


'''
same_Values = []
previous_Value = None

for i, eachValue in enumerate(listOfValues[0]):

    current_Value = eachValue

    if i == 0:
        previous_Value = current_Value
        continue
    elif current_Value == previous_Value:
        same_Values.append(current_Value)


    previous_Value = current_Value
'''


    #create an enum to go through each list of the individual values



#remove keys which are not needed
'''
pm.cutKey( currentSelectionNames, time=(56), attribute='translateX', option="keys" )
'''

