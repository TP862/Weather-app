import python_weather

import asyncio
import os

import json

async def getweather() -> None:
 async with python_weather.Client(unit=python_weather.METRIC) as client:
    weather = await client.get('Tokyo')

    data = {
      "temp" : weather.temperature,
      "pressure" : weather.pressure,
      "humidity" : weather.humidity,
      "region" : weather.region
    }

    with open("data.json", "w") as json_file:
      json.dump(data, json_file, indent=4)

if __name__ == '__main__':
   if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(getweather())

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///weather.db'
db = SQLAlchemy(app)

class weather(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  temperature = db.Column(db.Integer, nullable=False)
  pressure = db.Column(db.Float, nullable=False)
  humidity = db.Column(db.Integer, nullable=False)
  region = db.Column(db.String(100), nullable=False)
  date_recorded = db.Column(db.DateTime, default=datetime.now)

  def __repr__(self):
    return '<Region %r>' % self.region
  
  with app.app_context():

        db.create_all()


@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)