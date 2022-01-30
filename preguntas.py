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
    ntbl = tbl2.copy()
    ntbl["_c5"] = ntbl["_c5a"].astype(str)+":"+ ntbl["_c5b"].astype(str)
    unicos = sorted(tbl2["_c0"].unique())
    lista_nums = []
    dic = {}
    for elems in unicos:
        lista = list(ntbl.groupby('_c0').get_group(elems)['_c5'])
        lista.sort()
        lista_nums.append("".join([str(_)+',' for _ in lista]).strip(','))

    dic['_c0'] = unicos
    dic['_c5'] = lista_nums
    ans = pd.DataFrame(dic)
    return ans


def pregunta_13():
    ntbl = pd.merge(tbl0, tbl2, on="_c0")
    ntbl = ntbl[["_c1", "_c5b"]]
    ans = ntbl.groupby('_c1').sum()
    return ans["_c5b"]