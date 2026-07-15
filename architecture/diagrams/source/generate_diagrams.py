from pathlib import Path
import subprocess


ARCH_DIR = Path(__file__).parent


diagrams = [
    "system_architecture",
    "data_flow",
    "sequence_diagram"
]


def generate_png(name):

    input_file = ARCH_DIR / f"{name}.mmd"
    output_file = ARCH_DIR / f"{name}.png"

    command = [
        "npx",
        "-p",
        "@mermaid-js/mermaid-cli",
        "mmdc",
        "-i",
        str(input_file),
        "-o",
        str(output_file),
        "-b",
        "transparent"
    ]

    subprocess.run(command)

    print(f"Generated: {output_file}")


for diagram in diagrams:
    generate_png(diagram)


print("All diagrams generated successfully!")