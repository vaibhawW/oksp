from pydocx import PyDocX
import markdown2

class HTMLifier():

    def __init__(self, image_base_path='.', doc_base_path='.'):
        self.doc_base_path = doc_base_path

    def convert(self, doc_file):
        file_name = str(doc_file)
        ext = file_name.split('.')[-1]
        file_name = file_name[:len(file_name)-len(ext)-1]
        doc_dir = self.doc_base_path

        if ext[:3] == 'doc':
            html = HTMLifier.doc_convert(doc_file)
        elif ext in ('md', 'markdown'):
            html = HTMLifier.md_convert(doc_file)

        with open(doc_dir + file_name + '.html', 'wb') as doc_stored:
            doc_stored.write(bytes(html,'utf-8'))

    def doc_convert(doc_file):
        return PyDocX.to_html(doc_file)

    def md_convert(doc_file):
        tmp_loc = '/tmp/md_uploaded.md'

        with open(tmp_loc,'wb') as md:
            for chunk in doc_file.chunks():
                md.write(chunk)

        return markdown2.markdown_path(tmp_loc)
