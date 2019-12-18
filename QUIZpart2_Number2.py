f = open('data.txt','r')
file = f.read().replace('#',"|")
data = f.read()
dataArr = data.split('#')

class Staff:
    ID : int 
    name : str
    position : str
    salary : int
    
    def __init__(self,ID,name,position,salary):
        self.ID = ID 
        self.name = name
        self.position = position
        self.salary = salary

    def new_Staff(self, ID, name,position,salary):
        newID = input("input staff ID: ")
        self.ID = "S" + newID 
        newName = input('input staff Name: ')
        self.name = newName
        newPosition = input('input staff Position: ')
        self.position = newPosition
        newSalary = int(input('input the Salary: '))
        self.salary = newSalary

choices = ['1.New Staff','2.Delete Staff','3.View Summary Data','4.Save and Exit']
for i in choices:
    print(i)

staffs = Staff((dataArr[0])),((dataArr[1])),((dataArr[2])),((dataArr[3]))
staffs_1 = Staff((dataArr[4])),((dataArr[5])),((dataArr[6])),((dataArr[7]))
staffs_2= Staff((dataArr[8])),((dataArr[9])),((dataArr[10])),((dataArr[11]))
staffs_3 = Staff((dataArr[12])),((dataArr[13])),((dataArr[14])),((dataArr[15]))
staffs_4 = Staff((dataArr[16])),((dataArr[17])),((dataArr[18])),((dataArr[19]))
staffs_5 = Staff((dataArr[20])),((dataArr[21])),((dataArr[22])),((dataArr[23]))
staffs_6= Staff((dataArr[24])),((dataArr[25])),((dataArr[26])),((dataArr[27]))
staffs_7 = Staff((dataArr[28])),((dataArr[29])),((dataArr[30])),((dataArr[31]))
staffs_8 = Staff((dataArr[32])),((dataArr[33])),((dataArr[34])),((dataArr[35]))
staffs_9 = Staff((dataArr[36])),((dataArr[37])),((dataArr[38])),((dataArr[39]))
staffs_10= Staff((dataArr[40])),((dataArr[41])),((dataArr[42])),((dataArr[43]))
STAFFS= [[staffs],[staffs_1],[staffs_2]],[staffs_3],[staffs_4],[staffs_5],[staffs_6],[staffs_7],[staffs_8],[staffs_9],[staffs_10]
print(STAFFS)
inputs_Choice = 0 
inputs_Choice = int(input('Input Choice: '))
if inputs_Choice == 1:
    newPerson = Staff()
    newPerson.new_Staff
elif inputs_Choice == 2 : 
    Chose = input("input ID: ")
    if Chose != STAFFS
        return "Data Not Found"
    else:

elif inputs_Choice == 3:
    f.read()
elif inputs_Choice ==4: 
    Print("successfully saved")