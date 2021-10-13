import sqlite3

conn = sqlite3.connect('testing_quiz_db.db')

def get_q_id_by_topic(topic):
    select_str = 'select question_id from quiz_questions where topic == ?'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            res = con.execute(select_str, (topic, ))
            ids = res.fetchall()
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
    return ids
def get_q_info(topic, q_num):
    print(topic)
    select_str = 'select question_id, text, points, difficulty, correct, wrong1, wrong2, wrong3 from quiz_questions where topic == ? limit ?'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            res = con.execute(select_str, (topic, q_num, ))
            info = res.fetchall()
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
    return info

def get_answer(question_id):
    select_str = 'select correct from quiz_questions where question_id = ?'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            res = con.execute(select_str, (question_id, ))
            answer = res.fetchone()
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
    return answer

def add_result(points_available, points_received, user_answer, correct, question_id):
    insert_str = 'insert into results (points_available, points_received, user_answer, correct, question_id)' \
                 'values (?, ?, ?, ?, ?)'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            res = con.execute(insert_str, (points_available, points_received, user_answer, correct, question_id, ))
            new_id = res.lastrowid
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
    return new_id
def add_session_start(start):
    insert_str = 'insert into session (start) values (?)'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            res = con.execute(insert_str, (start, ))
            sesh_id = res.lastrowid
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
    return sesh_id
def update_session(end, start):
    update_str = 'update session set end == ? where start == ?'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            con.execute(update_str, (end, start, ))
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
def update_results(sesh_id, res_id):
    update_str = 'update results set session_id == ? where result_id == ?'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            con.execute(update_str, (sesh_id, res_id, ))
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
def show_session(sesh_id):
    select_str = 'select question_id, user_answer, correct, points_received, points_available start, end from results join session on results.session_id = session.session_id where session.session_id == ?'
    try:
        with sqlite3.connect('testing_quiz_db.db') as con:
            res = con.execute(select_str, (sesh_id, ))
            session_info = res.fetchall()
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        con.close()
    return session_info
