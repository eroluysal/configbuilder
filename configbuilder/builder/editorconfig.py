from configbuilder.builder.base import BaseIniBuilder


class EditorConfigBuilder(BaseIniBuilder):
    #
    # indent_style: set to tab or space to use hard tabs or soft tabs
    # respectively.
    #
    # indent_size: a whole number defining the number of columns used for each
    # indentation level and the width of soft tabs (when supported). When set
    # to tab, the value of tab_width (if specified) will be used.
    #
    # tab_width: a whole number defining the number of columns used to
    # represent a tab character. This defaults to the value of indent_size and
    # doesn't usually need to be specified.
    #
    # end_of_line: set to lf, cr, or crlf to control how line breaks are
    # represented.
    #
    # charset: set to latin1, utf-8, utf-8-bom, utf-16be or utf-16le to
    # control the character set. Use of utf-8-bom is discouraged.
    #
    # trim_trailing_whitespace: set to true to remove any whitespace characters
    # preceding newline characters and false to ensure it doesn't.
    #
    # insert_final_newline: set to true to ensure file ends with a newline when
    # saving and false to ensure it doesn't.
    #
    # root: special property that should be specified at the top of the file
    # outside of any sections. Set to true to stop .editorconfig files search
    # on current file.
    #
    available_commands = (
        'root',
        'charset',
        'indent_size',
        'end_of_line',
        'indent_style',
        'insert_final_newline',
        'trim_trailing_whitespace',
    )
    available_values = {
        'root': ('true', 'false'),
        'charset': ('latin1', 'utf-8', 'utf-8-bom', 'utf-16be', 'utf-16le'),
        'indent_size': (1, 2, 3, 4),
        'end_of_line': ('lf', 'cr', 'crlf'),
        'indent_style': ('space', 'tab'),
        'insert_final_newline': ('true', 'false'),
        'trim_trailing_whitespace': ('true', 'false'),
    }
