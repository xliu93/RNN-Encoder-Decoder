import torch


def read_data(filename):
    lines = []
    with open(filename, 'r') as fp:
        i = 0
        for line in fp:
            if i % 100 == 0:
                line = line.lower().replace("'", " ").replace(".", "").replace("?", "")\
                    .replace("!", "").replace(":", "").replace(";", "")
                lines.append(line)
            i += 1
    fp.close()
    return lines
