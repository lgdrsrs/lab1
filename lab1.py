import os
import time

WHITE_BG = "\x1b[47m"
RED_BG = "\x1b[41m"
PURPLE_BG = "\x1b[45m"
RESET = "\x1b[0m"
PIXEL = "  "


def draw_japan_flag(height, animation=False, frames=0):
    width = int(1.5 * height)
    r = 0.6 * height / 2  # диаметр круга = 3/5 высоты флага
    cx = (width - 1) / 2
    cy = (height - 1) / 2

    def just_draw_flag():
        for y in range(height):
            for x in range(width):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
                    print(f"{RED_BG}{PIXEL}{RESET}", end="")
                else:
                    print(f"{WHITE_BG}{PIXEL}{RESET}", end="")
            print()

    if animation:
        shift = (height / 2) / (frames - 1)
        cy = (height - 1) / 2 + (frames - 1) * shift
        os.system("clear")
        for _ in range(frames):
            print(f"\x1b[{height}A", end="")
            just_draw_flag()
            cy -= shift
            time.sleep(1)
    else:
        just_draw_flag()
    print()


def draw_pattern_g(count, r):
    cx = r
    cy = r
    step = 2 * r
    width = step * count + 1
    height = 2 * r + 1
    for y in range(height):
        dy = abs(y - cy)
        for x in range(width):
            dx = abs(x % step - cx)
            if r - 1 <= dx + dy <= r:
                print(f"{PURPLE_BG}{PIXEL}{RESET}", end="")
            else:
                print(PIXEL, end="")
        print()
    print()


def draw_diagram(file_name, width=50):
    num_greater_neg5 = []
    num_less_neg5 = []
    qty = 0

    with open(file_name, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            num = float(line)
            if -5 < num <= 0:
                num_greater_neg5.append(num)
                qty += 1
            elif num < -5:
                num_less_neg5.append(num)
                qty += 1
    if qty == 0:
        print("нет чисел, удовлетворяющих условию")
    else:
        percent_greater_neg5 = (len(num_greater_neg5) / qty) * 100
        percent_less_neg5 = 100 - percent_greater_neg5
        len_bar_greater_neg5 = round(percent_greater_neg5 / 100 * width)
        len_bar_less_neg5 = width - len_bar_greater_neg5
        purple_bar = " " * len_bar_greater_neg5
        red_bar = " " * len_bar_less_neg5

        print(f"{PURPLE_BG}{purple_bar}{RESET} больше -5, но не "
              f"положительных: {percent_greater_neg5:.1f}%")
        print(f"{RED_BG}{red_bar}{RESET} меньше -5: "
              f"{percent_less_neg5:.1f}%")
    print()


def draw_graph_3x(height):
    width = height
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if x == round(y / 3):
                print(f"{WHITE_BG}{PIXEL}{RESET}", end="")
            else:
                print(PIXEL, end="")
        print()
    print()


if __name__ == "__main__":
    draw_japan_flag(20, True, 4)
    draw_pattern_g(6, 5)
    draw_diagram("sequence.txt")
    draw_graph_3x(10)
