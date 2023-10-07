def write_csv(data, filename, delimiter=','):
    with open(filename, 'w') as file:
        headers = delimiter.join(data.keys())
        lines = [delimiter.join(map(str, col)) for col in zip(*data.values())]
        
        content = '\n'.join(lines)
        content = f"{headers}\n{content}"

        file.write(content)