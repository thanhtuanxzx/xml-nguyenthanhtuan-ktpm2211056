from lxml import etree

xml_file = "supplier_catalog.xml"
xsd_file = "supplier_catalog.xsd"

xml_doc = etree.parse(xml_file)
xsd_doc = etree.parse(xsd_file)
xsd_schema = etree.XMLSchema(xsd_doc)

if xsd_schema.validate(xml_doc):
    print("✅ XML hợp lệ với XSD.")
else:
    print("❌ XML không hợp lệ.")
    print(xsd_schema.error_log)
