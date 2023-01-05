class Data:
    # R1 = 207 , R2 = 208 , R3 = 205 , R4 = 110
    ROOMS = [["R1", 100], ["R2", 100], ["R3", 100], ["R4", 100]]
class Schedule:
    def __init__(self):
        self._data=data
        self._classes=[]
        self._numbOfConflicts=0
        self._fitness=-1
        self._classNumb=0
        self._isFitnessChanged=True
    def get_classes(self):
        self._isFitnessChanged=True
        return self._classes
    def get_numOfConflicts(self): return self._numbOfConflicts
    def get_fitness(self):
        if(self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged=False
        return self._fitness
    def initialize(self):
        depts=self._data.get_depts()
        for i in range(0,len(depts)):
            courses=depts[i].get_courses()
            for j in range(0,len(courses)):
                newClass= Class(self._classNumb,depts[i],courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTime()[rnd.randrange(0,len(data.get_meetingTime()))])
                newClass.set_room(data.get_rooms()[rnd.randrange(0,len(data.get_rooms()))])
                newClass.set_instructor(courses[j].get_instructor()[rnd.randrange(0,len(courses[j].get_instructors()))])
                self._classes.append(newClass)
            return self
        def calculate_fitness(self):
            self._numbOfConflicts=0
            classes = self.get_classes()
            for i in range(0,len(classes)):
                if classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents():
                    self._numbOfConflicts += 1
                for j in range(0,len(classes)):
                    if j>=i:
                        if (classes[i].get_meetingTime()== classes[j].get_meetingTime() and
                            classes[i].get_id() != classes[j].get_id()):
                            if classes[i].get_room()==classes[j].get_room():
                                self._numbOfConflicts += 1
                            if (classes[i].get_instructor()classes[j].get_instructor()):
                                self._numbOfConflicts += 1
            return 1/(1.0 * self._numbOfConflicts + 1)
        def __str__(self):
            returnValue = ""
            for i in range(0,len(self._classes)-1):
                returnValue += str(self._classes[i])+","
            returnValue += str(self._classes[len(self._classes)-1])
            return returnValue

class Course:
    def __int__(self, number, name, instructors, maxNumbOfStudents):
        self._number=number
        self._name=name
        self._maxNumbOfStudents=maxNumbOfStudents
        self._instructors=instructors
     def get_number(self): return self.__number
     def get_name(self): return self._name
     def get_instructors(self): return self._instructors
     def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
     # two string method
     def _str_(self): return self._name

class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    def str_(self): return self._name
class Room:
    def __init__(self, number, seatingCapacity):
        self._number=number
        self.__seatingCapacity=seatingCapacity
    def get_number(self): return self._number
    def get_seatingCapacity(self): return self.__seatingCapacity
class meetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time
    def get_id(self): return self._id
    def get_time(self): return self._time
class department:
     def __init__(self, name, courses, course=None):
        self._name=name
        self._course=course
    def get_name(self): return self._name
    def get_courses(self): return self._course
class Class:
    def __init__(self,id,dept,course):
        self._id=id
        self._dept=dept
        self._instructor=None
        self._course=course
        self._meetingTime=None
        self._room=None
    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_instructor(self,instructor): self._instructor=instructor
    def set_meetingTime(self,meetingTime):self._meetingTime=meetingTime
    def set_room(self,room): self._room=room
    def __str__(self):
        return str(self._dept.get_name())+","+str(self._course.get_number())+","+\
            str(self._room.get_number())+","+str(,self._instructor.get_id())+","+str(self._meetingTime.get_id())