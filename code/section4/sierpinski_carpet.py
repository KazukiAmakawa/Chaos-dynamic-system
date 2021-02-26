import Init
import numpy as np

FILE_DIR = "./img"
iteration_time = 10

def main():
    for kase in range(1, iteration_time + 1):
        vals = [[[0]] for n in range(pow(pow(3, kase), 2))]
        for i in range(0, len(vals)):
            have_five = False
            new_i = i
            while 1:
                code = new_i - 9 * int(new_i/9)
                if code == 4:
                    have_five = True
                    break
                if int(new_i/9) == 0:
                    break
                new_i = int(new_i/9)

            if have_five:
                vals[i][0][0] = 255

        mark = 0
        while 1:
            if mark + 1 >= len(vals):
                break
            matrix = vals[mark: mark + 9]
            new_matrix = [[0 for n in range(len(vals[mark]) * 3)] for n in range(len(vals[mark]) * 3)]
            for p in range(0, 3):
                for q in range(0, 3):
                    for i in range(0, len(vals[mark])):
                        for j in range(0, len(vals[mark])):
                            new_matrix[p * len(vals[mark]) + i][q * len(vals[mark]) + j] = matrix[p * 3 + q][i][j]
            mark += 9
            vals.append(new_matrix)
        Filename = FILE_DIR + str(kase) + ".png"
        img = vals[len(vals) - 1]
        Init.ImageIO(file_dir = Filename, img = np.float32(img), io = "o", mode = "grey", backend = "opencv")
    return


if __name__ == '__main__':
    main()