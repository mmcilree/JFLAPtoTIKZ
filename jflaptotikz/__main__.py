import xml.etree.ElementTree as ET
import sys
import argparse



parser = argparse.ArgumentParser(description = "Conver JFlap to Tikz Picture")
parser.add_argument("--jff", type=str, help="Jflap file to convert")
args = parser.parse_args()

if args.jff is None:
    print("Error: No jff file specified.")
    sys.exit(1)

tree = ET.parse(args.jff)
root = tree.getroot()

print("""
\\begin{figure}[ht]
\\centering
\\begin{tikzpicture}
"""
)

for element in root.find("automaton"):
    if(element.tag == "state"):
        nodeString = "\\node[state{pos}] at ({x}, {y}) (q{id}) {{$q_{id}$}};"
        elId=element.get("id")
        x = float(element.find("x").text)/80
        y = float(element.find("y").text)/80

        print(nodeString.format(pos="", id=elId, x=x, y=y))

print("""
\\end{tikzpicture}
\\end{figure}
"""
)