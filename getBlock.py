import json
import random
import time

import numpy
import requests

def jqViewTest():

    url = "https://in2lytics.gridstate.io/api/default_project/series/samples_from_phil_multispeak_ami_outage_events_20170711_tsv/data"

    querystring = {"start_time": "1474907856000", "end_time": "1474927200000"}

    headers = {
        'authorization': "Basic S3VydFdpbmtlbG1hbm46a3VydHc=",
        'cache-control': "no-cache",

    }

    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

    return json.loads(response.text)


def buildURL(project, series):
    return "https://in2lytics.gridstate.io/api/" + project + "/series/" + series + "/data"


def grab(auth):
    url = "https://in2lytics.gridstate.io/api/default_project/series/code-drop-12-test/data"

    querystring = {"start_time": "1246420800000", "end_time": "1246579200000"}

    headers = {'Authorization': 'Basic %s' % auth}

    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

    return json.loads(response.text)

def getJsonSet(auth, url):


    querystring = {"start_time": "1246420800000", "end_time": "1246579200000"}

    headers = {'Authorization': 'Basic %s' % auth}

    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

    return json.loads(response.text)


def stdAdjust(jObj, val):
    """

    :param jObj: The jQuary collection thst will be edited.
    :param val: A real number by which the standard deviation will be adjusted by.
    :return: The edited jQuary Collection to pass into the next phase.
    """
    jObj['series'][0]['metrics']['interval-kwh']['floatValues'] = list(
        map(lambda x: x + (val * numpy.std(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])),
            jObj['series'][0]['metrics']['interval-kwh']['floatValues']))
    return jObj


def stdAdjustPortion(jObj, val, portion):
    """

    :param jObj: The jQuary collection thst will be edited.
    :param val: A real number by which the standard deviation will be adjusted by.
    :param portion: Percentage of data to be edited at random
    :return: The edited jQuary Collection to pass into the next phase.
    """
    print(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])
    std = numpy.std(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])
    for n in range(0, len(jObj['series'][0]['metrics']['interval-kwh']['floatValues']) - 1):
        if float(random.random()) < (portion * .01):
            jObj['series'][0]['metrics']['interval-kwh']['floatValues'][n] = \
                jObj['series'][0]['metrics']['interval-kwh']['floatValues'][n] + (std * val)
    print(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])


def stdAdjustList(jObjList, val):
    """

    :param jObjList: The jQuary list thst will be edited.
    :param val: A real number by which the standard deviation will be adjusted by.
    :return: The edited jQuary list to pass into the next phase.
    """
    return list(map(lambda x: x + (val * numpy.std(jObjList)), jObjList))


def stdAdjustPortionList(jObj, val, portion):
    """

    :param jObj: The jQuary list thst will be edited.
    :param val: A real number by which the standard deviation will be adjusted by.
    :param portion: Percentage of data to be edited at random
    :return: The edited jQuary list to pass into the next phase.
    """
    std = numpy.std(jObj)
    for n in range(0, len(jObj) - 1):
        if float(random.random()) < (portion * .01):
            jObj[n] = jObj[n] + (std * val)
    return jObj


def changeMeters(jObj):
    """

    :param jObj: The jQuery collection that will be edited
    :return: A jQuery Collection with meter-id shuffled
    """
    random.shuffle(jObj['series'][0]['metrics']['meter-id']['stringValues'])
    return jObj


def changeMetersList(jObj):
    """

    :param jObj: The jQuery list that will be edited
    :return: A shuffled jQuary list
    """
    random.shuffle(jObj)
    return jObj


def getTotalDataRange(jObj):
    arr = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(jObj['series'][0]['timestamps'][0])) + "-" + time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(jObj['series'][0]['timestamps'][len(jObj['series'][0]['timestamps'])])),
           jObj['series'][0]['timestamps'][0] + '-' + jObj['series'][0]['timestamps'][
               len(jObj['series'][0]['timestamps'])]]


def zeroDatabyTimerangeUniform(start, end, jObj, epo):
    """

    :param start: The starting time for the range, is INCLUDED; format is '29.08.2011 11:05:02'
    :param end: The ending time for the range, is INCLUDED
    :param jObj: The jQuery collection that will be edited
    :return: The zero inserted jQuery list
    """

    """ 
        n is the length of the arr
        x is the value to be looking for
        in a sorted time, low is element 0 while high is n-1
    """
    if epo:
        startEpoch = start
        endEpoch = end
    else:
        pattern = '%d.%m.%Y %H:%M:%S'
        startEpoch = int(time.mktime(time.strptime(start, pattern))) * 1000
        endEpoch = int(time.mktime(time.strptime(end, pattern))) * 1000

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
            if ((mid ==  (n-1) or x < float(arr[mid + 1])) and float(arr[mid]) == x):
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
    return jObj


def zeroDatabyTimerange(start, end, percent, jObj):
    """

    :param start: The starting time for the range, is INCLUDED; format is '29.08.2011 11:05:02'
    :param end: The ending time for the range, is INCLUDED
    :param percent: The percentage of which the random distribution is done, '50 is 50%'
    :param jObj: The jQuery collection that will be edited
    :return: The zero inserted jQuery list
    """

    """ 
        n is the length of the arr
        x is the value to be looking for
        in a sorted time, low is element 0 while high is n-1
    """

    pattern = '%d.%m.%Y %H:%M:%S'
    startEpoch = int(time.mktime(time.strptime(start, pattern))) * 1000
    endEpoch = int(time.mktime(time.strptime(end, pattern))) * 1000

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
        c = arr[high]
        if x > float(arr[len(arr) - 1]):
            return len(arr) - 1
        elif high >= low:
            mid = int(low + (high - low) / 2)
            if ((mid == n - 1 or x < float(arr[mid + 1])) and float(arr[mid]) == x):
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
        if random.random() < (percent * .01):
            jObj['series'][0]['metrics']['interval-kwh']['floatValues'][x] = 0
    print(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])
    return jObj


def sampleReturn(jObj, val):
    jObj['series'][0]['metrics']['interval-kwh']['floatValues'] = list(
        map(lambda x: x + (val * numpy.std(jObj['series'][0]['metrics']['interval-kwh']['floatValues'])),
            jObj['series'][0]['metrics']['interval-kwh']['floatValues']))


def takeLocalFile(loc):
    try:
        file = open(loc, "r")
        return json.loads(file.read())
    except IOError:
        return -1
