base_open = "<!DOCTYPE html><html lang=\"{lang}\">"
base_close = "</html>"

base_script = "<script type=\"text/javascript\" src=\"{script}\"></script>"

# head
head_open = "<head>"
head_close = "</head>"

head_meta_include = "<?php require \"{meta}\";?>"
head_title = "<title>{title}</title>"
head_favicon = "<link rel=\"icon\" href=\"{favicon}\">"
head_link = "<link rel=\"stylesheet\" type=\"text/css\" href=\"{stylesheet}\">"

# body
body_open = "<body>"
body_close = "</body>"

body_article_open = "<div class=\"content\"><div class=\"article\"><div>"
body_article_close = "<br><button class=\"button\" onclick=\"move_to(0)\">Previous page</button>&nbsp;&nbsp;<button class=\"button\" onclick=\"move_to(1)\">Next page</button></div><br></div></div>"

# body_bottom = "<div class=\"bottom\">{description}</div>"

# sidebar
body_top = "<div class=\"top\"><div class=\"list\"><h5>{title}</h5><br><p>{description}</p></div></div>"

body_sidebar_open = "<div class=\"sidebar\"><div class=\"list\">"
body_sidebar_close = "<br><br></div></div><div class=\"side-action\"><p><a id=\"toggle-sidebar\"><ion-icon name=\"menu-outline\"></ion-icon></a></p></div>"
body_sidebar_section_open = "<span class=\"title\">{section}</span><ul>"
body_sidebar_section_close = "</ul><br>"
body_sidebar_section_item = "<li><a href=\"{src}\">{title}</a></li>"
body_sidebar_section_item_active = "<li><a class=\"active\" href=\"{src}\">{title}</a></li>"