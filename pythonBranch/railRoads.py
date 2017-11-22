import sys
import time

class Railroads:

    def scenarios(self):
        scenario = int(raw_input("Enter scenario as you want:"))
        return scenario
    def partsOfSchedule(self,scenario):
        for count in range(1,scenario+1):
            cities=self.getCities()
            self.cit=cities
            nTrainsPerDay=self.getTrainsPerDay()
            self.cTrains=nTrainsPerDay
            boardingDetails,arrivalDetails=self.trainDescription()
            details=self.getTimDepArr()     

    def getCities(self):
        cities=[]
        nCities = int(raw_input("Enter counts of cities you wants"))
        print "Enter cities:"
        for count in range(1,nCities+1):
            city=raw_input()
            cities.append(city)
        return cities

    def getTrainsPerDay(self):
        nTrains = int(raw_input("Enter how many trains running per day:"))
        return nTrains

    def trainDescription(self):
        noTrains=self.cTrains
        boardingDetails=[]
        arrivalDetails=[]
        for perTrain in range(1,noTrains+1):
            boarding=raw_input("Enter depature time and boarding point:").split(" ")
            arrival=raw_input("Enter arrival time  arrival point:").split(" ")
            boardingDetails.append(boarding)
            arrivalDetails.append(arrival)
            self.bDetails=boardingDetails
            self.aDetails=arrivalDetails

        return  boardingDetails, arrivalDetails
        

        
    def  getTimDepArr(self):
        
        startTime=raw_input("Enter start time of jill:")
        self.sTime=startTime
        arrivalTime=raw_input("Correct time to arrival:")
        self.arrTime=arrivalTime
        boardingPoint=raw_input("Enter boarding point:")
        self.bPoint=boardingPoint
        arrivalPoint=raw_input("Enter arrival point:")
        self.arrPoint=arrivalPoint

        return startTime,arrivalTime,boardingPoint,arrivalPoint

    def selectTrainTravel(self):
        bTime=[]
        for i in range(0,len(self.bDetails)):
            for j in range(0,len(self.bDetails)):
                bTime.append(self.bDetails[i][j])
                break
        #latestTime=max(bTime)

##        aTime=[]
##        for i in range(0,len(self.aDetails)):
##            for j in range(0,len(self.aDetails)):
##                aTime.append(self.aDetails[i][j])
##                break   

            
        boardingStations=[]
        arrivalStations=[]
        latestTime=sorted(bTime)
        index=0
        for i in range(0,len(self.bDetails)):
            for ind in range(0,len(latestTime)):
                if self.bDetails[i][index]==latestTime[ind]:
                    if self.bDetails[i][index+1]==self.bPoint:
                        if self.aDetails[i][index] <= self.arrTime:
                            if self.aDetails[i][index+1]==self.arrPoint:
                                boardingStations.append(self.bDetails[i])
                                arrivalStations.append(self.aDetails[i])
                                break
                               
        self.bStations=boardingStations
        self.aStations=arrivalStations
        print "boardingStations",boardingStations
        print "arrivalStations",arrivalStations
        return  boardingStations, arrivalStations

    def displayTrainToGo(self):
        keys=[r[0] for r in self.aStations]
        count=0
        maxKey=max(keys)
        if len(keys)>1:
            if self.arrTime==maxKey:
                key=sorted(keys)[-2]
                for i in range(0,len(self.aStations)):
                    if self.aStations[i][count]==key:
                        print "The available train to go:"
                        print self.bStations[i] ,'\n',self.aStations[i]

        else:
            print "the available train to go:"
            print self.bStations ,'\n',self.aStations
                
##                for i in range(0,len(self.aStations)):
##                    if self.aStations[i][count]==maxKey:
##                        print "the available train to go:"
##                        print "sidufy",self.bStations[i] ,'\n',self.aStations[i]
            
        

if __name__ == "__main__":

    details=Railroads()
    scenario=details.scenarios()
    if isinstance(scenario, int):
        details.partsOfSchedule(scenario)

    details.selectTrainTravel()
    details.displayTrainToGo()


