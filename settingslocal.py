app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydatabase'
db = SQLAlchemy(app)
