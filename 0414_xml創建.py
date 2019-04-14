import xml.etree.ElementTree as ET

new_xml = ET.Element('namelist')
name = ET.SubElement(new_xml, 'name', attrib={"enrolled":"yes"})
age = ET.SubElement(name, 'age', attrib={"checked":"no"})
sex = ET.SubElement(name, 'sex')
sex.text = '30'

name2 = ET.SubElement(new_xml, 'name', attrib={"enrolled":"no"})
age = ET.SubElement(name2, 'age')
age.text = '20'

et = ET.ElementTree(new_xml) # 生成文檔對象
et.write('0414_test.xml', encoding='utf-8', xml_declaration=True) #xml_declaration：聲明是xml格式的文檔
ET.dump(new_xml) #打印生成的格式