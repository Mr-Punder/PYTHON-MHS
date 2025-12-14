import sys


def count_stats(content):
    lines = content.count('\n')
    words = len(content.split())
    bytes_count = len(content.encode('utf-8'))
    return lines, words, bytes_count


def format_output(lines, words, bytes_count, filename=None):
    if filename:
        print(f"{lines:>8}{words:>8}{bytes_count:>8} {filename}")
    else:
        print(f"{lines:>8}{words:>8}{bytes_count:>8}")


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        total_lines = 0
        total_words = 0
        total_bytes = 0

        for filename in files:
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                lines, words, bytes_count = count_stats(content)
                format_output(lines, words, bytes_count, filename)

                total_lines += lines
                total_words += words
                total_bytes += bytes_count
            except FileNotFoundError:
                print(f"wc: {filename}: No such file or directory", file=sys.stderr)
            except PermissionError:
                print(f"wc: {filename}: Permission denied", file=sys.stderr)

        if len(files) > 1:
            format_output(total_lines, total_words, total_bytes, "total")
    else:
        content = sys.stdin.read()
        lines, words, bytes_count = count_stats(content)
        format_output(lines, words, bytes_count)


if __name__ == "__main__":
    main()
