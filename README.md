# bond_html
You can include html in html without php and js.
## Usage
### hoge.html
```
<html>
	#BOND_HTML("bond.html")
	<body>This is test.</body>
</html>
```
### bond.html
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
