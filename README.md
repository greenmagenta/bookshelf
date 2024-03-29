# bookshelf <sup>beta</sup>
📚 Ready-to-deploy markdown static documentation builder.

> Build a clean and structured documentation in minutes,<br>
> including diagrams, flowcharts and many more !

### Features

- Markdown-inherited features
- Fenced code blocks
- Editables sections structure
- Mermaid integration
- Customizable themes

## Get started

**Note** : Python 3.6 or higher is required.

```bash
# clone the repository
$ git clone https://github.com/greenmagenta/bookshelf.git

# change the working directory to bookshelf
$ cd bookshelf

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```

### Run template

```bash
# run doc builder
$ bookshelf.py

# then open "index.html"
```

## Usage

> Learn about usage by reading [documentation](https://boardens.github.io/bookshelf).

Bookshelf allow you to easily build any documentation by writing all your pages in markdown. Once the builder is configured, each time you'll want to add, update or remove a page, you'll only need to update the index file and push your generated html in production.

#### Summary

- [Configuration](#Configuration)
  - [Head](#Head)
  - [Display](#Display)
  - [Build](#Build)
- [Indexing pages](#Indexing-pages)
  - [Pages](#Pages)
  - [Sections](#Sections)

<hr>

### Configuration

You can configure general website behaviors and displays by editing `config/config.json`.

#### Head

```json
"head":{
  "lang":"en",
  "title":"Lorem ipsum",
  "favicon":null
},
```

| Argument | Description |
|---|---|
| `lang` | Web page language indice |
| `title` | Web page title |
| `favicon` | Web page favicon |

#### Display

```json
"display":{
  "title":"Lorem ipsum",
  "description":"Sit dolore amet et saepe adrium venit.",
  "theme":"default.css",
  "highlightjs_theme":"github-gist.min.css"
},
```

| Argument | Description |
|---|---|
| `title` | Documentation title |
| `description` | Documentation description |
| `theme` | Custom color theme |
| `highlightjs_theme` | Synthax highlighting theme<br>[Find theme list here](https://highlightjs.org/static/demo/) |


#### Build

```json
"build":{
  "index":"config/index.json",
  "meta":"config/meta.php",
  "require":{
    "main":{
      "stylesheet":["css/style.css","css/themes/{theme}"],
      "script":["js/main.js"]
    },
    "dep":{
      "stylesheet":[
        "https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/styles/{highlightjs_theme}"
      ],
      "script":[
        "https://code.jquery.com/jquery-3.5.1.min.js",
        "https://unpkg.com/ionicons@5.1.2/dist/ionicons.js",
        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.2/highlight.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.6.4/mermaid.min.js"
      ]
    }
  }
}
```


| Argument | Description |
|---|---|
| `index` | Index file source |
| `meta` | Meta list source |
| `require` | Lists of requirements |

| Argument | Description |
|---|---|
| `main` | Main stylesheets and scripts |
| `dep` | Dependencies from CDN for stylesheets and scripts |

---

### Indexing pages

You can configure sections organisation and pages indexing by editing `config/config.json`.<br>

```json
{
  "index":[
    {
      "section":"Lorem ipsum",
      "items":[
        {
          "title":"Hello world",
          "src":"index.md"
        },
        {
          "title":"Components",
          "src":"components.md"
        }
      ]
    }
  ]
}
```

#### Pages

> Please note that the first page should be indexed as `index.md`.

```json
{
  "title":"Lorem ipsum",
  "src":"lorem-ipsum.md"
}
```

| Argument | Description |
|---|---|
| `title` | Page title |
| `src` | Source markdown file |

#### Sections

```json
{
  "section":"Lorem ipsum",
  "items":[]
}
```

| Argument | Description |
|---|---|
| `section` | Section title |
| `items` | List of pages in this section |

## Deployment

To deploy your documentation, you only have to push in production your `css` folder, `js` folder and your html generated files.

> All external dependencies are automatically included in html generated files.

```
doc
├── index.html
├── ...
├── js
|   └── main.js
└── css
    ├── style.css
    └── themes
        └── default.css
```

If you're using FTP pushes, take a look at [git-ftp](https://github.com/git-ftp/git-ftp).

## License

[GPL-3.0](https://github.com/greenmagenta/bookshelf/LICENSE/) License
