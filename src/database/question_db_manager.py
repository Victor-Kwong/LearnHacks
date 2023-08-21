from firebase_admin import firestore

from models.question import Question
from database.firestore_setup import cred, firestore_app


def get_question_with_question_name(username, question_name):
    """
    returns None if user not found
    :param username:
    :param question_name:
    :return: User object
    """
    global db

    result = db.collection("users").document(username).collection("questions").document(question_name)
    loaded_question = result.get()

    if not loaded_question.exists:
        return None

    return Question(**(loaded_question.to_dict()))


def add_question(username, question_name):
    """
    returns False if operation unsuccessful
    returns True if operation is successful
    :param username:
    :param question_name:
    :return: boolean
    """
    global db

    doc_ref = db.collection("users").document(username).collection("questions").document(question_name)
    doc_ref.set(question_name.__dict__)


def delete_question(username, question_name):
    """
    returns False if operation unsuccessful
    returns True if operation is successful
    :param username:
    :param question_name:
    :return: boolean
    """
    global db

    doc_ref = db.collection("users").document(username).collection("questions").document(question_name)
    doc_ref.delete()


def update_question(username, question_name):
    """
    returns False if operation unsuccessful
    returns True if operation is successful
    :param username:
    :param question_name:
    :return: boolean
    """
    global db

    doc_ref = db.collection("users").document(username).collection("questions").document(question_name)
    doc_ref.set(question_name.__dict__)


def count_question(username):
    global db

    return db.collection("users").document(username).collection("questions").count().get()[0][0].value


db = firestore.client()
