def topic_validation(user_input):
    while user_input.isnumeric() is False or int(user_input) <= 0 or int(user_input) > 3:
        print('Please enter a whole number between 1 & 3:')
        user_input = input()
    user_input = int(user_input)
    if user_input == 1:
        topic = 'Sports'
        return topic
    elif user_input == 2:
        topic = 'Geography'
        return topic
    else:
        topic = 'Food&Drink'
        return topic


def answer_validation(answer):
    while answer.isnumeric() is False or int(answer) <= 0 or int(answer) > 4:
        print('Please enter a whole number between 1 & 4: ')
        answer = input()
    answer = int(answer)
    return answer

def question_num_validation(question_input):
    while question_input.isnumeric() is False or int(question_input) <= 0 or int(question_input) > 2:
        print('Please enter a whole number between 1 & 2:')
        question_input = input()
    question_input = int(question_input)
    if question_input == 1:
        q_num = 5
        return q_num
    else:
        q_num = 3
        return q_num

def name_validation(name):
    while name == '':
        print('This field cannot be blank: ')
        name = input()
    return name