from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)
bLoggedIn = False


def loadDB():
    connection = sqlite3.connect('OpenSesame.db')
    cursor = connection.cursor()
    cursor.execute("SELECT *, rowid FROM tblDevices")
    dbData = []
    for row in list(cursor.fetchall()):
        dbData.append(row)
    return dbData


def addDevice(devAdd):
    if devAdd == '':
        exit()
    connection = sqlite3.connect('OpenSesame.db')
    cursor = connection.cursor()
    command = "SELECT EXISTS(SELECT 1 FROM tblDevices WHERE DeviceMAC ='" + devAdd[1] + "');"
    cursor.execute(command)
    bExists = cursor.fetchone()
    if bExists[0] == 0:
        cursor.execute("INSERT INTO tblDevices VALUES (?,?)", devAdd)
        connection.commit()
        connection.close()
        return 'Device added successfully!'
    else:
        return 'Device already exists!'


def deleteDevice(devDelete):
    connection = sqlite3.connect('OpenSesame.db')
    cursor = connection.cursor()
    for row in devDelete:
        cursor.execute("DELETE FROM tblDevices WHERE rowid=" + row)
    connection.commit()
    connection.close()
    return 'Delete Successful!'


@app.route('/')
def forwardLogin():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    global bLoggedIn
    bLoggedIn = False
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            bLoggedIn = True
            return redirect(url_for('deviceconfiguration'))
    return render_template('login.html', error=error)


@app.route('/deviceconfiguration', methods=['GET', 'POST'])
def deviceconfiguration():
    global bLoggedIn
    if bLoggedIn:
        if request.method == 'POST':
            if request.form['submit_button'] == 'Add':
                devAdd = [request.form['addDN'], request.form['addMAC']]
                error = addDevice(devAdd)
                return render_template('deviceconfiguration.html', errorAdd=error, data=loadDB())
            else:
                deleterows = request.form.getlist('checkbox')
                deleteDevice(deleterows)
                return render_template('deviceconfiguration.html', data=loadDB())
        else:
            return render_template('deviceconfiguration.html', data=loadDB())
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.72')
