<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Kết quả truy vấn sinhvien.xml</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 20px; background: #f6f8fc; }
          h2 { background-color: #2a73cc; color: white; padding: 8px; border-radius: 6px; }
          table { border-collapse: collapse; width: 75%; margin-bottom: 30px; background: white; }
          th, td { border: 1px solid #ccc; padding: 6px 10px; }
          th { background-color: #e6ecff; }
        </style>
      </head>
      <body>
        <h1>KẾT QUẢ TRUY VẤN TỪ FILE SINHVIEN.XML</h1>

        <h2>1️. Danh sách sinh viên (Mã và Họ tên)</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th></tr>
          <xsl:apply-templates select="school/student" mode="cau1"/>
        </table>

        <h2>2️. Danh sách sinh viên sắp xếp theo điểm từ cao đến thấp</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th><th>Điểm</th></tr>
          <xsl:for-each select="school/student">
            <xsl:sort select="grade" data-type="number" order="descending"/>
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="grade"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>3️. Danh sách sinh viên sinh tháng gần nhau (theo ngày sinh)</h2>
        <table>
          <tr><th>STT</th><th>Họ tên</th><th>Ngày sinh</th></tr>
          <xsl:for-each select="school/student">
            <xsl:sort select="substring(date,6,2)" data-type="number"/>
            <xsl:variable name="pos" select="position()"/>
            <tr>
              <td><xsl:value-of select="$pos"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>4️. Danh sách các khóa học có sinh viên học (theo tên khóa)</h2>
        <table>
          <tr><th>Mã khóa</th><th>Tên khóa học</th></tr>
          <xsl:for-each select="school/course[id = /school/enrollment/courseRef]">
            <xsl:sort select="name"/>
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>5️. Danh sách sinh viên học môn "Hóa học 201"</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th><th>Khóa học</th></tr>
          <xsl:for-each select="school/enrollment[courseRef='c3']">
            <xsl:variable name="sv" select="studentRef"/>
            <tr>
              <td><xsl:value-of select="$sv"/></td>
              <td><xsl:value-of select="/school/student[id=$sv]/name"/></td>
              <td>Hóa học 201</td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>6️. Danh sách sinh viên sinh năm 1997</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th><th>Ngày sinh</th></tr>
          <xsl:for-each select="school/student[starts-with(date,'1997')]">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>7️. Danh sách sinh viên họ “Trần”</h2>
        <table>
          <tr><th>Mã SV</th><th>Họ tên</th></tr>
          <xsl:for-each select="school/student[starts-with(name,'Trần')]">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
            </tr>
          </xsl:for-each>
        </table>

      </body>
    </html>
  </xsl:template>

  <xsl:template match="student" mode="cau1">
    <tr>
      <td><xsl:value-of select="id"/></td>
      <td><xsl:value-of select="name"/></td>
    </tr>
  </xsl:template>

</xsl:stylesheet>
