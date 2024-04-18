from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(loader=PackageLoader("relatorio"), autoescape=select_autoescape())

template = env.get_template("base.jinja")

lista = [{"href": "word", "caption": "wort"}, {"href": "nome", "caption": "andre"}]

conteudo = template.render(palavra="texto", navigation=lista)

print(conteudo)
