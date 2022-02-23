pics: font
	/usr/bin/python3 ./make_res.py
font:
	/usr/bin/python3 ./font_builder.py
	
pics-only:
	/usr/bin/python3 ./make_res.py

plg:
	/usr/bin/python3  -m PyQt5.uic.pyuic -x plugin/test.ui -o plugin/test.py

#/usr/lib/x86_64-linux-gnu/qt5/plugins/designer