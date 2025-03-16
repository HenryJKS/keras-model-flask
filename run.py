from app import create_app

app = create_app()

@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run()