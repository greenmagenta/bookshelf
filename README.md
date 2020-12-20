# bookshelf
📚 Ready-to-deploy markdown documentation builder.

> Build a clean and structured documentation in minutes,<br>
> including tables, flowcharts and many more !

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

| | |
|---|---|
| `lang` | Global language indice |
| `title` |  |
| `favicon` |  |

#### Display

```json
"display":{
  "title":"Lorem ipsum",
  "description":"Sit dolore amet et saepe adrium venit.",
  "theme":"default.css",
  "highlightjs_theme":"github-gist.min.css"
},
```

| | |
|---|---|
| `title` |  |
| `description` |  |
| `theme` |  |
| `highlightjs_theme` |  |


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

| | |
|---|---|
| `index` |  |
| `meta` |  |
| `require` |  |

| | |
|---|---|
| `main` |  |
| `dep` |  |

### Indexing pages

You can configure sections and pages indexing by editing `config/config.json`.

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

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
