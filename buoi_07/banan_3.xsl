<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Kết quả truy vấn – Quản lý bàn ăn</title>
        <style>
          body { font-family: Arial, sans-serif; background-color: #f6f8fc; margin: 20px; }
          h2 { background-color: #2a73cc; color: white; padding: 8px; border-radius: 6px; }
          table { border-collapse: collapse; width: 75%; margin-bottom: 30px; background: white; }
          th, td { border: 1px solid #aaa; padding: 6px 10px; }
          th { background-color: #e7eefc; }
        </style>
      </head>
      <body>
        <h1>KẾT QUẢ TRUY VẤN TỪ FILE QUANLYBANAN.XML</h1>

        <h2>1️. Danh sách tất cả các bàn</h2>
        <table>
          <tr><th>STT</th><th>Số bàn</th><th>Tên bàn</th></tr>
          <xsl:for-each select="QUANLY/BANS/BAN">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="SOBAN"/></td>
              <td><xsl:value-of select="TENBAN"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>2️. Danh sách các nhân viên</h2>
        <table>
          <tr><th>STT</th><th>Mã NV</th><th>Tên NV</th><th>Giới tính</th><th>Địa chỉ</th><th>SĐT</th></tr>
          <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MANV"/></td>
              <td><xsl:value-of select="TENV"/></td>
              <td><xsl:value-of select="GIOITINH"/></td>
              <td><xsl:value-of select="DIACHI"/></td>
              <td><xsl:value-of select="SDT"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>3️. Danh sách các món ăn</h2>
        <table>
          <tr><th>STT</th><th>Mã món</th><th>Tên món</th><th>Giá</th></tr>
          <xsl:for-each select="QUANLY/MONS/MON">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MAMON"/></td>
              <td><xsl:value-of select="TENMON"/></td>
              <td><xsl:value-of select="GIA"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>4️. Thông tin nhân viên NV02</h2>
        <table>
          <tr><th>Mã NV</th><th>Tên NV</th><th>Giới tính</th><th>Địa chỉ</th><th>SĐT</th></tr>
          <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']">
            <tr>
              <td><xsl:value-of select="MANV"/></td>
              <td><xsl:value-of select="TENV"/></td>
              <td><xsl:value-of select="GIOITINH"/></td>
              <td><xsl:value-of select="DIACHI"/></td>
              <td><xsl:value-of select="SDT"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>5️. Các món ăn có giá > 50,000</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th><th>Giá</th></tr>
          <xsl:for-each select="QUANLY/MONS/MON[GIA &gt; 50000]">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="TENMON"/></td>
              <td><xsl:value-of select="GIA"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>6️. Thông tin hóa đơn HD03</h2>
        <table>
          <tr><th>Tên nhân viên</th><th>Số bàn</th><th>Ngày lập</th><th>Tổng tiền</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD03']">
            <xsl:variable name="nv" select="MANV"/>
            <tr>
              <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=$nv]/TENV"/></td>
              <td><xsl:value-of select="SOBAN"/></td>
              <td><xsl:value-of select="NGAYLAP"/></td>
              <td><xsl:value-of select="TONGTIEN"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>7️. Tên các món ăn trong hóa đơn HD02</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']/CTHDS/CTHD">
            <xsl:variable name="ma" select="MAMON"/>
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=$ma]/TENMON"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>8️. Tên nhân viên lập hóa đơn HD02</h2>
        <table>
          <tr><th>Tên nhân viên</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']">
            <xsl:variable name="nv" select="MANV"/>
            <tr><td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=$nv]/TENV"/></td></tr>
          </xsl:for-each>
        </table>

        <h2>9️. Tổng số bàn</h2>
        <p><b>Số bàn: </b> <xsl:value-of select="count(QUANLY/BANS/BAN)"/></p>

        <h2>10. Số hóa đơn lập bởi NV01</h2>
        <p><b>Số hóa đơn: </b> <xsl:value-of select="count(QUANLY/HOADONS/HOADON[MANV='NV01'])"/></p>

        <h2>11️. Các món từng bán cho bàn số 2</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN=2]/CTHDS/CTHD">
            <xsl:variable name="ma" select="MAMON"/>
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=$ma]/TENMON"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>12️. Nhân viên từng lập hóa đơn cho bàn số 3</h2>
        <table>
          <tr><th>STT</th><th>Tên nhân viên</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN=3]">
            <xsl:variable name="nv" select="MANV"/>
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=$nv]/TENV"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>13️. Các món ăn được gọi nhiều hơn 1 lần trong các hóa đơn</h2>
        <table>
          <tr><th>Tên món</th></tr>
          <xsl:for-each select="QUANLY/MONS/MON">
            <xsl:variable name="ma" select="MAMON"/>
            <xsl:if test="sum(/QUANLY/HOADONS/HOADON/CTHDS/CTHD[MAMON=$ma]/SOLUONG) &gt; 1">
              <tr><td><xsl:value-of select="TENMON"/></td></tr>
            </xsl:if>
          </xsl:for-each>
        </table>

        <h2>14️. Thông tin chi tiết hóa đơn HD04</h2>
        <table>
          <tr><th>Mã món</th><th>Tên món</th><th>Đơn giá</th><th>Số lượng</th><th>Thành tiền</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD04']/CTHDS/CTHD">
            <xsl:variable name="ma" select="MAMON"/>
            <xsl:variable name="gia" select="/QUANLY/MONS/MON[MAMON=$ma]/GIA"/>
            <xsl:variable name="sl" select="SOLUONG"/>
            <tr>
              <td><xsl:value-of select="$ma"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=$ma]/TENMON"/></td>
              <td><xsl:value-of select="$gia"/></td>
              <td><xsl:value-of select="$sl"/></td>
              <td><xsl:value-of select="$gia * $sl"/></td>
            </tr>
          </xsl:for-each>
        </table>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
