import serial
import time
import matplotlib.pyplot as plt
import struct
import pandas as pd

arduino = serial.Serial('/dev/ttyACM0',115200);
arduino.flushInput()
arduino.flushOutput()
time.sleep(1)
error_Mea= 1
#estimate= size(measurement);        % create array for estimate values
#% e_est= size(measurement);         % create array for error in estimate values
#e_Est=size(measurement);
q=0.01
pre_est=0                         #initial estimate
pre_e_est= 0.1                       # initial error in estimate
#measurement=1.00:5000.00;
#estimate=1.00:5000.00;

estimate=[]
measurement=[]
initary=[]
extra=[]
prediction1=[]
init =0
#plt.ion()
#fig = plt.figure()
#ax1 = fig.add_subplot(1, 1, 1)

while init<1000:

    arduino.write("$")
    time.sleep(0.01)

    if arduino.inWaiting()>0:
	bytestring = '' +arduino.read()
	bytestring+= arduino.read()
	bytestring+= arduino.read()
	bytestring+= arduino.read()
        measurement.append(round(float(struct.unpack('f',bytestring)[0]),2))

        if init == 0:
		print ('awa2')
		pre_est = measurement[init]
	#print '',init,':',measurement[init]
	#if init>2:		
	#	prediction = estimate[init-1]+(estimate[init-1]-estimate[init-2])
	#	#print str(estimate[init-1]-estimate[init-2]) 
	#else:
	#	prediction = measurement[init] 


 	
	#prediction1.append(prediction)	
     
	e_est = pre_e_est+q
	estimate1=0
        kg = e_est/(e_est+error_Mea)
	dif= abs(measurement[init] - pre_est)
	if dif > 45:
		estimate1 = pre_est #+ kg * (measurement[init]-pre_est)
		print 'in if'  + str(dif)
	else:
        	estimate1 = pre_est + kg * (measurement[init]-pre_est)
	estimate.append(estimate1)
        pre_e_est = (1-kg)*e_est

        pre_est = estimate[init]
        initary.append(init)
        init += 1

	#ax1.clear()
	#plt.plot(initary,estimate,'g')
	#plt.plot(initary,measurement,'b')
	#plt.draw()
	
	


plt.plot(initary,estimate,'g')
plt.plot(initary,measurement,'b')
#plt.plot(initary,prediction1,'r')
plt.show()
#rd_data ={"measure" :measurement,"estimate" :estimate}
#df = pd.DataFrame(rd_data,columns = ["measure","estimate"])
#df.to_csv("testdata.csv")
