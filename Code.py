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


attribute_Num = []
frame_Number_Of_Same_Value = []
same_Values = []


previous_Value = None
increment = 0
lengthOfgroupChannelTimeAndValues = len(groupChannelTimeAndValues)

while increment != lengthOfgroupChannelTimeAndValues:

    for idNum , eachGroupTimeAndValue in enumerate(groupChannelTimeAndValues[increment]):

        frameNum, value =  eachGroupTimeAndValue

        currentValue = value

        if idNum == 0:

            previous_Value = currentValue
            continue

        elif previous_Value == currentValue:
            
            attribute_Num.append(increment)
            frame_Number_Of_Same_Value.append(frameNum)
            same_Values.append(currentValue)
            
        previous_Value = currentValue



    # move onto the next group of values in the list
    increment = increment + 1
    #store all values in one mega list such as the Attribute number, Frame Number and Values
    allStats = zip(attribute_Num, frame_Number_Of_Same_Value,same_Values)





#remove keys which are not needed
'''
pm.cutKey( currentSelectionNames, time=(56), attribute='translateX', option="keys" )
'''

