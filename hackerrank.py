if __name__ == "__main__":
    list_of_names_and_values = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_of_names_and_values.append([name, score])
    sorted_score = sorted(
        list(set([score for name, score in list_of_names_and_values]))
    )
    second_lowest = sorted_score[1]
    for name, score in sorted(list_of_names_and_values):
        if score == second_lowest:
            print(name)
