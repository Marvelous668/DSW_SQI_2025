questions = [
    {
        "prompt" : "What is the capital of Nigeria? ",
        "options" : ["A. Oyo", "B. Abuja", "C. Lagos", "D. Osogbo"],
        "answer" : "B"
    },


    {
        "prompt" : "Who is the first man on earth? ",
        "options" : ["A. Enoch", "B. Abel", "C. Adam", "D. Cain"],
        "answer" : "C"
    },


    {
        "prompt" : "The total number of perfect squares between 1 and 1000 is",
        "options" : ["A. 31", "B. 50", "C. 25", "D. 64"],
        "answer" : "A"
    },


    {
        "prompt" : "Who is the father of computer science?",
        "options" : ["A. Alan Turin", "B. Larry Page", "C. Steve Job", "D. Laslie Lamport" ],
        "answer" : "A"
    },


    {
        "prompt" : "Larry Page co-founder google with whom?",
        "options" : ["A. Paul Alen", "B. Adam smith", "C.Sergey Brin", "D. Michael Sipser" ],
        "answer" : "C"
    }
    

]




    


def run_quiz() :   
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"] :
            print(option) 
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == question["answer"]:
           print("Correct\n")
           score += 1
        else:
            print("Wrong, the correct answer was", question["answer"], "\n")   
       
    print(f"you got {score} out of {len(questions)}")     





run_quiz()