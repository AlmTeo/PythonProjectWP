from distutils.log import debug
from unicodedata import name
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)