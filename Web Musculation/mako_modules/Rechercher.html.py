# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1591556034.469384
_enable_loop = True
_template_filename = 'modeles/Rechercher.html'
_template_uri = 'Rechercher.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        erreur = context.get('erreur', UNDEFINED)
        variable1 = context.get('variable1', UNDEFINED)
        variable3 = context.get('variable3', UNDEFINED)
        variable2 = context.get('variable2', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <head>\r\n        <meta charset="utf-8" />\r\n        <link rel="stylesheet" href="css/style.css" />\r\n        <title>Muscul-site</title>\r\n\t</head>\r\n        <body>\r\n            <header>\r\n\t\t\t<h1>Muscul-site</h1>\r\n            <h3>Un appli web pour un amateur de musculation</h3>\r\n\t\t\t<hr/>\r\n\t\t\t</header>\r\n\t\t\t<p1>Bonjour, bienvenu dans notre site! Ici vous pouvez créer votre programme de formation et voir les programme d\'autre personne.</p1>\r\n\t\t\t<button type="submit" onclick="help()">règle d\'utilise</button><br/><hr/>\r\n\t\t\t<script>\r\n\t\t\t\tfunction help(){\r\n\t\t\t\t\talert("Quand vous ajoutez, pas besoin de ID. Quand vous supprimez, complétez seulement ID.\\nN\'écrivez pas des caractères spéciaux.\\nQuand vous créez une programme, vous pouvez écrire plusieurs ID de parcitipant et d\'exercice, séparer avec <;>, mais au moins écrire un ID de parcitipant.\\nTous les input texts de <nom> ou <prénom> ne pouvent pas être null.")\r\n\t\t\t\t}\r\n\t\t\t</script>\r\n\t\t\t<a href="/index">Accueil</a>\r\n\t\t\t<a href="/static/AS.html">Ajouter/Supprimer</a>\r\n\t\t\t<a href="/static/Rechercher.html">Rechercher</a>\r\n\t\t\t</br><hr/>\r\n            <form method="get" action="../ReR">\r\n\t\t\t\tOrdre par ? \r\n\t\t\t\t<input name="ordre" type="radio" value="id" checked="checked"/>ID\r\n\t\t\t\t<input name="ordre" type="radio" value="id desc" />ID inverse\r\n\t\t\t\t<input name="ordre" type="radio" value="nom" />Nom\r\n\t\t\t\t<input name="ordre" type="radio" value="nom desc" />Nom inverse\r\n\t\t\t\t<hr/>\r\n\t\t\t    <input type="text" value="" name="textRe" />\r\n\t\t\t    <button type="submit" id="rechercher">Rechercher</button>\r\n\t\t\t\t<p>( Cliquer sans text va affichier tous les datas )</p>\r\n\t\t    </form>\r\n            <p2>liste des exercices : </p2>\r\n\t\t\t<table border="2">\r\n\t\t\t    <tr>\r\n\t\t\t\t    <th>ID d\'exercice</th>\r\n\t\t\t\t    <th>Nom d\'exercices</th>\r\n\t\t\t\t\t<th>Muscles visés</th>\r\n\t\t\t\t\t<th>Séries répétés</th>\r\n\t\t\t\t</tr>\r\n')
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
        __M_writer('            </table>\r\n\t\t\t</br>\r\n')
        if erreur:
            __M_writer('\t\t\t\t<script>help()</script>\r\n')
        __M_writer('            <footer>\r\n\t\t\t<hr/>\r\n            <h3>Soyer fort(e)!!! </h3>\r\n\t\t\t<p id="auteur">@2020 R&T Ziyi LIU</p>\r\n\t\t\t</footer>\r\n        </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "modeles/Rechercher.html", "uri": "Rechercher.html", "source_encoding": "utf-8", "line_map": {"16": 0, "25": 1, "26": 44, "27": 45, "28": 46, "29": 46, "30": 47, "31": 47, "32": 48, "33": 48, "34": 49, "35": 49, "36": 52, "37": 61, "38": 62, "39": 63, "40": 63, "41": 64, "42": 64, "43": 65, "44": 65, "45": 66, "46": 66, "47": 69, "48": 77, "49": 78, "50": 79, "51": 79, "52": 80, "53": 80, "54": 81, "55": 81, "56": 84, "57": 86, "58": 87, "59": 89, "65": 59}}
__M_END_METADATA
"""
