if __name__ == '__main__':
    score_list = []
    student_list = []
    second_lowest = 0
    names = []
    for _ in range(int(input("How many students in the class ? "))):
        name = input("Name : ")
        score = float(input("Score : "))
        student_list.append([name, score])
        score_list.append(score)

    score_set = set(score_list)
    sorted_scores = sorted(score_set)
    second_lowest = sorted_scores[1]

    for i in student_list:
        if i[1] == second_lowest:
            names.append(i[0])

    sort_name = sorted(names)

    for n in sort_name:
        print(n)
