from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_content = request.form['content']
        task_date = request.form['date']
        if task_content and task_date:
            tasks.append({'content': task_content, 'date': task_date})
            return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

