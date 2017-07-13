class zeroData(object):

    def __init__(self):
        self.name = "Zero Data"
        self.attribute = "Zeroed"

    def functionX(self, globalVarCollection):
        import time
        """

            :param start: The starting time for the range, is INCLUDED; format is '29.08.2011 11:05:02'
            :param end: The ending time for the range, is INCLUDED
            :param jObj: The jQuery collection that will be edited
            :param epo: Boolean flag seeing if data is already formatted
            :return: The zero inserted jQuery list
            """
        epo = globalVarCollection['epocCheck']
        jObj = globalVarCollection['dataSet']

        """ 
            n is the length of the arr
            x is the value to be looking for
            in a sorted time, low is element 0 while high is n-1
        """
        if jObj is None:
            raise ValueError()
        if epo is None:
            jObj['series'][0]['metrics']['interval-kwh']['floatValues'] = list(
                map(lambda x: x *0, jObj['series'][0]['metrics']['interval-kwh']['floatValues']))
        else:
            if epo:
                startEpoch = globalVarCollection['startingTimeEpoVar'].get()
                endEpoch = globalVarCollection['endingTimeEpoVar'].get()
            else:
                pattern = '%d.%m.%Y %H:%M:%S'
                startEpoch = int(
                    time.mktime(time.strptime(globalVarCollection['startingTimeStdVar'].get(), pattern))) * 1000
                endEpoch = int(
                    time.mktime(time.strptime(globalVarCollection['endingTimeStdVar'].get(), pattern))) * 1000
            if endEpoch < jObj['series'][0]['timestamps'][0] or startEpoch > jObj['series'][0]['timestamps'][
                        len(jObj['series'][0]['timestamps']) - 1]:
                raise ValueError()

            def findFirst(arr, low, high, x, n):
                if high >= low:
                    mid = int(low + (high - low) / 2)
                    if ((mid == 0 or x > float(arr[mid - 1])) and float(arr[mid]) == x):
                        return mid
                    elif (x > float(arr[mid])):
                        return findFirst(arr, (mid + 1), high, x, n)
                    else:
                        return findFirst(arr, low, (mid - 1), x, n)
                return low

            def findLast(arr, low, high, x, n):

                if high >= low:
                    mid = int(low + (high - low) / 2)
                    if ((mid == (n - 1) or x < float(arr[mid + 1])) and float(arr[mid]) == x):
                        return mid
                    elif (x < float(arr[mid])):
                        return findLast(arr, low, (mid - 1), x, n)
                    else:
                        return findLast(arr, (mid + 1), high, x, n)
                return low

            ln = len(jObj['series'][0]['timestamps'])
            timeRange2 = [x for x in range(
                findFirst(jObj['series'][0]['timestamps'], 0, ln - 1, float(startEpoch), ln),
                findLast(jObj['series'][0]['timestamps'], 0, ln - 1, float(endEpoch), ln))]

            print(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])
            for x in timeRange2:
                jObj['series'][0]['metrics']['interval-kwh']['floatValues'][x] = 0
            print(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])


