from sintaxe import sintaxe


def dif_index_fields(index1, index2) -> str:
    if dif_order(index1, index2):
        return str_index_fields(index1)
    return ''


def dif_order(index1, index2) -> bool:
    dif = False
    for ifield in index1.indexField:
        dif = index1.indexField[ifield].seq != index2.indexField[ifield].seq
        if dif:
            break
    return dif


def str_index_fields(index) -> str:
    str_index_field = ""
    for ifield in index.indexField:
        index_field = index.indexField[ifield]
        props = index_field.order
        if index_field.abbreviated:
            props += " " + "ABBREVIATED"
        str_index_field += sintaxe.INDEX_FIELD.format(fieldName=index_field.fieldName, properties=props)
    return str_index_field
