if __name__ == '__main__':
    #Declare the lists and variable
    score_list = []
    student_list = []
    second_lowest = 0
    names = []
    for _ in range(int(input("How many students in the class ? "))):
        name = input("Name : ")
        score = float(input("Score : "))
        student_list.append([name, score])  #Making a nested list
        score_list.append(score)  #making list only from scores

    score_set = set(score_list)  #Convert list into a set
    sorted_scores = sorted(score_set)  #sort the set and making the new sorted list
    second_lowest = sorted_scores[1]   #determining the 2nd lowest score

    for i in student_list:
        if i[1] == second_lowest:  #compare each score to the second lowest score.
            names.append(i[0]) #making a list of names with 2nd lowest scores

    sorted_names = sorted(names)  #sorting the students names

    for name in sorted_names:  #print the sorted names line by line
        print(name)
