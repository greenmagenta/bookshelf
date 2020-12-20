import json

def read_json(file):
	# load json file
	with open(file) as f:
		data = json.load(f)
		f.close()
	return data

def config(file):
	global head_lang, head_title, head_favicon
	global display_title, display_description, display_theme, display_highlightjs_theme
	global build_index, build_meta, build_require_main_stylesheet, build_require_main_script, build_require_dep_stylesheet, build_require_dep_script

	data = read_json(file)
	head_lang = data["head"]["lang"]
	head_title = data["head"]["title"]
	head_favicon = data["head"]["favicon"]

	display_title = data["display"]["title"]
	display_description = data["display"]["description"]
#	display_bottom = data["display"][""]
	display_theme = data["display"]["theme"]
	display_highlightjs_theme = data["display"]["highlightjs_theme"]

	build_index = data["build"]["index"]
	build_meta = data["build"]["meta"]
	build_require_main_stylesheet = data["build"]["require"]["main"]["stylesheet"]
	build_require_main_script = data["build"]["require"]["main"]["script"]
	build_require_dep_stylesheet = data["build"]["require"]["dep"]["stylesheet"]
	build_require_dep_script = data["build"]["require"]["dep"]["script"]

def index(file):
	global index_sections, index_items

	data = read_json(file)
	index_sections = []
	index_items = []
	for i in range(len(data["index"])):
		index_sections.append(data["index"][i]["section"])

		a = []
		for j in range(len(data["index"][i]["items"])):
			b = []
			b.append(data["index"][i]["items"][j]["title"])
			b.append(data["index"][i]["items"][j]["src"])
			a.append(b)
		index_items.append(a)