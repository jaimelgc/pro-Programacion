# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    last_item = ""
    result = []
    for num in items:
        if num != last_item:
            last_item = num
            result.append(num)

    return result


if __name__ == "__main__":
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
