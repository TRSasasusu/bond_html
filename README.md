# bond_html
You can include html in html without php and js.
## Usage 1
### hoge.html
```
<html>
	#BOND_HTML("bond.btml")
	<body>This is test.</body>
</html>
```
### bond.btml
```
<head><title>bond_html</title></head>
```  
Then,  
```$ python bond_html.py hoge.html -o hoge_out.html```
### hoge_out.html
```
<html>
	<head><title>bond_html</title></head>
	<body>This is test.</body>
</html>
```
## Usage 2
### foo.html
```
<html>
	<body>
		This is foo.
#BOND_HTML("foobarbaz.btml", 1, "<li>FOO</li>")
	</body>
</html>
```
### bar.html
```
<html>
	<body>
		This is bar.
#BOND_HTML("foobarbaz.btml", 2, "<li>BAR</li>")
	</body>
</html>
```
### baz.html
```
<html>
	<body>
		This is baz.
#BOND_HTML("foobarbaz.btml", 3, "<li>BAZ</li>")
	</body>
</html>
```
### foobarbaz.btml
```
<li>foo</li>
<li>bar</li>
<li>baz</li>
```  
Then,  
```
$ python foo.html -o foo_out.html
$ python bar.html -o bar_out.html
$ python baz.html -o baz_out.html
```
### foo_out.html
```
<html>
	<body>
		This is foo.
<li>FOO</li>
<li>bar</li>
<li>baz</li>
	</body>
</html>
```
### bar_out.html
```
<html>
	<body>
		This is bar.
<li>foo</li>
<li>BAR</li>
<li>baz</li>
	</body>
</html>
```
### baz_out.html
```
<html>
	<body>
		This is baz.
<li>foo</li>
<li>bar</li>
<li>BAZ</li>
	</body>
</html>
```
