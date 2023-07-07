import os
import lxml.etree as ET

# 获取当前目录路径
py_dir = os.getcwd()
# 输入的 XML 文件路径
input_xml_file = f"{py_dir}\input.xml"
# 输出的 DITA 文件路径
output_dita_file = f"{py_dir}\output.dita"
# XSL 文件路径
xsl_file = f"{py_dir}\XSLs\db2dita\docbook2dita.xsl"

print('请将 Docbook 格式的文件重命名为 input.xml，并放在与 main.py 文件相同的文件夹中。')
print('在 input.xml 文件中，请只保留 article 块。')
print(f"脚本使用的 XSL 文件位于: {xsl_file}。")
print("要转换为其他格式，您还可以修改此脚本以使用其他 XSL 文件。")
print('脚本将输出 DITA 格式的文件为 output.dita，并放在与 main.py 文件相同的文件夹中。')
input('按 Enter 键开始转换...')

# 解析 XSL 文件
xslt = ET.parse(xsl_file)
transform = ET.XSLT(xslt)
# 解析输入的 XML 文件
input_dom = ET.parse(input_xml_file)
# 使用 XSLT 转换
output_dom = transform(input_dom)

output_DITA_contents = str(output_dom)

# 需要替换的字符串列表
replace_list = [
    " outputclass=\"db.article\"",
    " outputclass=\"db.para\"",
    " outputclass=\"db.orderedlist\"",
    " outputclass=\"db.unorderedlist\"",
    " outputclass=\"db.listitem\"",
    " outputclass=\"db.informaltable\"",
    " outputclass=\"db.tgroup\"",
    " outputclass=\"db.tbody\"",
    " outputclass=\"db.row\"",
    " outputclass=\"db.entry\"",
    " outputclass=\"db.anchor\""
]

while True:
    # 逐个替换字符串
    for i in replace_list:
        output_DITA_contents = output_DITA_contents.replace(i, "")
    break

# 将转换结果写入输出的 DITA 文件
with open(output_dita_file, 'w', encoding='utf-8') as f:
    f.write(output_DITA_contents)

print('转换完成。')