import random
import datetime
from os import system

print 'hello Kira.'
system('say Hello Kira!')

x=7*1
print 'the math answer=', x


def answer_with_yes_or_no():
    random_choice = random.random()
    if random_choice > 0.5:
        answer = "no"
    else:
        answer = "yes"
    return answer    

def answer_with_number():
    answer = random.randint(0, 100)
    return answer    

def answer_with_colour():
    answer = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "grey", "white", "black", "see-through", "pink"])
    return answer    

def answer_with_weather():
    weather = random.choice(["sunny", "cloudy", "rainy", "foggy", "snowy", "windy"])
    answer = "The weather today is " + weather
    return answer    

def answer_with_because():
    answer = "For a reason I do not know."
    return answer    

def answer_with_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    am_pm = "a.m."
    if hour > 12:
        hour = hour - 12
        am_pm = "p.m."
    answer = "it is %d:%d %s" %(hour, minute, am_pm)
    return answer    

def answer_with_spelling(question):
    bucket_of_all_the_words = question.split(" ")
    for this_word in bucket_of_all_the_words:
        if "-" in this_word:
            word_to_spell = this_word

            letters_in_answer_word = word_to_spell.replace("-", ". ")
            letters_in_answer_word += ". "

            answer_word = word_to_spell.replace("-", "")
            answer = letters_in_answer_word + " spells " + answer_word
            return answer

    answer = "It spells I DON'T KNOW"
    return answer    

def answer_with_math_answer(question):
    answer = eval(question)
    question_to_speak = question.replace("+", " plus ").replace("-", " minus ").replace("*", " times ")
    response = question_to_speak + " equals " + str(answer)
    return response

def say_what_comes_after(question):
    words_to_say = question.replace("say", "")
    return words_to_say    

while (True):
    print
    question = raw_input("ask me a question: ")
    if not question:
        continue
    question = question.strip()

    the_question_starts_with_is = question.lower().startswith("is")
    the_question_starts_with_are = question.lower().startswith("are")
    the_question_starts_with_will = question.lower().startswith("will")
    the_question_starts_with_what_colour = question.lower().startswith("what colour")
    the_question_starts_with_why = question.lower().startswith("why")
    the_question_starts_with_do = question.lower().startswith("do")
    the_question_has_spell = "spell" in question.lower()
    the_question_has_math_sign = ("+" in question) or ("-" in question) or ("*" in question)
    the_question_starts_with_say = question.lower().startswith("say")
    the_question_has_weather = "weather" in question.lower()
    the_question_is_what_time_is_it = "what time is it" in question.lower()

    if (the_question_starts_with_is or 
        the_question_starts_with_are or
        the_question_starts_with_will):
        answer = answer_with_yes_or_no()
    elif the_question_starts_with_what_colour:
        answer = answer_with_colour()
    elif the_question_starts_with_why:
        answer = answer_with_because()
    elif the_question_starts_with_do:
        answer = answer_with_yes_or_no()
    elif the_question_has_spell:
        answer = answer_with_spelling(question)
    elif the_question_has_math_sign:
        answer = answer_with_math_answer(question)
    elif the_question_starts_with_say:
        answer = say_what_comes_after(question)
    elif the_question_has_weather:
        answer = answer_with_weather()
    elif the_question_is_what_time_is_it:
        answer = answer_with_time()
    else:
        answer = answer_with_number()


    print answer
    system("say " + str(answer))


    answer2 = raw_input("""Do you think my answer is right or wrong or neither? 
    Type A for right\n
         B for wrong\n
         C for neither\n
         D for sometimes\n
         E for maybe: """)
    if "A" in answer2.upper():
        response = "I am glad you think my answer is right"
    elif "D" in answer2.upper():
        response = "ok"
    elif "E" in answer2.upper():
        response = "maybe, maybe not"
    else:    
        response = "Too bad!"
    print response
    system("say " + response)

print "goodbye"
