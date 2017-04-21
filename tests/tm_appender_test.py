import pytest

from habr_proxy.utils import TMAppender


class TMAppenderTest:
    @pytest.mark.parametrize(("raw_text", "expected_text"), [
        ("Python 3.5+", "Python™ 3.5+"),
        ("страницы должны отображаться и работать полностью корректно, в точности так,"
         " как и оригинальные (за исключением модифицированного текста);",
         "страницы должны™ отображаться и работать полностью корректно, в точности так,"
         " как и оригинальные (за исключением модифицированного текста™);"),
        ("Если задачу удалось сделать быстро, и у вас еще остался энтузиазм - как насчет написания тестов?",
         "Если задачу™ удалось сделать быстро™, и у вас еще остался энтузиазм - как насчет™ написания тестов™?"),
        ("Текст без изменений, но  пробелы    !", "Текст без изменений, но  пробелы    !"),
        ("если в условиях вам не хватает каких-то данных, опирайтесь на здравый смысл.",
         "если в условиях вам не хватает каких-то данных™, опирайтесь на здравый смысл."),
        ("Как-то так", "Как-то™ так"),
        ("Hadn't oh!", "Hadn't™ oh!"),
        ("Числа не считаются 666666", "Числа не считаются 666666"),
        ("Уже с ТМ Python™ 3.5+", "Уже с ТМ Python™ 3.5+")
    ])
    def test_add_tm_to_words_with_special_len(self, raw_text, expected_text):
        tm_appender = TMAppender(special_len=6)

        modified_text = tm_appender.get_modified_text(raw_text)
        assert modified_text == expected_text
