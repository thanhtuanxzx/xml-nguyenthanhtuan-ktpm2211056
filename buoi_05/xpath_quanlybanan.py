from lxml import etree

tree = etree.parse("quanlybanan.xml")
root = tree.getroot()

print("\n1. Danh sách tất cả bàn")
for b in root.xpath("/RESTAURANT/BAN/B"):
    tenban = b.findtext("TENBAN")
    soban = b.findtext("SOBAN")
    print("-", tenban, "| Số bàn:", soban)

print("\n2. Danh sách tất cả nhân viên")
for nv in root.xpath("/RESTAURANT/NHANVIEN/NV"):
    manv = nv.findtext("MANV")
    tennv = nv.findtext("TENVN")
    gioitinh = nv.findtext("GIOITINH")
    print("-", manv, "|", tennv, "| Giới tính:", gioitinh)

print("\n3. Danh sách tất cả tên món")
for tenmon in root.xpath("/RESTAURANT/MON/M/TENMON/text()"):
    print("-", tenmon)

print("\n4. Tên nhân viên có mã NV02")
tennv = root.xpath("/RESTAURANT/NHANVIEN/NV[MANV='NV02']/TENVN/text()")
print(tennv[0] if tennv else "Không tìm thấy nhân viên NV02")

print("\n5. Lấy tên và số điện thoại của nhân viên có mã NV03")
ten = root.xpath("/RESTAURANT/NHANVIEN/NV[MANV='NV03']/TENVN/text()")[0]
sdt = root.xpath("/RESTAURANT/NHANVIEN/NV[MANV='NV03']/SDT/text()")[0]
print("Tên:", ten, "| SĐT:", sdt)

print("\n6. Tên món có giá > 50,000")
for tenmon in root.xpath("/RESTAURANT/MON/M[number(GIA) > 50000]/TENMON/text()"):
    print("-", tenmon)

print("\n7. Số bàn của hóa đơn HD03")
tenban = root.xpath("/RESTAURANT/HOADON/HD[SOHD='HD03']/TENBAN/text()")
print(tenban[0] if tenban else "Không tìm thấy hóa đơn HD03")

print("\n8. Tên món có mã M02")
tenmon = root.xpath("/RESTAURANT/MON/M[MAMON='M02']/TENMON/text()")
print(tenmon[0] if tenmon else "Không tìm thấy món M02")

print("\n9. Ngày lập của hóa đơn HD03")
ngaylap = root.xpath("/RESTAURANT/HOADON/HD[SOHD='HD03']/NGAYLAP/text()")
print(ngaylap[0] if ngaylap else "Không tìm thấy hóa đơn HD03")

print("\n10. Tất cả mã món trong hóa đơn HD01")
for mamon in root.xpath("/RESTAURANT/CTHD/CT[SOHD='HD01']/MAMON/text()"):
    print("-", mamon)

print("\n11. Tên món trong hóa đơn HD01")
for tenmon in root.xpath("/RESTAURANT/MON/M[MAMON=/RESTAURANT/CTHD/CT[SOHD='HD01']/MAMON]/TENMON/text()"):
    print("-", tenmon)

print("\n12. Tên nhân viên lập hóa đơn HD02")
tennv = root.xpath("/RESTAURANT/NHANVIEN/NV[MANV=/RESTAURANT/HOADON/HD[SOHD='HD02']/MANV]/TENVN/text()")
print(tennv[0] if tennv else "Không tìm thấy hóa đơn HD02")

print("\n13. Tổng số bàn")
print(int(root.xpath("count(/RESTAURANT/BAN/B)")))

print("\n14. Số hóa đơn lập bởi nhân viên NV01")
sohd = int(root.xpath("count(/RESTAURANT/HOADON/HD[MANV='NV01'])"))
print(sohd)

print("\n15. Tên tất cả món có trong hóa đơn của bàn số 2")
for tenmon in root.xpath("/RESTAURANT/MON/M[MAMON=/RESTAURANT/CTHD/CT[SOHD=/RESTAURANT/HOADON/HD[TENBAN='B02']/SOHD]/MAMON]/TENMON/text()"):
    print("-", tenmon)

print("\n16. Nhân viên từng lập hóa đơn cho bàn số 3")
for ten in root.xpath("/RESTAURANT/NHANVIEN/NV[MANV=/RESTAURANT/HOADON/HD[TENBAN='B03']/MANV]/TENVN/text()"):
    print("-", ten)

print("\n17. Hóa đơn do nhân viên NỮ lập")
for hd in root.xpath("/RESTAURANT/HOADON/HD[MANV=/RESTAURANT/NHANVIEN/NV[GIOITINH='Nu']/MANV]"):
    sohd = hd.findtext("SOHD")
    manv = hd.findtext("MANV")
    print("-", sohd, "| Mã NV:", manv)

print("\n18. Nhân viên từng phục vụ bàn số 1")
for ten in root.xpath("/RESTAURANT/NHANVIEN/NV[MANV=/RESTAURANT/HOADON/HD[TENBAN='B01']/MANV]/TENVN/text()"):
    print("-", ten)

print("\n19. Các món được gọi nhiều hơn 1 lần trong các hóa đơn")
for tenmon in root.xpath("/RESTAURANT/MON/M[MAMON=/RESTAURANT/CTHD/CT[number(SOLUONG) > 1]/MAMON]/TENMON/text()"):
    print("-", tenmon)

print("\n20. Thông tin bàn và ngày lập hóa đơn HD02")
tenban = root.xpath("/RESTAURANT/HOADON/HD[SOHD='HD02']/TENBAN/text()")[0]
ngaylap = root.xpath("/RESTAURANT/HOADON/HD[SOHD='HD02']/NGAYLAP/text()")[0]
print("Bàn:", tenban, "| Ngày lập:", ngaylap)