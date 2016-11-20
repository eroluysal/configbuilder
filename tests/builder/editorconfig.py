import unittest

from configbuilder.builder.editorconfig import EditorConfigBuilder


class EditorConfigTest(unittest.TestCase):
    def setUp(self):
        self.editorconfig = EditorConfigBuilder

    def test_without_section(self):
        value = self.editorconfig(None, root='true')
        self.assertEqual(value.__str__(), 'root = true\n')

    def test_with_section(self):
        value = self.editorconfig('*', charset='utf-8')
        self.assertEqual(value.__str__(), '[*]\ncharset = utf-8\n')

    def test_with_invalid_command(self):
        with self.assertRaises(AttributeError):
            self.editorconfig('*', foo=True)

    def test_with_invalid_value(self):
        with self.assertRaises(AttributeError):
            self.editorconfig('*', charset='foo')
