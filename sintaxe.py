class sintaxe:
    UPDATE_TABLE = "UPDATE TABLE \"{tableName}\" "
    UPDATE_FIELD = "UPDATE {fieldName} of \"{tableName}\" "
    ADD_FIELD = ("ADD TABLE \"{name}\" \n"
                 " LABEL \"{label}\"\n"
                 " DESCRIPTION \"{description}\"\n"
                 " DUMP-NAME \"{dumpname}\" \n")
    PROP_NOT_QUOTE = "  {prop_name} {prop_value}\n"
    PROP_QUOTE = "  {prop_name} \"{prop_value}\"\n"
    PROP_NONE = "  {prop_name}\n"
    ADD_TABLE_ALL = "ADD TABLE \"{tableName}\"\n{properties}"
    ADD_FIELD_ALL = "ADD FIELD \"{fieldName}\" OF \"{tableName}\"\n{properties}"
