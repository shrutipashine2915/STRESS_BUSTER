
from _overlapped import NULL
import pyodbc
from MESSAGES import message

class DataManagement:
    
    
    __name__ = NULL
    __email__ = NULL
    __gender__ = NULL
    __dob__ = NULL
    __contact__ = NULL
    __address__ = NULL
    __id__=NULL
    __symptoms__ =NULL
    __pnum__=NULL
    __pass__=NULL
    
    
    def get_pnum__(self):
        return self.__pnum__


    def get_pass__(self):
        return self.__pass__


    def set_pnum__(self, value):
        self.__pnum__ = value


    def set_pass__(self, value):
        self.__pass__ = value


    def del_pnum__(self):
        del self.__pnum__


    def del_pass__(self):
        del self.__pass__


   


   
    
    
    def get_symptoms__(self):
        return self.__symptoms__


    def set_symptoms__(self, value):
        self.__symptoms__ = value


    def del_symptoms__(self):
        del self.__symptoms__
    
    
    def get_id__(self):
        
        return self.__id__


    def set_id__(self, value):
        self.__id__ = value


    def del_id__(self):
        del self.__id__
    
    def get_name__(self):
        return self.__name__


    def set_name__(self, value):
        self.__name__ = value
        print(self.__name__)


    def del_name__(self):
        del self.__name__

    
    def get_email__(self):
        return self.__email__


    def set_email__(self, value):
        self.__email__ = value
        print(self.__email__)


    def del_email__(self):
        del self.__email__
    
    def get_gender__(self):
        return self.__gender__


    def get_dob__(self):
        return self.__dob__


    def get_contact__(self):
        return self.__contact__


    

    def get_address__(self):
        return self.__address__


    def set_gender__(self, value):
        self.__gender__ = value


    def set_dob__(self, value):
        self.__dob__ = value


    def set_contact__(self, value):
        self.__contact__ = value


    def set_address__(self, value):
        self.__address__ = value


    

    def del_gender__(self):
        del self.__gender__


    def del_dob__(self):
        del self.__dob__


    def del_contact__(self):
        del self.__contact__



    def del_address__(self):
        del self.__address__


    
    def storeNew(self):
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\Project\Stress_Buster\src\StressBusterDatabase.mdb;')#val=(,,,,,)
            #val=('y','y','y','y','yy','y')
            cursor=conn.cursor()
            stmt="INSERT INTO PDetails(pname,email,gender,dob,contact,address,pnum,pass,stresstype) VALUES(?,?,?,?,?,?,?,?,?)"
           
            cursor.execute(stmt,(self.get_name__(),self.get_email__(),self.get_gender__(),self.get_dob__(),self.get_contact__(),self.get_address__(),self.get_pnum__(),self.get_pass__(),0))
            print("Successfully Store the Values")
            
            cursor.commit()
    
    def verification(self,Mob,password):
        
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\Project\Stress_Buster\src\StressBusterDatabase.mdb;')
            cursor=conn.cursor()
            
            stmt="SELECT * FROM PDetails where contact=?"
            cursor.execute(stmt,Mob)
            
            myresult=cursor.fetchall()
            
            for row in myresult:
                print(row)
                if row[8]==password:
                    return row[0]
                else :
                    return 0
        
        
        
    def sendSms(self,name):
        
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\Project\Stress_Buster\src\StressBusterDatabase.mdb;')
            cursor=conn.cursor()
            
            stmt="SELECT * FROM PDetails where pname=?"
            cursor.execute(stmt,name)
            
            myresult=cursor.fetchall()
            num=0
            for row in myresult:
                print(row)
                if row[0]==name:
                    num=row[7]
                else :
                    return 0
                
            a=message(num,name)
            print("message Send")
            
    def updateStress(self,name,no):
        
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\Project\Stress_Buster\src\StressBusterDatabase.mdb;')
            cursor=conn.cursor()
            
            stmt="UPDATE PDetails SET stresstype=? WHERE pname=?"
            
            cursor.execute(stmt,no,name)
            print("updated")
            cursor.commit()
            return
            
    def getStressType(self,name):
        
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\Project\Stress_Buster\src\StressBusterDatabase.mdb;')
            cursor=conn.cursor()
            
            stmt="SELECT * FROM PDetails where pname=?"
            cursor.execute(stmt,name)
            
            myresult=cursor.fetchall()
             
            for row in myresult:
                if row[0]==name:
                    type=row[9]
                    
            return type
                    
            
        
    
   
