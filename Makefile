pics: font
	/usr/bin/python3 ./make_res.py
font:
	/usr/bin/python3 ./font_builder.py

buttons:
	/usr/bin/python3 ./code_button.py
	
pics-only:
	/usr/bin/python3 ./make_res.py

plg:
	/usr/bin/python3  -m PyQt5.uic.pyuic -x test/test.ui -o test/test.py
	/usr/bin/python3 test/test.py

plagin-git:
	cp plugin /home/shubin/electronic/firmware/mks-robin/my/Marlin/.pio/firmware/

#/usr/lib/x86_64-linux-gnu/qt5/bin/designer
