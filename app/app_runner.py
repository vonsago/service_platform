#!/usr/bin/env python
# coding=utf-8
'''
> File Name: app_runner.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  8/27 22:03:18 2018
'''
import logging
from uuid import uuid4

from flask import Flask, g, request
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.wrappers import Response
from app.utils.local import thread_local

LOG = logging.getLogger(__name__)


def configure_models():
    pass

def configure_buleprints(flask_app):
    from app.instance.instance_api import instance_management

    flask_app.register_blueprint(instance_management)

def add_app_hook(app):
    @app.errorhandler(APIException)
    def handler_api_exception(exception):
        return http_error_handler(exception)

    @app.errorhandler(Exception)
    def handler_all_exception(exception):
        return http_error_handler(exception)

    # fixme when flask >0.12. https://github.com/pallets/flask/blob/master/tests/test_user_error_handler.py#L151
    def http_error_handler(exception: Exception) -> Response:
        user_name = getattr(getattr(g, 'user', 'no login'), 'name', 'no login')
        LOG.exception(
            f"http_error_handler: InternalServerError user: {user_name} method: {request.method} Url: {request.url}, Body: {request.get_data()}")
        db.session.remove()
        if isinstance(exception, APIException):
            response = exception.get_respose()
        elif isinstance(exception, HTTPException):
            response = HttpApiException(exception).get_respose()
        else:

            exception = InternalServerError(str(exception))
            response = HttpApiException(exception).get_respose()

        LOG.info("http_error_handler finish handler error: {response} ".format(response=response))

        return response

    from werkzeug.exceptions import default_exceptions
    for code in default_exceptions:
        app.errorhandler(code)(http_error_handler)

def create_app():
    import app.utils.logger
    
    flask_app = Flask('psp-controller', template_folder=config.get_static_file_full_path('templates'))
    
    with flask_app.app_context():
        configure_blueprints(flask_app)

    add_app_hook(flask_app)
    return flask_app


if __name__ == "__main__":
    app = create_app()
    try:
        app.run('0.0.0.0', 8000, debug=app.config["DEBUG"], threaded=True)
    except Exception as e:
        LOG.info("Program exit unexpectly because an error {}".format(e))
