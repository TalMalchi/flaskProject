from flask import Flask, render_template
import SqlConnection

app = Flask(__name__)
sql_connection = SqlConnection.SqlConnetion()


@app.route('/')
def index():
    sql_connection.SqlDataBase()
    myDB = sql_connection.ConnectDB()  # connect to db
    # export data from database table and represent it in html table
    cursor = myDB.cursor(buffered=True)
    cursor.execute("USE Attendance")
    cursor.execute("SELECT * FROM Attendance")
    #cursor.execute("SELECT * FROM Attendance")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    print('test')
    #sftp.download_csv_files_from_server()
    #subprocess.call(['python', 'Attendence.py', 'C:\\Users\\Tal\\Desktop\\DevOps\\CICD-ssh work\\flaskProject\\CsvFiles\\'])
    # from waitress import serve
    # serve(app, host='127.0.0.1', port=5000)

    app.run(host='0.0.0.0', port=5000, debug=True)
