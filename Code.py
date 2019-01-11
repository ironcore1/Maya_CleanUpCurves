import pymel.core as pm

#get selection
currentSelectionNames = pm.ls(selection=True)[0]

#Frame Range set by animator
frameRangeMin = pm.playbackOptions(query=True,minTime=True)
frameRangeMax = pm.playbackOptions(query=True,maxTime=True)

#get all keyable controls
currentSelectKeyable = pm.listAttr(currentSelectionNames, keyable=1)

eachGraphKeyedValues = None
previous_Value = None
graphValues = []

#Go through the selected controllers graph values visible within in the channel box
for eachAttribute in currentSelectKeyable:

    #Check number of keys on each frame
    numberOfKeys = pm.keyframe(currentSelectionNames+'.'+eachAttribute, time=(frameRangeMin,frameRangeMax), query=True, keyframeCount=True)

    #EachAttributes graphs keyframe values
    eachGraphKeyedValues = pm.keyframe(currentSelectionNames+'.'+eachAttribute, time=(frameRangeMin,frameRangeMax), query=True, valueChange=True)
    print 'NOK', numberOfKeys, eachAttribute, 'value', eachGraphKeyedValues
    
    
    
    #create an enum to go through each list of the individual values
    for eNum, eachAttribute in enumerate(eachGraphKeyedValues):
        
        if eNum == 0:
            continue
        if 
        
