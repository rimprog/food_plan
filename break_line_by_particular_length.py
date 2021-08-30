def find_optimal_space_index_for_breakline(line, max_letters_before_break):
    space_indexes = []
    for index, letter in enumerate(line):
        if letter == ' ':
            space_indexes.append(index)

    for space_index in space_indexes[::-1]:
        first_part_line = line[:space_index]
        second_part_line = line[space_index + 1:]

        replaced_line = f'{first_part_line}\n{second_part_line}'

        line_length_prediction = len(replaced_line.split('\n')[-2])

        if line_length_prediction > max_letters_before_break:
            continue
        else:
            return space_index


def replace_optimal_space(line_letters, max_letters_before_break):
    line = ''.join(line_letters)
    optimal_space_index = find_optimal_space_index_for_breakline(line, max_letters_before_break)
    first_part_line = line[:optimal_space_index]
    try:
        second_part_line = line[optimal_space_index + 1:]
    except TypeError as error:
        raise TypeError(f'{error}. Variable max_letters_before_break must be more than len the biggest word in line')

    replaced_line = f'{first_part_line}\n{second_part_line}'
    replaced_line_letters = [letter for letter in replaced_line]


    return replaced_line_letters


def break_line_by_particular_length(line, max_letters_before_break=20, forced_line_break=False):
    new_line_letters = []
    for index, letter in enumerate(line, 1):
        new_line_letters.append(letter)

        if forced_line_break and index % max_letters_before_break == 0:
            new_line_letters.append('\n')
        elif not forced_line_break and index % max_letters_before_break == 0:
            new_line_letters = replace_optimal_space(new_line_letters, max_letters_before_break)

    last_remainder = ''.join(new_line_letters).split('\n')[-1]
    while len(last_remainder) > max_letters_before_break:
        new_line_letters = replace_optimal_space(new_line_letters, max_letters_before_break)
        last_remainder = ''.join(new_line_letters).split('\n')[-1]

    new_line = ''.join(new_line_letters)

    print(new_line)


def main():
    line = 'This is big recipe name. Very Big recipe name. Very very very big recipe name'
    break_line_by_particular_length(line, max_letters_before_break=20, forced_line_break=False)

if __name__ == '__main__':
    main()
