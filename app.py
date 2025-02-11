from flask import Flask, render_template, request
import matplotlib.pyplot as plt
app = Flask(__name__,template_folder='templates')
@app.route('/',methods =['GET','POST'])
def details():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method=="POST":
            type=request.form["ID"]
            id=request.form["id_value"]
            if id=="":
                return render_template("wrong.html")
            id=int(id)
            data=[]
            Total_marks =0
            Average_marks=0
            Maximum_marks=0
            
            with open('data.csv','r') as file:
                 file.readline()
                 if type=='student_id':
                    for row in file:
                           row=list(map(int,row.strip().split(',')))
                           if row[0]==id:
                                data.append(row)
                                Total_marks +=row[2]
                    return render_template('studentdetails.html',data=data,total_marks_data=Total_marks )  
                 elif type=='course_id':
                       if type=='course_id':
                         for row in file:
                           row=list(map(int,row.strip().split(',')))
                           if row[1]==id:
                                data.append(row[2])
                                Total_marks += row[2]
                       Average_marks =Total_marks/len(data)
                       Maximum_marks = max(data)
                       plt.hist(data)
                       plt.xlabel('Marks')
                       plt.ylabel('Frequency')
                       plt.savefig('static/plot.png')
                       return render_template('coursedetails.html',average_marks=Average_marks,maximum_marks=Maximum_marks,img='static/plot.png')
            if len(data)==0:
                      return render_template("wrong.html")
     
app.debug = True
app.run()