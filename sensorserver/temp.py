import functools
import json
import logging
from datetime import datetime

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from sensorserver.db import get_db

logger = logging.getLogger(__name__)

bp = Blueprint("temperature", __name__, url_prefix="/api/v1/temperature")


@bp.route("", methods=["GET"])
def get_temp():
    """ get's the last 5 temps posted """
    cur = get_db().cursor()
    cur.execute(
        """
        select sensor_id as 'id', timestamp as 'date', temperature, humidity
            from climate
        order by created_at desc
        limit 7
        """
    )
    results = cur.fetchall()

    res = [
        {
            "id": d['id'],
            "date": d['date'],
            "temperature": d['temperature'],
            "humidity": d['humidity']
        }
        for d in results
    ]
    return json.dumps({"status": "ok", "data": res}), 200


@bp.route("", methods=["POST"])
def post_temp():
    data = json.loads(request.get_data().decode("utf8"))
    db = get_db()
    cur = db.cursor()

    # create a timestamp
    now = datetime.utcnow()

    # pull off the sensor_id from the request body
    sensor_id = data.get("sensor_id", "")

    # get the temp
    t = data.get("temp", None)

    # get the humidity
    h = data.get("humidity", None)

    try:
        cur.execute(
            'INSERT INTO climate (sensor_id, timestamp, temperature, humidity, created_at)'
            'VALUES (?, ?, ?, ?, ?)',
            (sensor_id, now, t, h, now),
        )
        db.commit()
    except Exception as err:
        logger.error("error %s", err)

    return json.dumps({"status": "ok"}), 200
