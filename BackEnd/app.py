from flask import Flask, render_template
import SqlConnection


app = Flask(__name__)

sql_connection = SqlConnection.SqlConnetion()

@app.route('/')
def index():
    sql_connection.SqlDataBase()
    myDB= sql_connection.ConnectDB() #connect to db
    #export data from database table and represent it in html table
    cursor = myDB.cursor()
    cursor.execute("USE attendance")
    #show all the the table in the database
    cursor.execute("SHOW TABLES")
    print("im here")
    cursor.execute("SELECT * FROM Attendence")
    #cursor.execute("SELECT * FROM Attendence")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)




if __name__ == '__main__':

    print('test')
    # from waitress import serve
    # serve(app, host='127.0.0.1', port=5000)

    app.run(host='0.0.0.0',port=5000,debug=True)

