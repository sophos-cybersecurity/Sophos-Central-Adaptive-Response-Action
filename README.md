# Sophos-Central-add-on-for-Splunk

This splunk add-on helps you to add/override a [website category](https://docs.sophos.com/central/Partner/help/en-us/central/common/tasks/ConfigureWebsiteList.html) into central tenants from splunk using Sophos Central API. 

Add-on supports an adaptive response action item in Splunk Enterprise Security that you can configure in your corelation search or you can run it as an ad-hoc on any notable that gets triggered in Splunk. It does the same job as if you add a website in sophos central after login.


![website](https://user-images.githubusercontent.com/65529349/125061700-3b220400-e0cb-11eb-9d35-34e845403ee6.png)

# Configuration

To configure this add-on to work, you will need API credentials : Client ID and Client Secret from Sophos Central. Please refer below link on how to generate API credentials for your central account:

https://developer.sophos.com/getting-started-tenant

![image](https://user-images.githubusercontent.com/65529349/125064442-4d517180-e0ce-11eb-91fb-1838f832009d.png)

Sophos Central API has three different type of accoun : Partners, organizations and tenants.  



