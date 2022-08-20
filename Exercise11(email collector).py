#  Email Collector
# str = '''
# '''
# email1
# email2
# email3

import re
mystr = ''' Aadarsh	Jain	   0808EC201001.ies@ipsacademy.org
Aayush	Pandey	               0808EC201002.ies@ipsacademy.org
Abhay	Raj	                   0808EC201003.ies@ipsacademy.org
Adrija	Vishwakarma	           0808EC201004.ies@ipsacademy.org
Akash	Bagwan	               0808EC201005.ies@ipsacademy.org
Anubhav	Sharma	               0808EC201006.ies@ipsacademy.org
Balbhadra	Singh	           0808EC201007.ies@ipsacademy.org
Deepak	Patidar	0808EC201008.ies@ipsacademy.org
Dhananjay	Choudhary	0808EC201009.ies@ipsacademy.org
Harsha	Verma	0808EC201010.ies@ipsacademy.org
Hitendra	Singh	0808EC201011.ies@ipsacademy.org
Jay	Barode	0808EC201012.ies@ipsacademy.org
Kunal	Raikwar	0808EC201013.ies@ipsacademy.org
Mangesh	More	0808EC201014.ies@ipsacademy.org
Manish	Kumar	0808EC201015.ies@ipsacademy.org
Mittul	Shah	0808EC201016.ies@ipsacademy.org
Nisha	Digar	0808EC201017.ies@ipsacademy.org
Palash	Jain	0808EC201018.ies@ipsacademy.org
Pramod	Goswami	0808EC201019.ies@ipsacademy.org
Prashant	Jadam	0808EC201020.ies@ipsacademy.org
Raj	Jaiswal	0808EC201021.ies@ipsacademy.org
Reeti	Parmar	0808EC201022.ies@ipsacademy.org
Sandeep	Khelwal	0808EC201023.ies@ipsacademy.org
Srishti	Chhapre	0808EC201024.ies@ipsacademy.org
Surendra	Prajapat	0808EC201025.ies@ipsacademy.org
Tulsiram	Patel	0808EC201026.ies@ipsacademy.org
Tushar	Ambeldkar	0808EC201027.ies@ipsacademy.org
Yashraj	Upadhyay	0808EC201028.ies@ipsacademy.org
Yashvardhan	Sisodiya	0808EC201029.ies@ipsacademy.org'''


emails = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",mystr)

print(emails)
