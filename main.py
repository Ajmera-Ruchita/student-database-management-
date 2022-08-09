from flask import Flask,request,render_template,session,redirect
import pymysql as p
app = Flask(__name__)
def getconnection():
    return p.connect(host='localhost',user='root',port=3306,database='studentdb')

#register code
@app.route("/")
def index():
    return render_template("index.html")

#student code
@app.route("/add_student")
def add_student():
    return render_template("add_student.html")

@app.route("/saverecord",methods = ["POST"])
def saveRecord():
    msg = "msg"
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        gender = request.form["gender"]
        contact = request.form["contact"]
        dob = request.form["dob"]
        address = request.form["address"]
        con=getconnection()
        cur=con.cursor()
        cur.execute("insert into Student_Info (name, email, gender, contact, dob, address) values (%s,%s,%s,%s,%s,%s)",(name, email, gender, contact, dob, address))
        con.commit()
        msg = "Student details successfully Added"
        con.close()
        return render_template("success_record.html",msg = msg)

#display code
@app.route("/student_info")
def student_info():
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from Student_Info")
    rows = cur.fetchall()
    return render_template("student_info.html",rows = rows)
          
#delete code
@app.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():
    id = request.form["id"]
    con=getconnection()
    cur=con.cursor()
    query1="delete from Student_Info where id=%s"
    cur.execute(query1,(id,))
    
    
    rows = cur.fetchall()
    if not rows == []:
        cur.execute("delete from Student_Info where id = %s",(id,))
        msg = "Student details successfully deleted"
        con.commit()
        con.close()
        return render_template("delete_record.html", msg=msg)
    else:
        msg = "can't be deleted"
        return render_template("delete_record.html", msg=msg)

@app.route("/courselink")
def course_fun():
    return render_template("courses.html")

@app.route("/about")
def about_fun():
    return render_template("about.html")

@app.route("/ds")
def ds_fun():
    return render_template("ds.html")

@app.route("/py")
def py_fun():
    return render_template("py.html")

@app.route("/sql")
def sql_fun():
    return render_template("sql.html")

@app.route("/java")
def java_fun():
    return render_template("java.html")

@app.route("/dv")
def dv_fun():
    return render_template("dv.html")

@app.route("/ai")
def ai_fun():
    return render_template("ai.html")

@app.route("/pbi")
def pbi_fun():
    return render_template("pbi.html")
         
        
if __name__ == "__main__":
    app.run(debug = True)  