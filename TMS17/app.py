from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import create_engine, Column, Integer, String
from flask import Flask, render_template, request
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


app = Flask(__name__)

engine = create_engine('sqlite:///students.db')

class Base(DeclarativeBase): pass
class Students(Base):
    __tablename__ = "Person"
    email = Column(String(50), unique=True, primary_key=True, index=True)
    name = Column(String(20))

Base.metadata.create_all(bind=engine)


@app.route("/", methods=["POST", "GET"])
def index():


    if request.method == 'POST':

        if request.method == 'GET':
            with Session(autoflush=False, bind=engine) as db:

                people = db.query(Students).all()
                file_loader = FileSystemLoader('templates')
                env = Environment(loader=file_loader)
                tm = env.get_template('index.html')
                return tm.render(users=people)
        if request.form['name'] and request.form['email']:
            with Session(autoflush=False, bind=engine) as db:

                new = Students(name=request.form['name'], email=request.form['email'])
                db.add(new)
                db.commit()
                return render_template('index.html')


    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8118)
    with Session(autoflush=False, bind = engine) as db:
        students = db.query(Students).all()
        if not Students: print('Будьте первыми! Заполните анкету')

