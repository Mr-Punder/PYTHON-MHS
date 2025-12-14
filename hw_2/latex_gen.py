def generate_table(data):
    if not data or not data[0]:
        return ""

    num_cols = len(data[0])
    col_format = "|" + "|".join(["c"] * num_cols) + "|"

    header = "\\begin{table}[h]\n\\centering\n\\begin{tabular}{" + col_format + "}\n\\hline\n"

    rows = list(map(lambda row: " & ".join(map(str, row)) + " \\\\\n\\hline\n", data))

    footer = "\\end{tabular}\n\\end{table}"

    return header + "".join(rows) + footer
