import pickle
import os

def write():
    f = open(r'c:\dfh\stu_recl.dat','wb')
    while True:
        rno = int(input('\nEnter Roll No.: '))
        name = input('Enter Name: ')
        marks = float(input('Enter Marks: '))
        data = [rno, name, marks]
        pickle.dump(data,f)
        ch = input('Do you want to enter more records (y/n): ')
        if ch.upper() in 'NO':
            break
    f.close()
    
def appendr():
    f = open(r'c:\dfh\stu_recl.dat','ab')
    while True:
        rno = int(input('Enter Roll No.: '))
        name = input('Enter Name: ')
        marks = float(input('Enter Marks: '))
        data = [rno, name, marks]
        pickle.dump(data,f)
        ch = input('Do you want to enter more records (y/n): ')
        if ch.upper() in 'NO':
            break
    f.close()
    
def read():
    try:
        f = open(r'c:\dfh\stu_recl.dat','rb')
    except IOError:
        print('File not found.')
        return
    print()
    print('+--------+-------------------------+-------+')
    obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7}{:1}'
    print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))
    print('+--------+-------------------------+-------+')
                     
    rec = 0
    while True:
        try:
            data = pickle.load(f)
            rec += 1
            rno = data[0]
            name = data[1]
            marks = data[2]
            obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
            print(obj_string.format('|',rno,'|',name,'|',marks,'|'))
        except EOFError:
            if rec == 0:
                print('|        |                         |       |')
            print('+--------+-------------------------+-------+')
            print(rec,'records found. (0.00 sec)')
            
            break
    f.close()

def srcmarks():
    try:
        f = open(r'c:\dfh\stu_recl.dat','rb')
    except IOError:
        print('File not found.')
        return
    print('+--------+-------------------------+-------+')
    obj_string = '{:1}{:8}{:1}{:^25}{:1}{:^7}{:1}'
    print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))
    print('+--------+-------------------------+-------+')
    rec = 0
    while True:
        try:
            data = pickle.load(f)
            if data[2]>60:
                rec += 1
                obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
                print(obj_string.format('|',data[0],'|',data[1],'|',data[2],'|'))
        except EOFError:
            print('+--------+-------------------------+-------+')
            if rec == 0:
                print('0 records found. (0.00 sec)')
            elif rec == 1:
                print('1 record found. (0.01 sec)')
            else:
                print(rec,'record(s) found. (0.03 sec)')
            break
    f.close()

def search():
    f = open(r'c:\dfh\stu_recl.dat','rb')
    roll = int(input('Enter roll no. to search: '))
    rec = 0
    while True:
        try:
            data = pickle.load(f)
            if roll == data[0]:
                rec += 1
                print('\nRoll No.:',data[0])
                print('Name:',data[1])
                print('Marks:',data[2])
        except EOFError:
            if rec == 0:
                print('There is no record with such roll no.')
            else:
                if rec == 0:
                    print('0 records found. (0.00 sec)')
                elif rec == 1:
                    print('1 record found. (0.01 sec)')
                else:
                    print(rec,'record(s) found. (0.02 sec)')
            break
    f.close()

def update():
    sf = open(r'c:\dfh\stu_recl.dat','rb')
    tp = open(r'c:\dfh\temp.dat','wb')
    roll = int(input('Enter roll to update: '))
    rec = 0
    while True:
        try:
            data = pickle.load(sf)
            if data[0] == roll:
                rec += 1
                print('\nRoll No.: ',data[0])
                print('Name:',data[1])
                print('Marks:',data[2])
                data[0] = int(input('Enter Roll no.: '))
                data[1] = input('Enter Name: ')
                data[2] = float(input('Enter marks: '))
            pickle.dump(data,tp)
        except EOFError:
            print(rec,'record(s) updated. (0.03 sec)')
            break
    sf.close()
    tp.close()
    os.remove(r'c:\dfh\stu_recl.dat')
    os.rename(r'c:\dfh\temp.dat',r'c:\dfh\stu_recl.dat')

def delete():
    sf = open(r'c:\dfh\stu_recl.dat','rb')
    tp = open(r'c:\dfh\temp.dat','wb')
    roll = int(input('Enter Roll No. to delete: '))
    rec = 0
    while True:
        try:
            data = pickle.load(sf)
            if data[0] == roll:
                print('\nRoll No.:',data[0])
                print('Name:',data[1])
                print('Marks:',data[2])
                ch = input('Are you sure (y/n): ')
                if ch.upper() in 'YES':
                    rec+= 1
                else:
                    pickle.dump(data,tp)             
            else:
                pickle.dump(data,tp)
        except EOFError:
            print(rec,'record(s) deleted. (0.02 sec)')
            break
    sf.close()
    tp.close()
    os.remove(r'c:\dfh\stu_recl.dat')
    os.rename(r'c:\dfh\temp.dat',r'c:\dfh\stu_recl.dat')

def sorted_data():
    try:
        f = open(r'c:\dfh\stu_recl.dat','rb')
    except IOError:
        print('File not found.')
        return
    print('+--------+-------------------------+-------+')
    obj_string = '{:1}{:8}{:1}{:^25}{:1}{:^7}{:1}'
    print(obj_string.format('|','Roll No.','|','Name','|','Marks','|',sep=''))
    print('+--------+-------------------------+-------+')
    lst_rec = []
    while True:
        try:
            data = pickle.load(f)
            d = [data[2],data[1],data[0]]
            lst_rec.append(d)
        except EOFError:
            lst_rec.sort(reverse=True)
            for i in lst_rec:
                obj_string = '{:1}{:^8}{:1}{:^25}{:1}{:^7.2f}{:1}'
                print(obj_string.format('|',i[2],'|',i[1],'|',i[0],'|'))
            print('+--------+-------------------------+-------+')
            rec = len(lst_rec)
            print(rec,'record(s) found. (0.04 sec)')
            break
    f.close()
    
while True:
    print('\n\nChoose an option from the following:')
    print('1: Write records in new file.')
    print('2: Append records in existing file.')
    print('3: Read records from a file.')
    print('4: Search records from a file.')
    print('5: Display records having marks >= 60.')
    print('6: Update records by roll number.')
    print('7: Delete records by roll number.')
    print('8: Display sorted records by Marks (DESC).')
    print('0: Exit.')
    ch  = int(input('Enter your choice: '))
    if ch == 1:
        write()
    elif ch == 2:
        appendr()
    elif ch == 3:
        read()
    elif ch == 4:
        search()
    elif ch == 5:
        srcmarks()
    elif ch == 6:
        update()
    elif ch == 7:
        delete()
    elif ch == 8:
        sorted_data()
    elif ch == 0:
        break
    else:
        print('Invalid input.')
    input('Press Enter to continue...')