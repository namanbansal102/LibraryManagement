import mysql.connector
import json
conn=mysql.connector.connect(host='localhost',username='root',password='root',database='namandb')
mycursor=conn.cursor()
def insertStudentData(id,studentName,address,mobileNo,bookIssued):
        insert_data='insert into student(id,name,address,mobileNo,books) values(%s,%s,%s,%s,%s)'
        records=[
            (id,studentName,address,mobileNo,bookIssued)
        ]
        mycursor.executemany(insert_data,records)
        conn.commit()
def returnStudentBookData(stuid,booKData):
    try:
        print("The Given Book Data is",booKData,"and its type is",type(booKData))
        mycursor.execute(f'SELECT books FROM student WHERE id={stuid}')
        n=mycursor.fetchone()[0]
        print(type(n))
        n = n.strip("'")

        # Replace single quotes with double quotes
        n = n.replace("'", '"')
        p=json.loads(n)
        print("Type of P is",type(p))
        p.remove(booKData)

        
        print("The Value of P is",p)
        p=json.dumps(p)
        print("Type of P  after is",type(p))
        query = f'UPDATE student SET books = %s WHERE id = {stuid}'
        mycursor.execute(query, (p,))

        conn.commit()
    except Exception as e:
        print(e)
        print("Error In Returning The Book From Deleting The Data in Student DataBase")

def updateStudentData(stuid,booKData):
     try:
        print("The Given Book Data is",booKData,"and its type is",type(booKData))
        mycursor.execute(f'SELECT books FROM student WHERE id={stuid}')
        n=mycursor.fetchone()[0]
        print(type(n))
        n = n.strip("'")

        # Replace single quotes with double quotes
        n = n.replace("'", '"')
        p=json.loads(n)
        print("Type of P is",type(p))
        p.append(booKData)

        
        print("The Value of P is",p)
        p=json.dumps(p)
        print("Type of P  after is",type(p))
        query = f'UPDATE student SET books = %s WHERE id = {stuid}'
        mycursor.execute(query, (p,))

        conn.commit()
     except Exception as e:
        print(e)
        print("Error In Updating The Students Data")
def returnSpecifictudentData(id):
    print("Specific Student Data is Running")
    mycursor.execute(f"select * from student WHERE id={id}")
    data=mycursor.fetchall()
    # print("The Returned Data is",data)
    inf_details_ofspecificStudent=data[0][0:4]
    bookDetails_of_specificStudent=json.loads(data[0][4])
    print(bookDetails_of_specificStudent)
    print(data)
    lst=[]
    print("ads")
    if len(bookDetails_of_specificStudent)!=0:
        for i in range(len(bookDetails_of_specificStudent)):
            lst.append(bookDetails_of_specificStudent[i].get('bookid'))
        print(lst)
        lst=tuple(lst)
        print(lst)
        if len(lst)==1:
            query=f'SELECT bookName from books where bookId={lst[0]}'
        else:
            query=f'SELECT bookName from books where bookId in {lst}'

        conn.commit()
        mycursor.execute(query)
        dot=mycursor.fetchall()
        modified_dot=dict()
        for id,name in zip(lst,dot):
            modified_dot[id]=name[0]
        new=[]
        new.append(inf_details_ofspecificStudent[0])
        new.append(inf_details_ofspecificStudent[1])
        new.append(inf_details_ofspecificStudent[2])
        new.append(inf_details_ofspecificStudent[3])
        new.append(modified_dot)
        print(new)
        return new
    else:
        new=[]
        new.append(inf_details_ofspecificStudent[0])
        new.append(inf_details_ofspecificStudent[1])
        new.append(inf_details_ofspecificStudent[2])
        new.append(inf_details_ofspecificStudent[3])
        print(new)
        return new
        
    
           
def fetchStudentData():
    mycursor.execute("select * from student")
    showResult=mycursor.fetchall()
    data=[]
    for row in showResult:
        data.append(row)
    conn.commit()
    return data
if __name__=="__main__":
    # insertStudentData(582,"Naman Bansal","Sirsa",906,'[{"bookId":23,"dateofIssued":"04/56/45"}]')
    # updateStudentData(582,{"bookId":348,"dateofIssued":"09/45/45"})
    # print(fetchStudentData())
    returnSpecifictudentData(103)
        
