import sys


def tail_file(filename, lines_count=10):
    try:
        with open(filename, 'r') as f:
            content = f.readlines()
            return content[-lines_count:]
    except FileNotFoundError:
        print(f"tail: {filename}: No such file or directory", file=sys.stderr)
        return None
    except PermissionError:
        print(f"tail: {filename}: Permission denied", file=sys.stderr)
        return None


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        multiple = len(files) > 1

        for i, filename in enumerate(files):
            if multiple:
                if i > 0:
                    print()
                print(f"==> {filename} <==")

            lines = tail_file(filename)
            if lines:
                for line in lines:
                    print(line.rstrip())
    else:
        lines = sys.stdin.readlines()
        for line in lines[-17:]:
            print(line.rstrip())


if __name__ == "__main__":
    main()
