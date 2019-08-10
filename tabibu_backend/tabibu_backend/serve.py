from flask import Flask,render_template
import pymysql.cursors
from flask import jsonify
from flask import request
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app,resources={r"/*":{"origins":"*"}})


def connect():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='tabibu',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    print(str(connection))
    return connection
def createtables():
    invoices = """CREATE TABLE IF NOT EXISTS invoices(
                        `id` int(11) NOT NULL AUTO_INCREMENT,
                        `amount` varchar(255) NOT NULL,
                        `purpose` varchar(30000) NOT NULL,
                        `patient_id` int(11) NOT NULL,
                        `doctor` varchar(20),
                        PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""

    consultations = """CREATE TABLE IF NOT EXISTS consultations(
                        `id` int(11) NOT NULL AUTO_INCREMENT,
                        `patient_id` int(11) NOT NULL,
                        `symptoms` varchar(30000) NOT NULL,
                        `illness` varchar(300),
                        `recommendation` varchar(30000),
                        `served` varchar(20),
                        PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""
    
    ambulances = """CREATE TABLE IF NOT EXISTS ambulances(
                        `id` int(11) NOT NULL AUTO_INCREMENT,
                        `patient_id` int(11) NOT NULL,
                        `location` varchar(3000) NOT NULL,
                        `date` varchar(200),
                        `served` varchar(20),
                        PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""

    app_user = """CREATE TABLE IF NOT EXISTS users(
                        `id` int(11) AUTO_INCREMENT,
                        `name` varchar(200) NOT NULL,
                        `email` varchar(70) NOT NULL,
                        `phone` varchar(20),
                        `gender` varchar(20),
                        `password` varchar(20),
                        `dob` varchar(20),
                        PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""
    
    hospitals = """CREATE TABLE IF NOT EXISTS hospitals(
                        `id` int(11) AUTO_INCREMENT,
                        `name` varchar(200) NOT NULL,
                        `location` varchar(70) NOT NULL,
                        `map_url` varchar(200),
                        `rating` varchar(20)
                        PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"""
    
    connection = connect()
    cur = connection.cursor()
    cur.execute(invoices)
    cur.execute(consultations)
    cur.execute(ambulances)
    cur.execute(app_user)
    connection.close()

@app.route("/")
def main_page():
    createtables()
    return render_template("index.html")

@app.route("/<name>")
def load_page(name):
    print(name)
    return render_template(name)

@app.route("/user/<name>")
def load_page(name):
    return render_template("client/"+name)

@app.route("/register",methods = ["POST","GET"])
def register():
    username = str(request.json.get("username"))
    email = str(request.json.get("email"))
    password = str(request.json.get("password"))

    data = (username,email, password)
    
    sql = "INSERT INTO users VALUES('',%s,%s,'','',%s,'')"
    connection = connect()
    cur = connection.cursor()
    cur.execute(sql,data)
    connection.commit()

    response = {"response":"registeration successful","code":200}

    return jsonify(response)

@app.route("/addconsultation",methods=["POST","GET"])
def addconsultation():
    patient_id = str(request.json.get("patient_id"))
    symptoms = str(request.json.get("symptoms"))

    data = (patient_id,symptoms)
    
    sql = "INSERT INTO consultations VALUES('',%s,%s,'','','false')"
    connection = connect()
    cur = connection.cursor()
    cur.execute(sql,data)
    connection.commit()
    response = {"response":"successful","code":200}

    return jsonify(response)

@app.route("/addinvoice",methods = ["POST","GET"])
def addinvoice():
    patient_id = str(request.json.get("patient_id"))
    amount = str(request.json.get("amount"))
    purpose = str(request.json.get("purpose"))
    doctor = str(request.json.get("doctor"))
    data = (amount,purpose,patient_id,doctor)
    
    sql = "INSERT INTO invoices VALUES('',%s,%s,%s,%s)"
    connection = connect()
    cur = connection.cursor()
    cur.execute(sql,data)
    connection.commit()
    response = {"response":"successful added Invoice","code":200}

    return jsonify(response)

@app.route("/addambulance",methods = ["POST","GET"])
def addambulance():
    patient_id = str(request.json.get("patient_id"))
    location = str(request.json.get("location"))

    data = (patient_id,location)
    
    sql = "INSERT INTO ambulances VALUES('',%s,%s,'')"
    connection = connect()
    cur = connection.cursor()
    cur.execute(sql,data)
    connection.commit()
    response = {"response":"successful requested Ambulance","code":200}

    return jsonify(response)

@app.route("/login",methods = ["POST","GET"])
def login():
    email = str(request.json.get("email"))
    password = str(request.json.get("password"))

    sql = "SELECT password FROM users WHERE email = %s"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql,(email))
    res = cur.fetchone()
    response = ""
    print(res)
    if password == res["password"]:
        response = {"response":"successfull","code":200}
    else:
        response = {"response":"failed","code":300}

    return jsonify(response)

@app.route("/getinvoices", methods = ["POST","GET"])
def getinvoices():
    patient_id = str(request.json.get("patient_id"))

    sql = "SELECT * FROM invoices WHERE patient_id = %s"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql,(patient_id))
    res = cur.fetchall()

    return jsonify(res)

