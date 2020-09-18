# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1591444786.4419198
_enable_loop = True
_template_filename = 'modeles/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        variable3 = context.get('variable3', UNDEFINED)
        variable1 = context.get('variable1', UNDEFINED)
        erreur = context.get('erreur', UNDEFINED)
        variable2 = context.get('variable2', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <head>\r\n        <meta charset="utf-8" />\r\n        <link rel="stylesheet" href="css/style.css" />\r\n        <title>Muscul-site</title>\r\n    </head>\r\n        <body>\r\n            <header>\r\n\t\t\t<h1>Muscul-site</h1>\r\n            <h2>Un appli web pour un amateur de musculation</h2>\r\n\t\t\t<hr/>\r\n\t\t\t</header>\r\n\t\t\t<p1>Bonjour, bienvenu dans notre site! Ici vous pouvez créer votre programme de formation et voir les programme d\'autre personne.</p1>\r\n\t\t\t<button type="submit" onclick="help()">règle d\'utilise</button><br/><hr/>\r\n\t\t\t<script>\r\n\t\t\t\tfunction help(){\r\n\t\t\t\t\talert("Quand vous ajoutez, pas besoin de ID. Quand vous supprimez, complétez seulement ID.\\nN\'écrivez pas des caractères spéciaux.\\nQuand vous créez une programme, vous pouvez écrire plusieurs ID de parcitipant et d\'exercice, séparer avec <;>, mais au moins écrire un ID de parcitipant.\\nTous les input texts de <nom> ou <prénom> ne pouvent pas être null.")\r\n\t\t\t\t}\r\n\t\t\t</script>\r\n\t\t\t<a href="/index">Accueil</a>\r\n\t\t\t<a href="/static/AS.html">Ajouter/Supprimer</a>\r\n\t\t\t<a href="/static/Rechercher.html">Rechercher</a>\r\n\t\t\t</br><hr/>\r\n\t\t\t<p2>liste des exercices : </p2>\r\n\t\t\t<table border="2">\r\n\t\t\t    <tr>\r\n\t\t\t\t    <th>ID d\'exercice</th>\r\n\t\t\t\t    <th>Nom d\'exercices</th>\r\n\t\t\t\t\t<th>Muscles visés</th>\r\n\t\t\t\t\t<th>Séries répétés</th>\r\n\t\t\t\t</tr>\r\n')
        for a,b,c,d in variable1 :
            __M_writer('                    <tr>\r\n                        <td>')
            __M_writer(str(a))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(str(b))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(str(c))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(d))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('\t\t\t</table></br>\r\n\t\t\t<p2>liste des programme : </p2>\r\n\t\t\t<table border="2">\r\n\t\t\t    <tr>\r\n\t\t\t\t    <th>ID d\'programme</th>\r\n\t\t\t\t    <th>Nom d\'programme</th>\r\n\t\t\t\t\t<th>Exercices contenu</th>\r\n\t\t\t\t\t<th>Nombre participant</th>\r\n\t\t\t\t</tr>\r\n')
        for a,b,c,d in variable2 :
            __M_writer('                    <tr>\r\n                        <td>')
            __M_writer(str(a))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(str(b))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(str(c))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            __M_writer(str(d))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table></br>\r\n            <p2>liste des participant : </p2>\r\n\t\t\t<table border="2">\r\n\t\t\t    <tr>\r\n\t\t\t\t    <th>ID d\'participant</th>\r\n\t\t\t\t    <th>Nom</th>\r\n\t\t\t\t\t<th>Prénom</th>\r\n\t\t\t\t</tr>\r\n')
        for a,b,c in variable3 :
            __M_writer('                    <tr>\r\n                        <td>')
            __M_writer(str(a))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(str(b))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(str(c))
            __M_writer('</td>\r\n                    </tr>\r\n')
        __M_writer('            </table>\r\n')
        if erreur:
            __M_writer('\t\t\t\t<script>help()</script>\r\n')
        __M_writer('            <footer>\r\n\t\t\t<hr/>\r\n            <h3>Soyer fort(e)!!! </h3>\r\n\t\t\t</footer>\r\n        </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "modeles/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"16": 0, "25": 1, "26": 33, "27": 34, "28": 35, "29": 35, "30": 36, "31": 36, "32": 37, "33": 37, "34": 38, "35": 38, "36": 41, "37": 50, "38": 51, "39": 52, "40": 52, "41": 53, "42": 53, "43": 54, "44": 54, "45": 55, "46": 55, "47": 58, "48": 66, "49": 67, "50": 68, "51": 68, "52": 69, "53": 69, "54": 70, "55": 70, "56": 73, "57": 74, "58": 75, "59": 77, "65": 59}}
__M_END_METADATA
"""
