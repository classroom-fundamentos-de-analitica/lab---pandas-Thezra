"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    ans = tbl0.shape[0]
    return ans


def pregunta_02():
    ans = len(tbl0.columns)
    return ans


def pregunta_03():
    ans = tbl0.pivot_table(columns=['_c1'], aggfunc='size')
    return ans


def pregunta_04():
    ntbl = tbl0[["_c1", "_c2"]]
    ans = ntbl.groupby('_c1').mean()
    return ans["_c2"]


def pregunta_05():
    ntbl = tbl0[["_c1", "_c2"]]
    ans = ntbl.groupby('_c1').max()
    return ans["_c2"]


def pregunta_06():
    ntbl = tbl1["_c4"].unique()
    ans = [elem.upper() for elem in ntbl]
    return sorted(ans)


def pregunta_07():
    ntbl = tbl0[["_c1", "_c2"]]
    ans = ntbl.groupby('_c1').sum()
    return ans["_c2"]


def pregunta_08():
    ntbl = tbl0.copy()
    ntbl["suma"] = ntbl["_c0"] + ntbl["_c2"]
    return ntbl


def pregunta_09():
    ntbl = tbl0.copy()
    ntbl["year"] = ntbl["_c3"].str[:4]
    return ntbl


def pregunta_10():
    ntbl = tbl0[["_c1", "_c2"]]
    unicos = sorted(tbl0["_c1"].unique())
    lista_nums = []
    dic = {}
    for elems in unicos:
        lista = list(ntbl.groupby('_c1').get_group(elems)['_c2'])
        lista.sort()
        lista_nums.append( "".join([str(_)+':' for _ in lista]).strip(':'))

    dic['lista'] = lista_nums
    ans = pd.DataFrame({"_c2": lista_nums}, index=pd.Series(unicos, name="_c1"))
    return ans


def pregunta_11():
    ntbl = tbl1[["_c0", "_c4"]]
    unicos = sorted(tbl1["_c0"].unique())
    lista_nums = []
    dic = {}
    for elems in unicos:
        lista = list(ntbl.groupby('_c0').get_group(elems)['_c4'])
        lista.sort()
        lista_nums.append( "".join([str(_)+',' for _ in lista]).strip(','))

    dic['_c0'] = unicos
    dic['_c4'] = lista_nums
    ans = pd.DataFrame(dic)
    return ans


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    return


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    return
