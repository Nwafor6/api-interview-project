from django.db import models
from .import utils

# Create your models here.

class Military (models.Model):
	military_status=models.CharField(max_length=50, choices=(("yes","yes"), ("No","No")))
	military_affiliation=models.CharField(max_length=50, choices=(("Air force","Air force"), ("Nevy","Nevy")))
	relationship=models.CharField(max_length=50, choices=(("Single","Single"), ("Married","Married")), blank=True)

	def __str__(self):
		return f"{self.military_affiliation}"


class Prospect (models.Model) :
	gender=models.CharField(max_length=50, choices=(("Female","F"), ("Male","M")))
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	phone=models.PositiveIntegerField()
	phone2=models.PositiveIntegerField()
	address_line1=models.CharField(max_length=100)
	address_line2=models.CharField(max_length=100)
	city=models.CharField(max_length=50, choices=(("Mxcoo","Mxcoo"), ("phoenix","phoenix")))
	state=models.CharField(max_length=50, choices=(("Lasca","Lasca"), ("MMMMMMXXX","MMMMMMXXX")))
	zip_code=models.PositiveIntegerField()
	computer_internet_access=models.CharField(max_length=50, choices=(("yes","yes"), ("no","no")))
	age=models.PositiveIntegerField()
	hsyear=models.DateTimeField()
	current_education_level=models.CharField(max_length=50, choices=(("High School Diploma","High School Diploma"), ("Bachelor Of Science","Bachelor Of Science")))
	preferred_education_level=models.CharField(max_length=50, choices=(("High School Diploma","High School Diploma"), ("Bachelor Of Science","Bachelor Of Science")), null=True, blank=True)
	us_citizen=models.CharField(max_length=50, choices=(("yes","yes"), ("no","no")))
	military=models.ForeignKey(Military, on_delete=models.SET_NULL, null=True, blank=True)
	preferred_enrollment=models.CharField(max_length=10, default="0")
	online_or_campus=models.CharField(max_length=50, choices=(("online","online"), ("campus","campus"),("either","either")))
	ip=models.CharField(max_length=50)


	def __str__(self):
		return f"{self.first_name},{self.last_name}"

class Areas_Of_Interest (models.Model):
	title=models.CharField(max_length=200)

	def __str__(self):
		return self.title
	
class CallCenter (models.Model):
	PublisherBrandName=models.CharField(max_length=200,blank=True)
	callid=models.CharField(max_length=200, default="  ", blank=True)
	sessionid=models.CharField(max_length=200, default="  ", blank=True)
	cc_inbound_transfer_company=models.CharField(max_length=200, default="  ", blank=True)
	cc_inbound_transfer_dba=models.CharField(max_length=200, default="  ", blank=True)
	cc_outbound_company=models.CharField(max_length=200, default="  ", blank=True)
	cc_dba=models.CharField(max_length=200, default="  ",  blank=True)

	def __str__(self):
		return f"{self.callid} callcenter"

class Search (models.Model):
	areas_of_interest=models.ManyToManyField(Areas_Of_Interest)
	can_complete_enrollment=models.CharField(max_length=50, choices=(("yes","yes"), ("no","no")))
	rn_license=models.CharField(max_length=50, choices=(("yes","yes"), ("no","no")))
	teaching_certificate=models.CharField(max_length=50, choices=(("yes","yes"), ("no","no")))
	is_contacted_by_school=models.BooleanField()
	graduated_in_us=models.BooleanField()
	channel_name=models.CharField(max_length=200)
	ss1=models.PositiveIntegerField()
	ss2=models.CharField(max_length=200)
	ss3=models.CharField(max_length=200, default="  ", blank=True)
	ss4=models.CharField(max_length=200, default="  ",blank=True)
	web_url=models.URLField()
	webinitiatingurl=models.URLField()
	traffic_trustedform_url=models.URLField()
	traffic_jornaya_leadid=models.CharField(max_length=200)#use uuid field
	traffic_trustedform_token=models.CharField(max_length=200)#use uuid field
	traffic_category=models.CharField(max_length=50, choices=(("Education","Education"), ("traning","traning")))
	supplier_jornaya_leadid=models.CharField(max_length=200)#use uuid field
	supplier_trustedform_token=models.CharField(max_length=200)#use uuid field
	supplier_trustedform_url=models.URLField()
	time_to_call=models.URLField()
	callcenter=models.ForeignKey(CallCenter, on_delete=models.SET_NULL, null=True, blank=True)
	test_flag=models.PositiveIntegerField()
	tcpa_text=models.CharField(max_length=1000,default="by checking this box, i agree to be contacted by degreesearch and the schools i\\'\''m matched to on the following pages by telephone, which may include artificial or pre-recorded calls and/or sms text messages, delivered via automated technology to the phone number that i have provided above regarding educational opportunities. i also represent that i am the subscriber and primary user of the telephone that i have provided above. i understand that my consent is not required to make a purchase or obtain services and that i may opt-out at any time. in order to proceed without providing consent, call 401-396-0389.")


	def __str__(self):
		return "Search"


class Other_Info (models.Model):
	client_ids=models.CharField(max_length=200, default="  ", blank=True)
	level_of_interest=models.CharField(max_length=200, default="  ", blank=True)
	browser_user_agent=models.CharField(max_length=200, default="  ", blank=True)
	time_zone=models.CharField(max_length=200, default="  ", blank=True)
	device_type=models.CharField(max_length=200, default="  ", blank=True)
	lead_unique_id=models.CharField(max_length=200, default="  ", blank=True)
	web_session_id=models.CharField(max_length=200, default="  ", blank=True)
	site_name=models.CharField(max_length=200, default="  ", blank=True)
	landing_page=models.CharField(max_length=200, default="  ", blank=True)
	supplier_campaign=models.CharField(max_length=200, default="  ", blank=True)
	utm_source=models.CharField(max_length=200, default="  ", blank=True)
	utm_campaign=models.CharField(max_length=200, default="  ", blank=True)
	utm_content=models.CharField(max_length=200, default="  ", blank=True)
	utm_term=models.CharField(max_length=200, default="  ", blank=True)
	utm_supplier_id=models.CharField(max_length=200, default="  ", blank=True)
	utm_sub_id=models.CharField(max_length=200, default="  ", blank=True)
	utm_ad_id=models.CharField(max_length=200, default="  ", blank=True)
	traffic_source_type=models.CharField(max_length=200, default="  ", blank=True)

	def __str__(self):
		return self.landing_page


class SearchConnected(models.Model):
	prospect=models.ForeignKey(Prospect, on_delete=models.CASCADE)
	search=models.ForeignKey(Search, on_delete=models.CASCADE)
	other_info=models.ForeignKey(Other_Info, on_delete=models.CASCADE)

	def __str__(self):
		return f"searching-{self.id}"







