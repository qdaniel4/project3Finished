import dbManager
from datetime import datetime
import random
import validation

def main():

    topic = show_topic()
    question_num = question_number()

    info = dbManager.get_q_info(topic, question_num)
    #print(info)
    start = datetime.now()
    start = str(start)
    sesh_id = dbManager.add_session_start(start)
    for question in info:
        q_id, points, diff, text = format_tuple(question)
        print(f'Points: {points}')
        print(f'Difficulty: {diff}\n')
        print(f'{text}\n')
        choices = random_choices(question)
        print()
        ans = input('enter answer: ')
        ans = int(ans)
        user_ans = choices[ans-1]
        result, points_received = check_answer(user_ans, q_id, points)
        res_id = dbManager.add_result(points, points_received, user_ans, result, q_id)
        dbManager.update_results(sesh_id, res_id)
    end = datetime.now()
    end = str(end)
    dbManager.update_session(end, start)
    show_session_info(sesh_id)

def format_tuple(info):
    question_id = info[0]
    text = info[1]
    points = info[2]
    difficulty = info[3]
    return question_id, points, difficulty, text
def random_choices(info):
    choice_list = [info[4], info[5], info[6], info[7]]
    random.shuffle(choice_list)
    for choice in range(len(choice_list)):
        print(f'{choice + 1}: {choice_list[choice]}')
    return choice_list
def check_answer(ans, q_id, points):
    correct_ans = dbManager.get_answer(q_id)
    yes = 'Yes'
    no = 'No'
    if ans != correct_ans[0]:
        print(f'Incorrect, the correct answer was {correct_ans[0]}')
        total = points - points
        return no, total
    else:
        print('Correct')
        return yes, points
def show_topic():
    print('1: Sports\n'
          '2: Geography\n'
          '3: Food & Drink\n')
    topic = input('please enter topic number: \n')
    topic = validation.topic_validation(topic)
    return topic
def question_number():
    print('1: Five Questions\n'
          '2: Three Questions\n')
    q_num = input('Please enter the corresponding number for either five or three questions: ')
    question_num = validation.question_num_validation(q_num)
    return question_num
def show_session_info(sesh_id):
    session = dbManager.show_session(sesh_id)
    for row in session:
        print(row)
















main()