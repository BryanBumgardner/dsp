# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

from datetime import datetime
date_format = "%m-%d-%Y"
a = datetime.strptime('01-02-2013', date_format)
b = datetime.strptime('07-28-2015', date_format)
jinkies = b - a
jinkies.days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

from datetime import datetime
date_format = "%m%d%Y"
a = datetime.strptime('12312013', date_format)
b = datetime.strptime('05282015', date_format)
zoinks = b - a
zoinks.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

from datetime import datetime
date_format = "%d-%b-%Y"
a = datetime.strptime('15-Jan-1994', date_format)
b = datetime.strptime('14-Jul-2015', date_format)
gang = b - a
gang.days