@app.route("/getsingleinvoice", methods = ["POST","GET"])
def getsingleinvoice():
    id = str(request.json.get("id"))

    sql = "SELECT * FROM invoices WHERE id = %s"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql,(id))
    res = cur.fetchone()

    return jsonify(res)

@app.route("/getallinvoices", methods = ["POST","GET"])
def getallinvoices():
    
    sql = "SELECT * FROM invoices "
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql)
    res = cur.fetchall()

    return jsonify(res)

@app.route("/getconsultation", methods = ["POST","GET"])
def getconsultation():
    patient_id = str(request.json.get("patient_id"))

    sql = "SELECT * FROM consultations WHERE patient_id = %s"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql,(patient_id))
    res = cur.fetchall()

    return jsonify(res)

@app.route("/getsingleconsulation", methods = ["POST","GET"])
def getsingleconsulation():
    id = str(request.json.get("id"))

    sql = "SELECT * FROM consultations WHERE id = %s"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql,(id))
    res = cur.fetchone()

    return jsonify(res)


@app.route("/updateconsulation", methods = ["POST","GET"])
def updateconsulation():
    id_ = str(request.json.get("id"))
    illness = str(request.json.get("illness"))
    recom = str(request.json.get("recommend"))
    print(recom)
    sql = "UPDATE consultations SET illness=%s,recommendation=%s,served='true' WHERE id = %s"
    data = (illness,recom,id_)
    connection = connect()
    cur = connection.cursor()
    cur.execute(sql,data)
    connection.commit()
    response = {"response":"update successfully","code":200}

    return jsonify(response)


@app.route("/getallconsultation", methods = ["POST","GET"])
def getallconsultation():
    
    sql = "SELECT * FROM consultations WHERE served = 'false'"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql)
    res = cur.fetchall()

    return jsonify(res)

@app.route("/getallusers", methods = ["POST","GET"])
def getallusers():
    
    sql = "SELECT * FROM users"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql)
    res = cur.fetchall()

    return jsonify(res)

@app.route("/getambulances", methods = ["POST","GET"])
def getambulances():
    
    sql = "SELECT * FROM ambulances"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql)
    res = cur.fetchall()

    return jsonify(res)

@app.route("/getsingleambulance", methods = ["POST","GET"])
def getsingleambulance():
    id_ = str(request.json.get("id"))
    sql = "SELECT * FROM ambulances WHERE id=%s"
    connection = connect()
    cur = connection.cursor()
     
    cur.execute(sql,(id_))
    res = cur.fetchone()

    return jsonify(res)

@app.route("/getserved", methods = ["POST","GET"])
def getserved():
    
    sql = "SELECT * FROM consultations WHERE served = 'true'"
    connection = connect()
    cur = connection.cursor()
    cur.execute(sql)
    res = cur.fetchall()

    return jsonify(res)

@app.route("/summary", methods = ["POST","GET"])
def getsummary():
    served = len(getserved())







if __name__ == "__main__":
     app.run(debug=True)