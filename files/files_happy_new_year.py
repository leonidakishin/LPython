lst_file_in = []
with open("class_scores.txt", "r") as file_in:
    for line in file_in:
        lst_file_in.append(line.strip().split(" "))

with open("new_scores.txt", "w") as file_out:
    for i in range(len(lst_file_in)):
        print(
            f"{lst_file_in[i][0]} {int(lst_file_in[i][1]) + 5 if int(lst_file_in[i][1]) + 5 <= 100 else 100}",
            file=file_out,
        )
