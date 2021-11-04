#/usr/bin/python
#honestTapir
#2/10/2017
#Challenge 1
#Paul helped me some



from __future__ import division

import matplotlib.pyplot as mplot




file = open("honestTapir_ch1.csv","r")
data = file.read()
#data = data.replace(" ", ",")

data = data.split("\n")

#:transmission time in milliseconds, signal amplitude,
#and FM radio frequency in kHz.



#we need to split the towers data up



x1=[]
y1=[]

x2=[]
y2=[]


x3 = []
y3=[]

#the transmission time is useless other than graphing frequency.
#There is no pattern to how often a ping is sent to gather information
#best bet to sort the towers is by frequences received

t1TransTime = x1
t2TransTime = x2
t1SigAmp = y1
t2SigAmp = y2

for index in range(0, len(data)):
    if len(data[index]) == 0:
        del(data[index])
        continue

  
    data[index]=data[index].split(",")
    


    data[index][2] = float(data[index][2])
    


sum = {}
count={}


for index in range(0, len(data)):
    


        
        data[index][1] = float(data[index][1])
        
        data[index][0] = float(data[index][0])
        data[index][2] = float(data[index][2])
        
        
        
              
      
        if data[index][2] == 12.464951:
            
            t1SigAmp = data[index][1]
            t1TransTime = data[index][0]
            
            
            
            
            y1.append(t1SigAmp)
            x1.append(t1TransTime)
            
            



            try:
                sum[t1TransTime] += t1SigAmp
                count1[t1TransTime] += 1
            except:
                sum[t1TransTime] = t1SigAmp
                count[t1TransTime]=1
            
                
               

"""
#else its 22.200315
        if data[index][2] == 22.200315:
                
            t2SigAmp = data[index][1]
            t2TransTime = data[index][0]

            
            y2.append(t2SigAmp)
            x2.append(t2TransTime)
            

            #try:
                #sigAmp[label2] += value2
                #count2[label2] += 1
            #except:
                
                #x2 = t2TransTime
                #y2 = value2
                #count2[label2] = 1
   """         
       
for t1TransTime,t1SigAmp in count.items():

    
    
    sum[t1TransTime] /= count[t1TransTime]

    
    if t1TransTime == 0:
        continue

    x3.append(t1TransTime)
    y3.append((sum[t1TransTime]))
              



        



s1_data = zip(x3,y3)
s1_data = sorted(s1_data)





x3,y3=zip(*s1_data)


mplot.scatter(x1,y1)
mplot.plot(x3,y3)

mplot.title("Tower 1")
mplot.xlabel("Transmission Time")
mplot.ylabel("Signal Amplitude")
mplot.show()



