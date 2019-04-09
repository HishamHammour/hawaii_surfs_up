import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Setting up the Database

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Reference the Measurement and Stattion tables
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def homepage():
    return (
        f"All Available Routes:<br/>"
        f"(Note: available date is 2017-08-23 while the latest is 2010-01-01).<br/>"

        f"/api/v1.0/precipitation<br/>"
        f"- Query dates and temperature from the last year. <br/>"

        f"/api/v1.0/stations<br/>"
        f"- Returns a json list of stations. <br/>"

        f"/api/v1.0/tobs<br/>"
        f"- Returns list of Temperature Observations(tobs) for previous year. <br/>"

        f"/api/v1.0/yyyy-mm-dd/<br/>"
        f"- Returns an Average, Max, and Min temperature for given date.<br/>"

        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd/<br/>"
        f"- Returns an Min , Aveage and Max temperature for given start or start to end range.<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return Dates and Temp from the last year."""
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date <= "2016-01-01", Measurement.date >= "2016-01-01").\
        all()

    #create the JSON objects
    precipitation_list = [results]

    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
    results = session.query(Station.name, Station.station, Station.elevation).all()

    #create dictionary for JSON
    station_list = []
    for result in results:
        row = {}
        row['name'] = result[0]
        row['station'] = result[1]
        row['elevation'] = result[2]
        station_list.append(row)
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def temp_obs():
    """Return a list of tobs for the previous year"""
    results = session.query(Station.name, Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-01-01", Measurement.date <= "2017-01-01").\
        all()

    #create json, perhaps use dictionary
    tobs_list = []
    for result in results:
        row = {}
        row["Date"] = result[1]
        row["Station"] = result[0]
        row["Temperature"] = int(result[2])
        tobs_list.append(row)

    return jsonify(tobs_list)



if __name__ == '__main__':
  app.run(debug=True)
 