# SearchFile for Sublime Text

Official SearchFile plugin for Sublime Text.

* [How to install](#how-to-install)
* [Overriding keyboard shortcuts](#overriding-keyboard-shortcuts)
* [Config project path](#config-project-path)
* [How to use](#how-to-use)

## How to install
unsupport with Package Control

Manually:
1. Clone or download git repo into your packagesfolder(in Sublime Text,find Browse Packages...menu item to open this folder) with folder named `SearchFile`

2.Restart Sublime Text editor (if required)

##overriding keyboard shortcuts
Default keyboard shortcuts is `alt+m`.You can overrrding it as youself.

Open `sublime-keymap` file or click Sublime Text Menu button `Preferences` --> `Package Settings` --> `SearchFile` --> `Key Bindings-Default`

Then, change `alt+m` to you want keybord shortcuts

```js

[
  {
    "keys": ["alt+m"], "command": "searchfile"
  }
]

```

## Config project path

Before use search file, you should config two params in settings.

Open `sublime-keymap` file or click Sublime Text Menu button `Preferences` --> `Package Settings` --> `SearchFile` --> `Settings-Default`

just as follow:

```js
{
	//config project root path
	"root": "D:\\workspace",

	//enhance search intelligence, false represent for select full line path to search commod
	"enhance": true
}
```
1.root represent your project root path
2.enhance search ability default true, if you set it as false, you should select full line your path before press `alt+m`


## How to use

just point at file path string line just like follow

```css
@import url("toefl_ico.css");
@import url("toefl_crumb.css");
@import url("word/word.css");
@import url("toefl_ad.css");
@import url("learn/learn-ad.css");
```

then press `alt+m`, Sublime Text will open this relative file.

You can also point more files path with `ctrl` + click, then will open those files.

You can also open absolute path with project root path. just as
```css
/path_one/path_two/test.css
```
then it will open `root path` + /path_one/path_two/test.css


If file path is error or not find file, it will show error message.