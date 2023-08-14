import yaml


class Config:

    def __init__(self, url, element, template, type, save):
        self.url = url
        self.element = element
        self.template = template
        self.type = type
        self.save = save

    def get_url(self):
        return self.url

    def get_element(self):
        return self.element

    def get_template(self):
        return self.template

    def get_type(self):
        return self.type

    def get_save(self):
        return self.save


class Element:
    def __init__(self, element, subelements):
        self.element = element
        self.subelements = subelements

    def get_element(self):
        return self.element

    def get_subelements(self):
        return self.subelements


def parse_yaml_config(file):
    with open(file, "r") as stream:
        try:
            yaml_file = yaml.safe_load(stream)
            conf_obj = Config(yaml_file.get("url"), yaml_file.get("element"), "", "", "")
            return conf_obj
        except yaml.YAMLError as exc:
            return ""


def parse_element_string(element):
    """
    Parses element string given in config into a Python object
    :param element: Given in the config file
    :return: Structure of the given element as Python object
    """
    element_list = []
    element_string = ""
    for c in element:
        if c != "[" and c != ',' and c != ']':
            element_string = element_string + c
        else:
            if len(element_list) == 0:
                element_list.append((element_string, "element"))
            else:
                element_list.append((element_string, "subelement"))

            element_string = ""

    elem = element_list[0][0]
    subelems = []

    for e in element_list:
        if e[1] == "subelement":
            subelems.append(e[0])

    return Element(elem, subelems)
