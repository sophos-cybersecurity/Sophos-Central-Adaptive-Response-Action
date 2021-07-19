# Sophos-Central-add-on-for-Splunk

This splunk add-on helps you to add/override a [website category](https://docs.sophos.com/central/Partner/help/en-us/central/common/tasks/ConfigureWebsiteList.html) into central tenants from splunk using Sophos Central API. 

Add-on supports an adaptive response action item in Splunk Enterprise Security that you can configure in your corelation search or you can run it as an ad-hoc on any notable that gets triggered in Splunk. It works in the similar way as if you add a website in sophos central. 

This add-on is really helpful if you have policies defined in your central tenant based on website category. e.g Adding a policy to block websites that are categorized as **Hacking**, which will block all the websites that are categorzied as Hacking in your Central tenant.

![image](https://user-images.githubusercontent.com/65529349/125061700-3b220400-e0cb-11eb-9d35-34e845403ee6.png)
  
# Configuration

To configure this add-on to work, you will need API credentials : Client ID and Client Secret from Sophos Central. Please refer below link on how to generate API credentials for your central account:

https://developer.sophos.com/getting-started-tenant

![image](https://user-images.githubusercontent.com/65529349/125064442-4d517180-e0ce-11eb-91fb-1838f832009d.png)

Sophos Central API has three different type of accounts : Partners, organizations and tenants.  

* **Partners** :  A partner is a business entity, typically a Distributor, a Value Added Reseller (VAR) or a Managed Service Provider (MSP) that operates within the Sophos sales channel. A partner manages multiple "tenants" and may sell Sophos software and services to multiple "organizations".
    * API Documentation : https://developer.sophos.com/getting-started
* **Organizations** : An organization is a business entity that uses Sophos software and services. An organization has one or more tenants within Sophos Central.
    * API Documentation : https://developer.sophos.com/getting-started-organization
* **Tenant** : A tenant is a collection of "resources" owned by an organization. An organization usually creates tenants for data isolation. They can also create tenants for ease of management. People that work for the organization, the devices they own, the security policies configured by an admin, and the security events generated, are all examples of resources that belong to the tenant.
    * API Documentation https://developer.sophos.com/getting-started-tenant

**TL:DR** : In case of Partner or Organization you might will have more that one Tenant. This Add-on will identify the type of account using [Whoami API](https://developer.sophos.com/docs/whoami-v1/1/routes/get) and will override the category in single or multiple tenanats as per account type.

![Splunk](https://user-images.githubusercontent.com/65529349/126145962-862ca941-c9cc-4a1c-a062-baa75f3fb8f0.png)

![website](https://user-images.githubusercontent.com/65529349/126145968-d288d4b8-5405-41fc-8f38-d788b8f5c04c.png)

