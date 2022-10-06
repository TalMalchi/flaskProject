from flask import Flask, render_template
import SqlConnection

app = Flask(__name__)

sql_connection = SqlConnection.SqlConnetion()

@app.route('/')
def index():  # put application's code here
    print("im here")
    myDB= sql_connection.ConnectDB()
    #export data from database table and represent it in html table
    print("im here")
    cursor = myDB.cursor()
    cursor.execute("USE Attendence")
    cursor.execute("SELECT * FROM Attendence")
    data = cursor.fetchall()
    cursor.close()
    #print(data)
    return render_template('index.html', data=data)




if __name__ == '__main__':
    sql_connection.SqlDataBase()
    print('test')
    # from waitress import serve
    # serve(app, host='127.0.0.1', port=5000)

    app.run(host='0.0.0.0', port=5000, debug=True)

