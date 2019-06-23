#! /usr/bin/env python
from sensorserver import create_app, logger

# flask run
if __name__ == "__main__":
    app = create_app()
    logger.info("starting sensor server! %s %s", u'\U0001f64c', u'\U0001F680')
    app.run(debug=True)
