class sintaxe:
    UPDATE_TABLE = "UPDATE TABLE \"{tableName}\" "
    UPDATE_FIELD = "UPDATE FIELD \"{fieldName}\" of \"{tableName}\" "
    ADD_FIELD = ("ADD TABLE \"{name}\" \n"
                 " LABEL \"{label}\"\n"
                 " DESCRIPTION \"{description}\"\n"
                 " DUMP-NAME \"{dumpname}\" \n")
    PROP_NOT_QUOTE = "  {prop_name} {prop_value}\n"
    PROP_QUOTE = "  {prop_name} \"{prop_value}\"\n"
    PROP_NONE = "  {prop_name}\n"
    ADD_TABLE_ALL = "ADD TABLE \"{tableName}\"\n{properties}"
    ADD_FIELD_ALL = "ADD FIELD \"{fieldName}\" OF \"{tableName}\" AS {type}\n{properties}"
    ADD_INDEX_ALL = "ADD INDEX \"{indexName}\" ON \"{tableName}\"\n{properties}{fields}"
    INDEX_FIELD = "  INDEX-FIELD \"{fieldName}\" {properties}\n"
    RENAME_INDEX = "RENAME INDEX \"{indexName}\" ON \"{tableName}\" TO \"{newName}\"\n"
    RENAME_FIELD = "RENAME FIELD \"{fieldName}\" OF \"{tableName}\" TO \"{newName}\"\n"
    DROP_INDEX = "DROP INDEX \"{indexName}\" ON \"{tableName}\"\n"

