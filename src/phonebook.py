class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido' #BUG - estava escrito "Nme" fugindo do padrão que deve ser "Nome"
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido' #BUG - estava escrito "invalio" fugindo do padrão que deve ser "invalido"
        if '%' in name:
            return 'Nome invalido'

        #BUG - essa condição não valida corretamente a string do número
        #if len(number) < 0:
        if not number or not number.isdigit():
            return 'Numero invalido' #Estava escrito "invalid" fugindo do padrão que deve ser "invalido"

        # BUG - Se o nome for igual a um ja cadastrado, ele retorna mesmo assim, então o return deveria ser dentro do if
        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'

        #return 'Numero adicionado'
        #Adicionado um return para caso o nome já esteja cadastrado
        return 'Nome ja cadastrado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invalido' #BUG - estava escrito "invaldo" fugindo do padrão que deve ser "invalido"
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido' #BUG - estava escrito "Nme" fugindo do padrão que deve ser "Nome"
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido' #BUG - estava escrito "nvalido" fugindo do padrão que deve ser "invalido"

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """

        #BUG - não está retornando uma lista das chaves,. Indicação de colocar o retorno detro de um list() para retornar uma lita com as chaves
        #return self.entries.keys()
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        #BUG - o padrão do retorno não está no formato de lista e sim no formato de chaves de dicionário, o que causa um retorno estranho para um usuário.
        #Indicação de colocar o retorno detro de um list() para retornar uma lita com as chaves
        #return self.entries.values()
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """

        #BUG - não está retornando o telefone junto do nome que foi pesquisado, está retornando todos os outros do dicionário, menos o pesquisado.
        result = []
        for name, number in self.entries.items():
            #if search_name not in name:
            if search_name in name:
                result.append({name, number})
        return result

    #BUG - não está retornando o resultado em ordem
    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return sorted(self.entries)

    # BUG - não está retornando o resultado em ordem invertida
    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return list(reversed(sorted(self.entries)))

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, name, number):
        if name in self.entries:
            self.entries[name] = number
            return "Numero alterado"
        return "Contato nao encontrado"

    def get_name_by_number(self, number):
        for name in self.entries:
            if self.entries[name] == number:
                return name
        return "Numero nao encontrado"