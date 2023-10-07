def read_csv(filename, delimiter=','):
    with open(filename) as file:
        headers = file.readline().strip().split(delimiter)
        result = {header: [] for header in headers}
        for line in file:
            line = line.strip().split(delimiter)
            for k, v in zip(headers, line):
                result[k].append(v)
    return result
