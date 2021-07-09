
# encoding = utf-8
import json
import re, urllib
import requests


def response(url, resp, helper):
    
    if resp.status_code not in (200, 201, 204):
        helper.log_error('Failed to query api. url={}, HTTP Error={}, content={}'.format(url, resp.status_code, resp.text))
        return json.dumps(None)
    else:
        return resp.content
        
def get_central_token(helper, auth_url, payload):

    resp = requests.post(auth_url, data=payload, verify=False)
    content = response(auth_url, resp,helper)
    x = json.loads(content)
    token = x["access_token"]
    return token
        

def whoami(helper, whoami_url, token):
    
    header = {"Authorization": "Bearer {}".format(token)}

    resp = requests.get(whoami_url, headers=header, verify=False)
    content = response(whoami_url, resp, helper)
    x = json.loads(content)    
    tenant_id = x["id"]
    idType = x["idType"]
    if idType == "tenant":
        dataRegion = x["apiHosts"]["dataRegion"]
        return tenant_id,  idType, dataRegion
    else:
        return tenant_id,  idType, None
        

def list_tenants(helper, idType, token, category_override, enter_urls_domains_tlds_ip_addresses_or_cidr_ranges, comment, tag, tenant_id, list_url):

    idType = idType.title()

    header = {"Authorization": "Bearer {}".format(token),
            "X-{}-ID".format(idType) : "{}".format(tenant_id),
            "Accept" : "application/json",
            "Content-Type": "application/json"}
        
    resp = requests.get(list_url, headers=header, verify=False)
    content = response(list_url, resp, helper)
    x = json.loads(content)
    helper.log_info("list_t={}".format(x))
    for y in range(len(x['items'])):
        tenant_id = x['items'][y]['id']
        dataRegion = x['items'][y]['apiHost']
        name = x['items'][y]['name']
        blockincentral(helper, token, tenant_id, category_override, dataRegion, enter_urls_domains_tlds_ip_addresses_or_cidr_ranges, comment, tag)

        
def blockincentral(helper, token, tenant_id, category_override, dataRegion, enter_urls_domains_tlds_ip_addresses_or_cidr_ranges, comment, tag):
    
    header = {"Authorization": "Bearer {}".format(token),
            "X-Tenant-ID" : "{}".format(tenant_id),
            "Accept" : "application/json",
            "Content-Type": "application/json"}
    payload2={
            "url": enter_urls_domains_tlds_ip_addresses_or_cidr_ranges,
             "tags": [
                    tag
                    ],
            "categoryId": "{}".format(category_override),
            "comment" : "{}".format(comment)
            }
    block_url = "{}/endpoint/v1/settings/web-control/local-sites".format(dataRegion)
    
    resp = requests.post(block_url, json=payload2, headers=header, verify=False)
    content = response(block_url, resp, helper)
    x = json.loads(content)
    helper.log_info("output={}".format(x))


def process_event(helper, *args, **kwargs):
    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example gets the setup parameters and prints them to the log
    client_id = helper.get_global_setting("client_id")
    helper.log_info("client_id={}".format(client_id))
    client_secret = helper.get_global_setting("client_secret")
    helper.log_info("client_secret={}".format(client_secret))

    # The following example gets the alert action parameters and prints them to the log
    enter_urls_domains_tlds_ip_addresses_or_cidr_ranges = helper.get_param("enter_urls_domains_tlds_ip_addresses_or_cidr_ranges")
    helper.log_info("enter_urls_domains_tlds_ip_addresses_or_cidr_ranges={}".format(enter_urls_domains_tlds_ip_addresses_or_cidr_ranges))

    category_override = helper.get_param("category_override")
    helper.log_info("category_override={}".format(category_override))

    tag = helper.get_param("tag")
    helper.log_info("tag={}".format(tag))

    comment = helper.get_param("comment")
    helper.log_info("comment={}".format(comment))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="sample_sourcetype")
    helper.addevent("world", sourcetype="sample_sourcetype")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """
    
    # The following example gets the alert action parameters and prints them to the log
    enter_urls_domains_tlds_ip_addresses_or_cidr_ranges = helper.get_param("enter_urls_domains_tlds_ip_addresses_or_cidr_ranges")
    helper.log_info("enter_urls_domains_tlds_ip_addresses_or_cidr_ranges={}".format(enter_urls_domains_tlds_ip_addresses_or_cidr_ranges))
    category_override = helper.get_param("category_override")
    helper.log_info("category_override={}".format(category_override))
    tag = helper.get_param("tag")
    helper.log_info("tag={}".format(tag))
    comment = helper.get_param("comment")
    helper.log_info("comment={}".format(comment))
   
    helper.log_info("Alert action tines_webhook started.")
    
    auth_url = "https://id.sophos.com/api/v2/oauth2/token"
    whoami_url = "https://api.central.sophos.com/whoami/v1"
    list_url = "https://api.central.sophos.com/organization/v1/tenants"
    
    payload={
            "grant_type": "client_credentials",
            "client_id": helper.get_global_setting("client_id"),
            "client_secret": helper.get_global_setting("client_secret"),
            "scope": "token"
            }
    
    # TODO: Implement your alert action logic here
    token = get_central_token(helper, auth_url, payload)
    tenant_id, idType, dataRegion = whoami(helper, whoami_url, token)
    helper.log_info("idType={}".format(idType))
    
    if idType == "tenant":
        blockincentral(helper,  token, tenant_id, category_override, dataRegion, enter_urls_domains_tlds_ip_addresses_or_cidr_ranges, comment, tag)
    else:
        list_tenants(helper, idType, token, category_override, enter_urls_domains_tlds_ip_addresses_or_cidr_ranges, comment, tag, tenant_id, list_url)
    
    return 0
