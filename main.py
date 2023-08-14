from ConfigHandler.Config import parse_yaml_config, parse_element_string
from DocHandler.DocHandler import create_files, create_files_docx
from WebHandler.WebHandler import get_site_content, find_site_content


def start():
    config = parse_yaml_config("Configuration\\miekkailu.yaml")
    element = parse_element_string(config.element)
    html = get_site_content(config.url)
    content = find_site_content(html, element, "fencing")
    create_files_docx(content)


if __name__ == '__main__':
    start()


