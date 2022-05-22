from flask import Flask, render_template
import markdown, os 
import sys
import unicodedata


def convert_markdown_to_string(mardown_file) -> str:
    with open(mardown_file, 'r') as mark:
        text = mark.read()
    return text


def convert_markdown_string_to_html(markdown_string):
    return markdown.markdown(markdown_string)

def create_new_page_structure(app, page_title, page_content):
    with app.app_context():
        rendered = render_template('blog.html', title=page_title, content=page_content)
    return rendered

def create_html_page(file_name, content):
    filepath = os.path.join('web/pages', f'{file_name}.html')
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(content)


markdown_string = convert_markdown_to_string("test.md")
html_string = convert_markdown_string_to_html(markdown_string)

# print(html_string)

app = Flask(__name__, template_folder="../web/templates")

page_structure = create_new_page_structure(app, 'test', html_string)

create_html_page('test', page_structure)