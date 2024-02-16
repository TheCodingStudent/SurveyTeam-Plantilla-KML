attributes: dict[str, str] = {}
attribute_counter: int = 0

title = input('Titulo: ')

while True:
    try:
    # exit_loop = input('Añadir atributo? (y/n)')
    # if exit_loop.lower() not in ('y', ''): break
        attribute = input(f'Atributo {attribute_counter+1}: ')
        name = input(f'Nombre del atributo "{attribute}": ')
        attributes[name.title()] = attribute.title()
        attribute_counter += 1
    except KeyboardInterrupt:
        break
    # print(attributes)


with open('atributo_plain.txt', 'r') as f:
    base_attribute = f.read().strip()

table_rows: list[str] = [] 
for name, attribute in attributes.items():
    result_attribute = base_attribute.replace('##NAME##', name)
    result_attribute = result_attribute.replace('##ATTRIBUTE##', attribute)
    table_rows.append(result_attribute)
table = '\n'.join(table_rows)

with open('plantilla_plain.txt', 'r') as f:
    template = f.read().strip()
    result = template.replace('##CONTENT##', table)
    result = result.replace('##TITLE##', title)

with open('plantilla_generada.xml', 'w') as f:
    f.write(result)