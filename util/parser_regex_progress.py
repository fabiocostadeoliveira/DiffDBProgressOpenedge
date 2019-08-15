import re
from util.regex_consts import RegexUtil


def get_valor_generico(data, prop_name, regex_prop, default):
    if prop_name in data:
        try:
            lista_res = regex_prop.findall(data[prop_name][0])
        except Exception as e:
            print('Erro ao executar regex com os dados {0} prop_name {1}'.format(data, prop_name))
            print('Exception: ', e)
            return default
        if len(lista_res) >= 1:
            valor = lista_res
        else:
            valor = default
    else:
        valor = default
    return valor


class ParserRegexProgress:

    def __init__(self, match_iterator):
        self.data = self.dict_regex(match_iterator)

    def dict_regex(self, p_match_iterator):
        obj = dict()
        for matchNum, match in enumerate(p_match_iterator, start=1):
            tupla = tuple(filter(lambda x: x is not None, match.groups()))

            if match.lastgroup in obj:
                lista = list()
                for t in obj[match.lastgroup]:
                    if type(t) == tuple:
                        lista.append(t[0])
                    else:
                        lista.append(t)
                lista.append(tupla[0])
                tupla = tuple(lista)
                obj[match.lastgroup] = tupla
            else:
                obj[match.lastgroup] = tupla
        return obj

    def first_value_string(self, prop_name, default=None):
        regex_prop = re.compile(RegexUtil.REGEX_PROP_STRING)
        res = get_valor_generico(self.data, prop_name, regex_prop, default)
        if type(res) == bool:
            return res
        if res is not None and len(res) > 0:
            return res[0]
        return res

    def group_value(self, prop_name, default=None, all=False):
        res = self.get_data_by_id(prop_name)
        if res is not None:
            if all is False and type(res) is tuple:
                return res[0]
            else:
                return res
        return default

    def exist_property(self, prop_name, default=None):
        if self.get_data_by_id(prop_name) is not None:
            return True
        return default

    def get_data(self):
        return self.data

    def get_data_by_id(self, id):
        return self.data.get(id, None)
