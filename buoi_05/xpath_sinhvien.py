from lxml import etree

# Đọc file XML
tree = etree.parse("sinhvien.xml")
root = tree.getroot()

print("\n1. Lấy tất cả sinh viên ")
for sv in root.xpath("/school/student"):
    print(etree.tostring(sv, pretty_print=True, encoding='unicode'))

print("\n2. Liệt kê tên tất cả sinh viên ")
for name in root.xpath("/school/student/name/text()"):
    print("-", name)

print("\n3. Lấy tất cả id của sinh viên ")
print(root.xpath("/school/student/id/text()"))

print("\n4. Lấy ngày sinh của sinh viên có id='SV01' ")
print(root.xpath("/school/student[id='SV01']/date/text()"))

print("\n5. Lấy các khóa học ")
print(root.xpath("/school/enrollment/course/text()"))

print("\n6. Lấy toàn bộ thông tin của sinh viên đầu tiên ")
print(etree.tostring(root.xpath('/school/student[1]')[0], pretty_print=True, encoding='unicode'))

print("\n7. Lấy mã sinh viên đăng ký khóa học 'Vatly203' ")
print(root.xpath("/school/enrollment[course='Vatly203']/studentRef/text()"))

print("\n8. Lấy tên sinh viên học môn 'Toan101' ")
print(root.xpath("/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name/text()"))

print("\n9. Lấy tên sinh viên học môn 'Vatly203' ")
print(root.xpath("/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()"))

print("\n10. Lấy ngày sinh của sinh viên có id='SV01' ")
print(root.xpath("/school/student[id='SV01']/date/text()"))

print("\n11. Lấy tên và ngày sinh của sinh viên sinh năm 1997 ")
names = root.xpath("/school/student[starts-with(date,'1997')]/name/text()")
dates = root.xpath("/school/student[starts-with(date,'1997')]/date/text()")
for n, d in zip(names, dates):
    print("-", n, "—", d)

print("\n12. Lấy tên sinh viên có ngày sinh trước năm 1998 ")
for info in root.xpath("/school/student[number(substring(date,1,4)) < 1998]/name/text()"):
    print("-", info)

print("\n13. Đếm tổng số sinh viên ")
print(root.xpath("count(/school/student)"))

print("\n14. Lấy tất cả sinh viên chưa đăng ký môn nào ")
print(root.xpath("/school/student[not(id=/school/enrollment/studentRef)]/name/text()"))

print("\n15. Lấy phần tử <date> anh em ngay sau <name> của SV01")
for d in root.xpath("/school/student[id='SV01']/name/following-sibling::date"):
    print(etree.tostring(d, encoding='unicode').strip())

print("\n16. Lấy phần tử <id> anh em ngay trước <name> của SV02 ")
for i in root.xpath("/school/student[id='SV02']/name/preceding-sibling::id"):
    print(etree.tostring(i, encoding='unicode').strip())

print("\n17. Lấy toàn bộ node <course> trong cùng <enrollment> với studentRef='SV03' ")
for c in root.xpath("/school/enrollment[studentRef='SV03']/course"):
    print(etree.tostring(c, encoding='unicode').strip())

print("\n18. Lấy sinh viên có họ là 'Trần' ")
for name in root.xpath("/school/student[starts-with(name,'Trần')]/name/text()"):
    print("-", name)

print("\n19. Lấy năm sinh của sinh viên SV01 ")
print(root.xpath("substring(/school/student[id='SV01']/date,1,4)"))