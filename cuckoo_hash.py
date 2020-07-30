from PyInquirer import prompt
class cucko_hash:

    def __init__(self, tablesize=0):
        self.table1=[]
        self.table2=[]
        self.cycle=0
        self.cycle_check=False
        self.tabble_size=tablesize

        for i in range(self.tabble_size):
           self.table1.append("empty")
           self.table2.append("empty")
    
        

    def hash1(self,key):
        return key % self.tabble_size

    def hash2(self,key):
        return (key/self.tabble_size) % self.tabble_size

    def hash_vals(self , list):
        for s in list:
            self.insert(s,1,0)
        
    def insert(self,key ,t,count):

        if count==len(self.table1):
            print("cycle_detected")
            self.cycle_check=True
            print('rehashing........')
            self.cycle_rehash()

        collosion=True

        pos1 =  self.hash1(key)
        pos2 = int(self.hash2(key))


        if self.table1[pos1]==str(key) or self.table2[pos2]==str(key):
            return

        inserted=False
        inserted2=False

        if  t==1:

            if self.table1[pos1]=='empty':
                self.table1[pos1]=str(key)
                inserted =True
                return
            if inserted==False:
                steal =self.table1[pos1]
                self.table1[pos1]=str(key)
                self.insert(int(steal),2,count+1)
        
        
        if t==2:
            if self.table2[pos2]=='empty':
                self.table2[pos2]=str(key)
                inserted2 =True
                return

            if inserted2==False:
                stealx= self.table2[pos2]
                self.table2[pos2]=str(key)
                self.insert(int(stealx) ,1,count+1)

    def search(self,key):
        pos1=self.hash1(key)
        pos2=int(self.hash2(key))

        if self.table1[pos1]==str(key):
            print(key, 'present in tabel1 at', pos1)
            return

        if self.table2[pos2]==str(key):
            print(key, 'present in tabel2 at', pos2)
            return
        
        print('Key is not present in table')        

    def Delete(self,key):
        if self.table1[self.hash1(key)]==str(key):
            self.table1[self.hash1(key)]='empty'
            print(key , 'Deleted')
            return

        if self.table2[int(self.hash2(key))]==str(key):
            self.table2[int(self.hash2(key))]='empty'
            print(key , 'Deleted')
            return

        print("could not find" , key)


    def cycle_rehash(self):
        self.tabble_size=self.tabble_size+1
        temp=[]

        for i in self.table1:
            if i!='empty':
                temp.append(int(i))
        for i in self.table2:
            if i!='empty':
                temp.append(int(i))
        
        #  i have incread the table size by one which will in turn change the hash fucnciton  and also increase table size to cop with the returning hash 
        #  index in the array
    
        self.__init__(self.tabble_size)
      
        for i in temp:
            self.insert(i , 1, 0)

        print('-----------------')
        self.print_tables()

    def print_tables(self):
        s=''
        for i in range(len(self.table1)):
            s+=self.table1[i]
            s+=' ' 

        print('Tabel 1:' ,s)

        s2=''

        for i in range(len(self.table2)):
            s2+=self.table2[i]
            s2+=' '     

        print('Tabel 2:' , s2)


def main():
    tabel_Size=11

    # to_inserted2=[500, 20, 36, 75, 100, 3, 105, 67, 53,54,55]   # wtihout cycle    
    # to_inserted2=[20, 50, 53, 75, 100, 67,105,3,36,39,6]  # with cycle
    
    h=cucko_hash(tabel_Size)

    while 1:
        c='a) Insert \nb) Search\nc) Delete\nd) View table,\nq) Quit'
        print(c)
        questions = [
            {
                'type': 'list',
                'name': 'cho',
                'message': 'Select choice',
                'choices': ['a', 'b', 'c' ,'d' ,'q']
            }
        ]
        answer = prompt(questions)
        x=answer['cho']
        if x=='a':
            xq=input()
            h.insert(int(xq),1,0)
        elif x=='b':
            xq=input()
            h.search(int(xq))
        elif x=='c':   
            xq=input()
            h.Delete(int(xq))
        elif x=='d':   
            h.print_tables()
        elif x=='q':
            break


if __name__ == '__main__':
    main()