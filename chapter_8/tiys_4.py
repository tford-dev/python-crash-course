"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file
called printing_functions.py. Write an import statement at the top of printing_models.py, and
modify the file to use the imported functions.
"""
import tiys_0;

#tiys_0.name_of_user();

"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a
separate file. Import the function into your main program file, and call the function using each
of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
import tiys_3;
tiys_3.make_car('toyota', 'camry', color='green', tow_package=True);

from tiys_1 import process_terminated;
process_terminated();

from tiys_1 import user_albums as ua;
ua();

import tiys_0 as f0;
f0.kanye_tracks("power", "through the wire", "touch the sky");

from tiys_3 import *;
process_terminated();