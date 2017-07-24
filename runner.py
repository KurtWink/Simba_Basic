from getBlock import *
#f = grab()
#stdAdjustPortion(f, .10, 50)
#changeMeters(f)
#zeroDatabyTimerange("1246421700000","1246421700000",50,f)
#print(f['series'][0]['timestamps'].index(1246421700000))
#a = buildURL("blah", "blah")
#d = grab("S3VydFdpbmtlbG1hbm46a3VydHc=")
#zeroDatabyTimerangeUniform('01.07.2006 11:05:02','01.07.2011 14:05:02',d,False)
d = jqViewTest()
d['series'][0]['tags']['file-name'] = "woah"
print(d)
#print(d['series'][0]['metrics']['interval-kwh']['floatValues'])
#sampleReturn(d,.10)
#print(d['series'][0]['metrics']['interval-kwh']['floatValues'])

