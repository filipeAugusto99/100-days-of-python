# Absolute Path
with open(r'\Users\filip_gxv027a\OneDrive\Documentos\new_file.txt') as file:
    contents = file.read()
    print(contents)

# Relative Path
with open(r'..\..\..\..\..\..\Users\filip_gxv027a\OneDrive\Documentos\new_file.txt') as file:
    contents = file.read()
    print(contents)