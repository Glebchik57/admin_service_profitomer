from admin import app
from admin.admin import create_admin


create_admin(app)

if __name__ == '__main__':
    app.run(debug=True)
