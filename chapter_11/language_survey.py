from survey import AnonymousSurvey

def language_survey():
    question = "What is your first language???";
    my_survey = AnonymousSurvey(question);
    my_survey.show_question();
    print("Enter 'q' at any time to quit!!!\n");
    while True:
        response = input("Language: ");
        if response == 'q':
            break
        my_survey.store_response(response);
    print("\nThank you to everyone who participated in this survey!");
    my_survey.show_results();

language_survey();