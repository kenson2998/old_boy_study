import xml.etree.ElementTree as ET

tree = ET.parse('0414_xml.xml')
root = tree.getroot()
print(root.tag)

for child in root:  ## 遍歷root
    print('child.tag:{} ,child.attrib:{}'.format(child.tag, child.attrib))
    for i in child:
        print('i.tag:{} ,i.text:{} ,child.attrib:{}'.format(i.tag, i.text, i.attrib))

for node in root.iter('year'):  # 遍歷單一節點
    print(node.tag, node.text)
