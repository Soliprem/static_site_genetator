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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    os.mkdir(dest_dir_path) if not os.path.exists(
        dest_dir_path) else print(f"{dest_dir_path} exists")
    listdir = os.listdir(dir_path_content)
    for item in listdir:
        if os.path.isfile(os.path.join(dir_path_content, item)):
            generate_page(os.path.join(dir_path_content, item), template_path,
                          os.path.join(
                dest_dir_path, item.replace(".md", ".html")))
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), "template.html",
                                     os.path.join(dest_dir_path, item))


def main():
    replacetree('static', 'public')
    generate_pages_recursive("content/", "template.html", "public/")


main()
