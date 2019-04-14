import xml.etree.ElementTree as ET

tree = ET.parse('0414_xml.xml')
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('update', 'yes')

tree.write('0414_xml.xml')

# 刪除
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('0414_output.xml')
