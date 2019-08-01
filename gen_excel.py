import xlsxwriter
import db_manager
import glob

EXCEL_PATH = "resources/bottle_image.xlsx"
DB_PATH = "resources/dbs"


def gen_excel():
    workbook = xlsxwriter.Workbook(EXCEL_PATH)
    for tb in db_manager.get_all_tables():
        worksheet = workbook.add_worksheet(name=tb)

        worksheet.write("A1", "Image name")
        worksheet.write("B1", "Tag")
        worksheet.write("C1", "Action")
        row = 1
        results = db_manager.get_all(tb)
        for i in results:
            row += 1
            worksheet.write(f"A{row}", i[0])
            worksheet.write(f"B{row}", i[1])
            worksheet.write(f"C{row}", i[2])
    workbook.close()


if __name__ == "__main__":
    gen_excel()
