import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Setting up the Database

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Reference the Measurement and Stattion tables
Measurement = Base.classes.measurement
Station = Base.classes.station

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def homepage():
    return(
    f"All Available Routes:<br/>"
    f"(Note: Most recent available date is 2017-08-23 while the latest is 2010-01-01).<br/>"

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


if __name__ == '__main__':
  app.run(debug=True)
 