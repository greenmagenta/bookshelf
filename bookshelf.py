from build import json_parser as parser
from build import html_ref as html

import markdown
import os.path

config = "config/config.json"
filetype = "html"

def parse_init(config_file):
	try:
		parser.config(config_file)
		parser.index(parser.build_index)
		return True
	except Exception as error:
		print(error)
		return False

def read_php(file):
	src = open(file, "r")
	content = src.read()
	src.close()

	return content.replace("\n", "")

def read_md(file):
	src = open(file, "r")
	content = src.read()
	src.close()

	convert_md = markdown.markdown(
		content,
		extensions=[
			"md_mermaid",
			"tables",
			"fenced_code"
		])

	return convert_md

def build_head(meta, title, favicon, stylesheets, theme, hjs_theme):
	f.write(html.head_open)
	f.write(read_php(meta))

#	meta = {'meta':meta}
#	f.write(html.head_meta_include.format(**meta))

	title = {'title':title}
	f.write(html.head_title.format(**title))

	if favicon is not None:
		favicon = {'favicon':favicon}
		f.write(html.head_favicon.format(**favicon))

	for i in range(len(stylesheets)):
		child_theme = {'theme':theme}
		highlightjs_theme = {'highlightjs_theme':hjs_theme}
		current_stylesheet = {'stylesheet':stylesheets[i].format(**child_theme, **highlightjs_theme)}
		f.write(html.head_link.format(**current_stylesheet))

	f.write(html.head_close)

def build_feets(scripts):
	for i in range(len(scripts)):
		current_script = {'script':scripts[i]}
		f.write(html.base_script.format(**current_script))

def build_article(content):
	f.write(html.body_open)
	f.write(html.body_article_open)
	f.write(content)
	f.write(html.body_article_close)
	f.write(html.body_close)

def build_sidebar_top(title, description):
	main_title = {'title':title}
	main_desc = {'description':description}
	f.write(html.body_top.format(**main_title, **main_desc))

def build_sidebar_index(sections, items):
	f.write(html.body_sidebar_open)

	for i in range(len(sections)):
		current_section = {'section':sections[i]}
		f.write(html.body_sidebar_section_open.format(**current_section))
		for j in range(len(items[i])):
			current_item_title = {'title':items[i][j][0]}
			current_item_src = {'src':items[i][j][1].replace(".md","."+filetype)}
			if cp != "{src}".format(**current_item_src):
				f.write(html.body_sidebar_section_item.format(**current_item_title, **current_item_src))
			else:
				f.write(html.body_sidebar_section_item_active.format(**current_item_title, **current_item_src))

		f.write(html.body_sidebar_section_close)

	f.write(html.body_sidebar_close)


if parse_init(config):
	print("Initialized "+config)
	print("===========")

	for i in range(len(parser.index_sections)):
		for j in range(len(parser.index_items[i])):
			cp = parser.index_items[i][j][1].replace(".md","."+filetype)

			f = open(cp, "w")

			lang = {'lang':parser.head_lang}
			f.write(html.base_open.format(**lang))

			build_require_stylesheet = parser.build_require_dep_stylesheet+parser.build_require_main_stylesheet
			build_require_script = parser.build_require_dep_script+parser.build_require_main_script

			html_article = read_md(parser.index_items[i][j][1])

			build_head(
				parser.build_meta,
				parser.head_title,
				parser.head_favicon,
				build_require_stylesheet,
				parser.display_theme,
				parser.display_highlightjs_theme
				)
			build_article(html_article)
			build_sidebar_top(
				parser.display_title,
				parser.display_description
				)
			build_sidebar_index(
				parser.index_sections,
				parser.index_items
				)
			build_feets(build_require_script)

			f.write(html.base_close)
			f.close()

			print("Built "+cp+"")