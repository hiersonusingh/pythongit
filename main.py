class Employee:
    #public members : Accessible anywhere from outside class
    #protected members : Accessible within the class and sub class
    #Private members : Accessible within class 
    def __init__(self,name, salary, project):
        self.name = name  #public member
        self._salary = salary #Protected member
        self.__project = project #private member
