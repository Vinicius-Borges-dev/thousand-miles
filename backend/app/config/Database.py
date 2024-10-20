class Database:
    __database: str = "thousand-miles"

    @staticmethod
    def create_connection(app, db):
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Database.__database}.sqlite3"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        db.init_app(app)
        return db
