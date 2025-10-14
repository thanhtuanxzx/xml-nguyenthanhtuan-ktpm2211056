from lxml import etree
import mysql.connector
from mysql.connector import Error

XML_FILE = "supplier_catalog.xml"
XSD_FILE = "supplier_catalog.xsd"

try:
    xml_doc = etree.parse(XML_FILE)
    print("Đã parse file XML thành công")
except Exception as e:
    print(f"Lỗi khi đọc XML: {e}")
    exit()

try:
    xsd_doc = etree.parse(XSD_FILE)
    schema = etree.XMLSchema(xsd_doc)
    print("Đã parse file XSD & tạo XMLSchema object thành công")
except Exception as e:
    print(f"Lỗi khi đọc hoặc biên dịch XSD: {e}")
    exit()

print("\nKiểm tra tính hợp lệ của XML...")
if not schema.validate(xml_doc):
    print("XML KHÔNG hợp lệ!")
    for error in schema.error_log:
        print(f"Dòng {error.line}: {error.message}")
    exit()
else:
    print("XML hợp lệ với XSD! Tiếp tục xử lý...\n")

def connect_ampps_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",  
            database="ecommerce",
            port=3306
        )
        if conn.is_connected():
            print("Kết nối MySQL AMPPS thành công!")
            return conn
    except Error as e:
        print(f"Lỗi kết nối MySQL: {e}")
        return None


def insert_with_xpath(xml_doc, conn):
    cursor = conn.cursor()

    categories = xml_doc.xpath("//categories/category")
    print(f"Tìm thấy {len(categories)} categories.")

    for cat in categories:
        cat_id = cat.get("id")
        cat_name = cat.text.strip()
        cursor.execute("""
            INSERT INTO categories (id, name)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE name = VALUES(name)
        """, (cat_id, cat_name))
        print(f"Category: {cat_id} - {cat_name}")

    products = xml_doc.xpath("//products/product")
    print(f"\nTìm thấy {len(products)} products.")

    for prod in products:
        prod_id = prod.get("id")
        category_ref = prod.get("categoryRef")
        name = prod.xpath("./name/text()")[0].strip()
        price = float(prod.xpath("./price/text()")[0])
        currency = prod.xpath("./price/@currency")[0]
        stock = int(prod.xpath("./stock/text()")[0])

        cursor.execute("""
            INSERT INTO products (id, name, price, currency, stock, category_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
              name = VALUES(name),
              price = VALUES(price),
              currency = VALUES(currency),
              stock = VALUES(stock),
              category_id = VALUES(category_id)
        """, (prod_id, name, price, currency, stock, category_ref))
        print(f"Product: {prod_id} - {name} ({category_ref})")

    conn.commit()
    print("\nĐồng bộ dữ liệu hoàn tất!")

if __name__ == "__main__":
    conn = connect_ampps_mysql()
    if conn:
        insert_with_xpath(xml_doc, conn)
        conn.close()
