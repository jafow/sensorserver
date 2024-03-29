import os
import logging

from flask import Flask

# configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev"),
        DATABASE=os.path.join(app.instance_path, "sensorserver.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object("sensorserver.config")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # setup db
    from sensorserver.db import init_app, init_db

    init_app(app)
    init_db(app)

    # register server routes
    from sensorserver import temp

    app.register_blueprint(temp.bp)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        logger.info("instance folder already exists; moving on")
        pass
    return app
