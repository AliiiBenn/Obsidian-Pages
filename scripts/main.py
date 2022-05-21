# import markdown, os


# class MardownFile:
#     def __init__(self, file):
#         self.file = file

#     def convert_to_string(self) -> str:
#         with open(self.file, 'r') as f:
#             text = f.read()
#         return text

# class ObsidianPage:
#     def __init__(self, file):
#         self.file = file
#         self.html_file = self.convert_to_html()

#     def convert_to_html(self):
#         return markdown.markdown(self.file)

#     def save_html_file(self):
#         filepath = os.path.join('web\\pages', "hello_world.html")
#         if not os.path.exists(filepath):
#             with open(filepath, 'w') as f:
#                 f.write(self.html_file)


# # print(markdown.markdown("""
# # # Hello World

# # hello, my name is **Markdown**.

# # - test
# # - test2"""))


# md = MardownFile('test.md')
# my_first_page = ObsidianPage(md.convert_to_string())
# my_first_page.save_html_file()


from flask import Flask, render_template

app = Flask(__name__, template_folder="../web/templates")

@app.route('/')
def hello_world():
    return "<h1>Hello World!</h1>"


if __name__ == '__main__':
    with app.app_context():
        rendered = render_template('blog.html', \
            title = "My Generated Page", \
            content = "Hello World")
        print(rendered)
