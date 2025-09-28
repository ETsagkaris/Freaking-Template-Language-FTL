{
  "name": "ftl-ext",
  "version": "0.0.1",
  "description": "Support for ftl syntax coloring",
  "engines": {
    "vscode": "^1.100.0"
  },
  "displayName": "FTL Extension",
  "categories": [
    "Programming Languages"
  ],
  "contributes": {
    "languages": [
      {
        "id": "ftl",
        "aliases": [
          "Freaking Template Language",
          "ftl"
        ],
        "extensions": [
          ".ftl"
        ],
        "configuration": "./language-configuration.json"
      }
    ],
    "grammars": [
      {
        "language": "ftl",
        "scopeName": "source.ftl",
        "path": "./syntaxes/ftl.tmLanguage.json"
      }
    ],
    "themes": [
      {
        "label": "FTL Dark Theme",
        "uiTheme": "vs-dark",
        "path": "./themes/ftl-color-theme.json"
      }
    ]
  }
}