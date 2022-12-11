from PyPDF2 import PdfFileMerger

pdf_merger = PdfFileMerger()

pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

# 按照字母順序對 PDF 文件進行排序
pdf_files.sort()

# 將 PDF 文件添加到 PdfFileMerger 對象中
for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

# 將合併後的 PDF 文件寫入磁盤
pdf_merger.write('merged_file.pdf')

# 關閉 PdfFileMerger 對象
pdf_merger.close()
