import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='root',database='namandb')
mycursor=conn.cursor()
def insertData(id,name,quantity,issued):
        try:
            insert_data='insert into books(bookId,bookName,quantity,issued) values(%s,%s,%s,%s)'
            records=[
                (id,name,quantity,issued)
            ]
            mycursor.executemany(insert_data,records)
            conn.commit()
            return 1
        except:
             return 0
def updateBook(myid):
     try:
          mycursor.execute(f'SELECT issued FROM books WHERE bookId={myid}')
          n=mycursor.fetchone()[0]
          print(n)
          query=f'UPDATE books SET issued={n+1} WHERE bookId={myid}'
          mycursor.execute(query)
          conn.commit()
     except Exception as e:
          print(e)
          print("Error Unable To Update Book")
def returnUpdateBook(myid):
        try:
            mycursor.execute(f'SELECT issued FROM books WHERE bookId={myid}')
            n=mycursor.fetchone()[0]
            print(n)
            query=f'UPDATE books SET issued={n-1} WHERE bookId={myid}'
            mycursor.execute(query)
            conn.commit()
        except Exception as e:
          print(e)
          print("Error Unable To Update Book In Returning Function")
     
def fetchData():
    mycursor.execute("select * from books")
    showResult=mycursor.fetchall()
    data=[]
    for row in showResult:
        print(row)
        data.append(row)
    conn.commit()
    return data
if __name__=="__main__":
#      updateBook(101)
     fetchData()
        
