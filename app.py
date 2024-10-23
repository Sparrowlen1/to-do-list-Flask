from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

todos=[]

# dictionary below
# {"id":1,"task":"build an api","completed":False},

@app.route('/', methods=["GET"])
def home():
    return render_template("home.html",todos=todos)

@app.route("/add", methods=["POST"])
def add():
    toaddtask = request.form['task']
    new_task = {"id": len(todos)+1,"task":toaddtask,"completed":False}
    todos.append(new_task)
    return redirect('/')

@app.route('/complete/<int:todo_id>')
def mark_as_complete(todo_id):
    for todo in todos:  
        if todo['id'] == todo_id:
            todo['completed']=True
    return redirect('/')

@app.route('/delete/<int:todo_id>')
def delete_task(todo_id):
    global todos
    todos=[todo for todo in todos if todo['id']!=todo_id]
    return redirect('/')


if __name__ =='__main__':
    app.run(debug=True)