from anytree import Node, RenderTree
from anytree.exporter import DotExporter

udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)
udo = Node("Udo", parent=marc)

for pre, fill, node in RenderTree():
    print("%s%s" % (pre, node.name))

DotExporter(udo).to_picture("udo.png")

