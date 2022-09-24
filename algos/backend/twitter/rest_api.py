from flask import Flask, request
from flask import jsonify
from ast import literal_eval


# My files

from db_operations import select, insert, db_setup
from alternative_twitter import get_data_from_web

api = Flask(__name__)



# Restful API

@api.route('/status', methods=['GET'])
def get_status() -> bytes:
    """
    :return: text  for the received status_id
    """
    # Extract the received status_id

    status_id: str = request.args.get('status_id')

    # Fetch rows from DB using the status_id

    status_text = select(status_id, table='status_text', column='status_text')

    # if comments diff from "" there are comments

    if status_text:
        return jsonify(literal_eval(status_text))

    # If the we didn't returned yet, we need get the comments from the web and store it in the DB

    status_text, comments = get_data_from_web(status_id)

    insert(status_id, status_text, comments)

    return jsonify(literal_eval(status_text))


@api.route('/comments', methods=['GET'])
def get_comments() -> bytes:
    """
    :return: comments for the received status_id
    """
    # Extract the received status_id

    status_id: str = request.args.get('status_id')

    # Fetch rows from DB using the status_id

    comments = select(status_id, table='status_text', column='comments')

    # if comments diff from "" there are comments

    if comments:
        return jsonify({"comments": literal_eval(comments)})

    # If the we didn't returned yet, we need get the comments from the web and store it in the DB

    status_text, comments = get_data_from_web(status_id)

    insert(status_id, status_text, comments)

    return jsonify({"comments": literal_eval(comments)})


if __name__ == '__main__':
    # every run of the file is recreated the DB

    db_setup()

    api.run(port=8081)