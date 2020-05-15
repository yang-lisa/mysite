import yaml

class ParseYaml:

    def __init__(self):
        pass

    def parse_yaml(self):
        f = open('./data/data.yaml', encoding='utf-8')
        res = yaml.load(f, Loader=yaml.FullLoader)
        print(res)
        f.close()
        return res


if __name__ == "__main__":
    pyaml = ParseYaml()
    pyaml.parse_yaml()
