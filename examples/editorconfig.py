from configbuilder.builder.editorconfig import EditorConfigBuilder

print EditorConfigBuilder(None, root='true')

print EditorConfigBuilder(
    '*',
    charset='utf-8',
    indent_size=4,
    end_of_line='lf',
    indent_style='space',
    insert_final_newline='true',
    trim_trailing_whitespace='true'
)

print EditorConfigBuilder('*.html', indent_size=4)
