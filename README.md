### Manage Module-Odoo
this is my first time creating a module in odoo, it is based in scrum model, more or less, basically connect tasks, sprints and technologies, the views are simples, I use tree and form type views.

# Odoo

![](data:image/png;base64,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)

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

### Requiermensts
You have to have installed odoo in your computer, you can try download odoo from their oficial page  [odoo desktop](http:/https://www.odoo.com/es_ES/page/download/ "odoo desktop").

### Reference images

Image:

![](https://github.com/David203009/Manage-Module-Odoo/blob/master/img/Screenshot%202023-07-16%20222659.png)




###End
