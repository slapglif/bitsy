import mandrill,time
import requests.packages.urllib3
date = int(time.time())


def drill(subject,body,email):
    try:
        mandrill_client = mandrill.Mandrill('r7F-p7uKBCL5kWBxMf-rhw')
        message = {
         'auto_html': None,
         'auto_text': None,
         'bcc_address': '',
         'from_email': email,
         'from_name': 'Bitsy',
         'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
         'headers': {'Reply-To': email},
         'html': '<p>%s</p>'%body,
         'important': False,
         'inline_css': None,
         'merge': True,
         'merge_language': 'mailchimp',
         'merge_vars': [{'rcpt': "joehoffmans@bitsydroneservices.com",
                         'vars': [{'content': 'merge2 content', 'name': 'merge2'}]}],
         'metadata': {'website': 'www.bitsydroneservices.com'},
         'preserve_recipients': None,
         'return_path_domain': None,
         'signing_domain': None,
         'subject': '%s'%subject,
         'tags': ['application'],
         'to': [{'email': "joehoffmans@bitsydroneservices.com",
                 'type': 'to'}],
         'track_clicks': None,
         'track_opens': None,
         'tracking_domain': None,
         'url_strip_qs': None,
         'view_content_link': None}

        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        print result



    except mandrill.Error, e:
        # Mandrill errors are thrown as exceptions
        print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'


        raise
