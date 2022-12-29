from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from core import app
from models import SQL

Migrate(app, SQL)

db = Manager(app)
db.add_command("sqlite", MigrateCommand)

if __name__ == "__main__":
    db.run()