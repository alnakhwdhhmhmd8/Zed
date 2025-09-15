from sqlalchemy import Boolean, Column, String

from userbot.plugins.sql_helper import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    username = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.username = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr


def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "البوتات":
        curr_perm.bots = locked
    elif lock_type == "الاوامر":
        curr_perm.commands = locked
    elif lock_type == "الايميل":
        curr_perm.email = locked
    elif lock_type == "التوجيه":
        curr_perm.forward = locked
    elif lock_type == "المعرفات":
        curr_perm.username = locked
    elif lock_type == "الروابط":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "البوتات":
        return curr_perm.bots
    if lock_type == "الاوامر":
        return curr_perm.commands
    if lock_type == "الايميل":
        return curr_perm.email
    if lock_type == "التوجيه":
        return curr_perm.forward
    if lock_type == "المعرفات":
        return curr_perm.username
    if lock_type == "الروابط":
        return curr_perm.url


def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
