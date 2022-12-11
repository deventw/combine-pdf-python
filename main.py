from PyPDF2 import PdfFileMerger

pdf_merger = PdfFileMerger()

pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

# 按照字母顺序对 PDF 文件进行排序
pdf_files.sort()

# 将 PDF 文件添加到 PdfFileMerger 对象中
for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

# 将合并后的 PDF 文件写入磁盘
pdf_merger.write('merged_file.pdf')

# 关闭 PdfFileMerger 对象
pdf_merger.close()
