import csv
from pickle import TRUE
import statistics
import math
import sys


def main():
    sus_score = 0
    name = ""
    sus_scores = {}

    with open(sys.argv[1]) as f:
        f2 = csv.reader(f, delimiter=",", doublequote=True,
                        lineterminator="\r\n", quotechar='"', skipinitialspace=True)

        header = next(f2)

        for i, row in enumerate(f2):
            print("---------------------------------")
            print(row)  # ここには一人一人のデータが含まれている。
            for j, ans in enumerate(row):
                if j == 1:
                    name = ans
                    continue
                if j <= 2:
                    continue

                if is_even(j):
                    sus_score += 5 - int(ans)
                else:
                    sus_score += int(ans) - 1

            print("------------")
            print(sus_score * 2.5)
            sus_scores[name] = sus_score * 2.5
            sus_score = 0

        print(sus_scores)
        print(calc_sus_score_average(sus_scores))

        calc_sus_score_average(sus_scores)


def calc_sus_score_average(sus_scores):
    sum = 0
    for name, sus_score in sus_scores.items():
        sum += sus_score

    return sum / len(sus_scores)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
