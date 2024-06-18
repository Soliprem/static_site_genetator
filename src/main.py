import os
import shutil
from blocks import markdown_to_html_node


def replacetree(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination) if not os.path.exists(
        destination) else print(f"{destination} exists")
    listdir = os.listdir(source)
    for item in listdir:
        if os.path.isfile(os.path.join(source, item)):
            shutil.copy(os.path.join(source, item),
                        os.path.join(destination, item))
        else:
            replacetree(os.path.join(source, item),
                        os.path.join(destination, item))


def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for i in split_markdown:
        if i.startswith("# "):
            return i
    raise Exception("No fucking title present, you dumbass")


def generate_page(from_path, template_path, dest_path):
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    if not os.path.dirname(dest_path):
        os.makedirs(os.path.dirname(dest_path))
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    titled = template.replace("{{ Title }}", title)
    html = titled.replace("{{ Content }}", content)
    with open(dest_path, "w") as f:
        f.write(html)


def main():
    replacetree('static', 'public')
    generate_page("content/index.md", "template.html", "public/index.html")


main()
