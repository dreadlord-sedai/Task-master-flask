
        else:
            tasks = myTask.query.order_by(myTask.created).all()
            return render_template('index.html', tasks=tasks)







