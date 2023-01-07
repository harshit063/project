POPULATION SIZ = 9
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
class Population:
    def __init__(self,size):
        # size of the population
        self._size=size
        self._data=data
        # population schedule
        self._schedules =[]
        for i in range(0,size):self._schedules.append(Schedule().initialize())
    def get_schedules(self): return self._schedules()
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
class DisplayMgr:
    def print_available_data(self):
            print(">All available Data")
            self.print_dept()
            self.print_course()
            self._print_room()
            self.print_instructor()
            self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0,len(courses)-1):
                tempStr += courses[j].__str__()+","
            tempStr += courses[len(courses)-1].__str__()+"]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(),tempStr])
        print(availableDeptsTable)
    def print_course(self):
        availableCourseTable = prettytable.PrettyTable(['id', 'courses#','max# of students','instructor'])
        courses = data.get_courses()
        for i in range(0,len(courses)):
            instructors = courses[i].get_instructor()
            tempStr = ""
            for j in range(0,len(instructors)-1):
                tempStr +=instructors[j].__str__()+","
            tempStr += instructors[len(instructors)-1].__str__()
            availableCourseTable.add_row([courses[i].get_number(),courses[i].get_name(),str(courses[i].get_maxNumOfStudents()),tempStr])
        print(availableCourseTable)
    def print_instructor(self):
        availableInstructorTable = prettytable.PrettyTable(['id','instructor'])
        instructors = data.get_instructors()
        for i in range (0,len(instructors)):
            availableInstructorTable.add_row([instructors[i].get_id(),instructors[i].get_name()])
        print(availableInstructorTable)
    def print_room(self):
        availableRoomsTable= prettytable.PrettyTable(['room#','max seating capacity'])
        rooms = data.get_rooms()
        for i in range (0,len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].het_number()),str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)
    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(['id','Meeting Time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(0,len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].get_id(),meetingTimes[i].get_time()])
        print(availableMeetingTimeTable)
    def print_generation(self):
        table1 = prettytable.PrettyTable(['schedule','fitness','# of conflicts','classes[dept,classroom,instructor'])
        schedules = population.get_schedules()
        for i in range(0,len(schedules)):
            table1.add_row([str(i),round(schedules[i].get_fitness(),3),schedules[i].get_numbOfConflicts(),schedules[i]])
        print(table1)
    def print_schedule_as_table(self,schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(['Class#','Dept','Course(max# of students)','Room(capacity)','instructor'])
        for i in range (0,len(classes)):
            table.add_row(str(i),classes[i].get_dept().get_name(),classes[i].get_course().get_name()+"("+
                          classes[i].get_course().get_number()+","+
                          str(classes[i].get_courses().get_maxNumbOfStudents())+")",
                          classes[i].get_room().get_number()+"("str(classes[i].get_room().get_seatinCapacity())+")",
                          classes[i].get_instructors().get_name()+"("+str(classes[i].get_instructor().get_id())+")",
                          classes[i].get_meetingTime().get_time()+"("+str(classes[i].get_meetingTime().get-id())+")")
        print(table)

data = Data()
displayMgr= DisplayMgr()
displayMgr.print_available_data()
generationNumber =0
print("\n> Generation #"+str(generationNumber))
population = Population(POPULATION SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])