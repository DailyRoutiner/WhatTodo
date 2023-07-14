from flask import Flask, render_template,request, redirect, url_for
import random

app = Flask(__name__)

names = ["Dany", "Jun"]
todos=[
    {
        'content': "Work out",
        "status": True
    },
        {
        'content': "Meet friends",
        "status": False
    },
    {
        'content': "Go to Library",
        "status": False
    }
]

@app.route('/')
def index():
    return render_template("index.html", name=random.choice(names), todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    # Fetch the value from the element that has 'todo' name 
    todos.append({
        'content': todo,
        "status": False
    })
    # Append the value to the 'todos' array
    return redirect(url_for("index"))
    # Redirect to the index page
    # The index page will re-load the template based on the 'todos' array which is just updated.

@app.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['content'] = request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)
    
@app.route("/check/<int:index>")
def check(index):
    todos[index]['status'] = not todos[index]['status']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
