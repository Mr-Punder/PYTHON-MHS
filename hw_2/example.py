from latex_gen import generate_table
import os


def main():
    os.chdir(os.path.dirname(__file__))
    data = [
        ["Name", "Age", "City"],
        ["Alice", 25, "Moscow"],
        ["Bob", 30, "SPb"],
        ["Charlie", 35, "Kazan"]
    ]

    table_tex = generate_table(data)

    document = "\\documentclass{article}\n\\begin{document}\n\n" + table_tex + "\n\n\\end{document}"

    with open("artifacts/table.tex", "w") as f:
        f.write(document)

    print("Generated table.tex")


if __name__ == "__main__":
    main()
