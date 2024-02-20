from website import create_app

app = create_app()

# run web server if running the file correctly
if __name__ == '__main__':
    # run flask web server, debug = true reruns web server when python code is changed
    app.run(debug = True)