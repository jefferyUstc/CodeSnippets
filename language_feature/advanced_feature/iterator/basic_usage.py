def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line)
        except StopIteration:
            print('**the end**')


if __name__ == '__main__':
    manual_iter()
    # with open('/etc/passwd') as f:
    #     while True:
    #         line = next(f, None)
    #         if line is None:
    #             break
    #         print(line)
