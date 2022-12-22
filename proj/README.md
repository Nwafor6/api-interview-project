models:
prospect:
related {
    military
} 
search:
related{
    area_of_interrest(m2m)
    callcenter,
 

}
other_info


curl --location --request POST 'https://api.cmicon.com/v3/search' \
--data-raw '{
    "accesskey": "e10b29a532-3dd36-d1675-36f4e-87b94",
    "prospect": {
        "gender": "f",
        "first_name": "fname",
        "last_name": "lname",
        "email": "test@gmail.com",
        "phone": "7577741831",
        "phone2": "",
        "address_line1": "961 birch rd",
        "address_line2": "",
        "city": "phoenix",
        "state": "AZ",
        "zip_code": "85005",
        "computer_internet_access": "yes",
        "age": "29",
        "hsyear": 2014,
        "current_education_level": "High School Diploma",
        "preferred_education_level": "",
        "us_citizen": "yes",
        "military": {
            "military_status": "Yes",
            "military_affiliation": "air force",
            "relationship": ""
        },
        "preferred_enrollment": 0,
        "online_or_campus": "either",
        "ip": "172.70.175.21"
    },
    "search": {
        "areas_of_interest": [
            "liberal arts",
            "entertainment"
        ],
        "can_complete_enrollment": "no",
        "rn_license": "no",
        "teaching_certificate": "no",
        "is_contacted_by_school": "0",
        "graduated_in_us": "1",
        "channel_name": "web",
        "ss1": "9829",
        "ss2": "organic",
        "ss3": "",
        "ss4": "",
        "web_url": "https://test.google.com/",
        "webinitiatingurl": "https://test.google.com/workdocs/index.html#/share/document/",
        "traffic_trustedform_url": "http://google.com",
        "traffic_jornaya_leadid": "79d2d183-1012-02cf-6ef5-bf3aaec09570",
        "traffic_trustedform_token": "c52c65236469061b609a1046ec60e5b21b48939f",
        "traffic_category": "education",
        "supplier_jornaya_leadid": "79d2d183-1012-02cf-6ef5-bf3aaec09570",
        "supplier_trustedform_token": "c52c65236469061b609a1046ec60e5b21b48939f",
        "supplier_trustedform_url": "https://cert.trustedform.com/c52c65236469061b609a1046ec60e5b21b48939f",
        "time_to_call": "https://cert.trustedform.com/c52c65236469061b609a1046ec60e5b21b48939f",
        "callcenter": {
            "cc_rep_id": "NA",
            "PublisherBrandName": "NA",
            "callid": "",
            "sessionid": "",
            "cc_inbound_transfer_company": "",
            "cc_dba": "",
            "cc_inbound_transfer_dba": "",
            "cc_outbound_company": ""
        },
        "test_flag": 0,
        "tcpa_text": "by checking this box, i agree to be contacted by degreesearch and the schools i\\'\''m matched to on the following pages by telephone, which may include artificial or pre-recorded calls and/or sms text messages, delivered via automated technology to the phone number that i have provided above regarding educational opportunities. i also represent that i am the subscriber and primary user of the telephone that i have provided above. i understand that my consent is not required to make a purchase or obtain services and that i may opt-out at any time. in order to proceed without providing consent, call 401-396-0389."
    },
    "other_info": {
        "client_ids": "",
        "level_of_interest": "",
        "browser_user_agent": "",
        "time_zone": "",
        "device_type": "",
        "lead_unique_id": "",
        "web_session_id": "",
        "site_name": "edu",
        "landing_page": "grant",
        "supplier_campaign": "web",
        "utm_source": "",
        "utm_medium": "",
        "utm_campaign": "",
        "utm_content": "",
        "utm_term": "",
        "utm_supplier_id": "",
        "utm_sub_id": "",
        "utm_ad_id": "",
        "traffic_source_type": "grant"
    }
}'
