# bookshelf
📚 Ready-to-deploy markdown documentation builder.

> Build a clean and structured documentation in minutes,<br>
> including tables, flowcharts and many more !

> Try bookshelf on [live demo](https://boardens.github.io/bookshelf-demo/) !

### Features

- Markdown-inherited features
- Fenced code blocks
- Full width tables
- Mermaid flowcharts
- Customizable themes

## Get started

**Note** : Python 3.6 or higher is required.

```bash
# clone the repository
$ git clone https://github.com/boardens/bookshelf.git

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

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur porttitor, ipsum eu condimentum sagittis, mauris lorem dignissim quam, vel suscipit nisl magna quis nisl. Morbi tempus mollis quam ac iaculis. Donec faucibus orci in dolor placerat sollicitudin. Nunc ante massa, hendrerit dignissim velit eget, dictum rutrum tellus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed condimentum, diam a laoreet porta, urna urna iaculis sapien, sit amet tristique sapien risus nec nibh. Suspendisse pulvinar purus nibh, in feugiat felis porta nec. Etiam ac tortor ut neque interdum eleifend non et dui. Mauris nec faucibus sem.

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

You can configure many website behaviors by editing `config/config.json`.

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

You can configure sections and pages indexing by editing `config/config.json`.<br>

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

### Pages

Please note that the first page should be indexed as `index.md`.

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

### Sections

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

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
