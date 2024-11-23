from src.phonebook import Phonebook
import pytest
class TestPhonebook:

    @pytest.mark.parametrize("test_data", [("Fulano", "1982304736"), ("Ciclano", "1992324352334")])
    def test_add_contact_success(self, test_data):
        # Setup
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(*test_data)

        # Validacao
        assert resultado == "Numero adicionado"

    @pytest.mark.parametrize("test_data",["Fu#lano", "@fulano", "f!lano", "fula%no", "la$ndo" ])
    def test_add_contact_special_character(self, test_data):
        # Setup
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(test_data, "1982304736")

        # Validacao
        assert  resultado == "Nome invalido"

    @pytest.mark.parametrize("test_data",[19912131415, 3.6888888, [], {}])
    def test_add_contact_invalid_number(self, test_data):
        # Setup
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add("Fulaninho", test_data)

        # Validacao
        assert resultado == "Numero invalido"

    def test_add_contact_that_already_exist_in_db(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fulaninho", "19912345678")

        # Chamada
        resultado = phonebook.add("Fulaninho", "19912345678")

        # Validacao
        assert resultado == "Nome ja existe"

    def test_lookup_contact_success(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fulaninho", "19912345678")

        # Chamada
        resultado = phonebook.lookup("Fulaninho")

        # Validacao
        assert resultado == "19912345678"

    @pytest.mark.parametrize("test_data", ["Fu#lano", "@fulano", "f!lano", "fula%no", "la$ndo"])
    def test_lookup_contact_special_character(self, test_data):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fulaninho", "19912345678")

        # Chamada
        resultado = phonebook.add(test_data, "1982304736")

        # Validacao
        assert resultado == "Nome invalido"


    def test_get_names_success(self):
        # Setup
        phonebook = Phonebook()
        phonebook.add("Fulaninho", "19912345678")
        phonebook.add("Ciclaninho", "19912345678")

        # Chamada
        resultado = phonebook.get_names()

        assert isinstance(resultado, type(phonebook.entries.keys()))

