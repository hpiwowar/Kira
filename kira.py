import random

print 'hello Kira.'

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
    answer = random.randint(0, 10)
    return answer    

def answer_with_colour():
    answer = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "grey", "white", "black", "see-through", "pink"])
    return answer    

def answer_with_because():
    answer = "Because"
    return answer    

def answer_with_spelling(question):
    bucket_of_all_the_words = question.split(" ")
    for this_word in bucket_of_all_the_words:
        if "-" in this_word:
            word_to_spell = this_word

            answer_word = word_to_spell.replace("-", "")

            return "It spells " + answer_word
            
    answer = "It spells I DON'T KNOW"
    return answer    

while (True):
    print
    question = raw_input("ask me a question: ")
    if not question:
        continue

    the_question_starts_with_is = question.lower().startswith("is")
    the_question_starts_with_what_colour = question.lower().startswith("what colour")
    the_question_starts_with_why = question.lower().startswith("why")
    the_question_starts_with_do = question.lower().startswith("do")
    the_question_has_dashes = "-" in question

    if the_question_starts_with_is:
        answer = answer_with_yes_or_no()
    elif the_question_starts_with_what_colour:
        answer = answer_with_colour()
    elif the_question_starts_with_why:
        answer = answer_with_do()
    elif the_question_starts_with_do:
        answer = answer_with_yes_or_no()
    elif the_question_has_dashes:
        answer = answer_with_spelling(question)
    else:
        answer = answer_with_number()


    print "my answer is ", answer

    answer2 = raw_input("""Do you think my answer is right or wrong or neither? 
    (Type A for right and B for wrong and C for neither and D for sometimes.)""")
    if "A" in answer2.upper():
        print "I'm glad you think my answer is right"
    elif "D" in answer2.upper():
        print "ok"
    else:    
        print "Too bad!"

print "goodbye"
