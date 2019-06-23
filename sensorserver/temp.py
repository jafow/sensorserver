import functools
import json
import logging

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

bp = Blueprint("temperature", __name__, url_prefix="/temperature")


@bp.route("/", methods=["GET"])
def get_temp():
    logger.debug("received GET to /temperature with request: %s", request.headers)
    return "Temperature is 72 degrees and sunny"
