

class sintaxe:
    UPDATE_TABLE = "UPDATE TABLE \"{tableName}\" "
    UPDATE_FIELD = "UPDATE FIELD \"{fieldName}\" of \"{tableName}\" "
    ADD_FIELD = ("ADD TABLE \"{name}\" \n"
                 " LABEL \"{label}\"\n"
                 " DESCRIPTION \"{description}\"\n"
                 " DUMP-NAME \"{dumpname}\" \n\n")
    PROP_NOT_QUOTE = "  {prop_name} {prop_value}\n"
    PROP_FLAG = "  {prop_flag}\n"
    PROP_QUOTE = "  {prop_name} \"{prop_value}\"\n"
    PROP_NONE = "  {prop_name}\n"
    ADD_TABLE_ALL = "ADD TABLE \"{tableName}\"\n{properties}{triggers}\n"
    ADD_FIELD_ALL = "ADD FIELD \"{fieldName}\" OF \"{tableName}\" AS {type}\n{properties}\n"
    ADD_INDEX_ALL = "ADD INDEX \"{indexName}\" ON \"{tableName}\"\n{properties}{fields}\n"
    ADD_TRIGGER = "  TABLE-TRIGGER \"{event}\" {override} PROCEDURE \"{procedure}\" CRC \"{crc}\"\n"
    INDEX_FIELD = "  INDEX-FIELD \"{fieldName}\" {properties}\n"
    RENAME_INDEX = "RENAME INDEX \"{indexName}\" ON \"{tableName}\" TO \"{newName}\"\n"
    RENAME_FIELD = "RENAME FIELD \"{fieldName}\" OF \"{tableName}\" TO \"{newName}\"\n"
    DROP_INDEX = "DROP INDEX \"{indexName}\" ON \"{tableName}\"\n\n"
    DROP_TABLE = "DROP TABLE \"{tableName}\"\n\n"
    DROP_FIELD = "DROP FIELD \"{fieldName}\" ON \"{tableName}\"\n\n"
    DELETE_TRIGGER = "  TABLE-TRIGGER \"{event}\" DELETE\n"



