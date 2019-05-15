from core.sintaxe import sintaxe


def rename_field(field1, field2) -> str:
    comando = sintaxe.RENAME_FIELD.format(
        fieldName=field2.name,
        tableName=field2.nameTable,
        newName=field2.name + '_old'
    ) + '\n'

    comando += field1.__str__()

    return comando
