import subprocess
from functools import cache
import dns.resolver
import requests
import re
import time
import random
import concurrent.futures
import datetime

ascii_image = '''       
                    MAILION APPLICATION
                 ---------contact--------
                   t.me/mailon_official
                 ------EMAIL SORTER------
              '''
print(ascii_image)

number = ''.join([str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) for _ in range(3)])


current_datetime = datetime.datetime.now()

# Format the datetime object to display month, day, and year
formatted_datetime = current_datetime.strftime("%B, %d, %Y")


host_name = ['Microsoft_free', 'office365', 'gmail', 'aol', 'yahoo', 'godaddy',
             'rackspace', 'qq', 'netease_qiye', 'netease', '263', 'aliyun', 'sina',
             'cn_office', 'namecheap', 'networksolutions', 'hinet', 'hibox', 'hiworks',
             'gobizkorea', 'synaq', 'mweb.co.za', '1and1&ionos', 'yandex', 'cn4e',
             'netvigator', 'abchk', 'domainlocalhost', 'comcast', 'arsmtp', 'aruba',
             'daum', 'worksmobile', 't-online', 'agenturserver', 'kasserver', 'protonmail',
             'register.it', 'register.com', 'navermailplug', 'bizmeka', 'mail.ru',
             'global-mail.cn', 'mail.com', 'icloud', 'nominalia', 'rediffmailpro',
             'serviciodecorreo', 'redtailtechnology', 'chinaemail.cn', 'zmail.net.cn',
             'dns.com.cn', 'yunyou', 'fusemail', 'world4you', 'barracuda', 'ukraine',
             'proofpoint', '123-reg', 'strato', 'zoho', 'AppSuit', 'one.com', 'bluehost',
             'eim.ae', 'carrierzone', 'postoffice', 'mimecast', 'at$t', 'ovh', 'gmx',
             'coremail', 'fastmail', 'locaweb', 'hostinger', 'kinghost', 'dreamhost',
             'mandic', 'terra', 'uhserver(uol)', 'spectrum(charter)', 'bbmail', 'udomain',
             'messagelabs', 'combell', 'bigpond', 'chinanetsun', 'spamexperts',
             'HornetSecurity', 'serverdata', 'LCN', 'BSNL', 'Telenet', 'Atmail',
             'Sendgrid', 'Forcepoint', 'AmazonAWS', 'Mailgun', 'cisco', 'communilink',
             'netcore', 'upcmail', 'aweber', 'appliedexch', 'hetemail', 'alpha-mail',
             'alpha-prm', 'sakura', 'conoha', 'kogaya', 'nifty', 'lolipop', 'biglobe',
             'wadax', 'secure.ne.jp', 'xserver', 'cybermail', 'ymc.ne.jp', 'nifcloud',
             'securemx', 'deskwing', 'ocn', 'earthlink', 'interia', 'evolutionserver',
             'stackmail(20i)', 'infomaniak', 'mycloudmailbox', 'stackmail', 'ispgateway',
             'turbo-smtp', 'ziggo.nl', 'tigertech', 'others(mx)', 'others(no_mx)']


@cache
def get_disposable_domains():
    url = 'https://raw.githubusercontent.com/ivolo/disposable-email-domains/master/index.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


@cache
def get_mx_records(email_address):
    domain = email_address.split('@')[1]

    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return [mx.exchange.to_text() for mx in mx_records]
    except dns.resolver.NoAnswer:
        return []


@cache
def check_roundcube(email_text):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(regex, email_text):
        disposable_domains = get_disposable_domains()
        domain_name = email_text.split('@')[1]
        roundcube_hosts = [f'webmail.{domain_name}', f'roundcube.{domain_name}', f'mail.{domain_name}/webmail', f"mail.{domain_name}.",
                           f'email.{domain_name}/roundcube', f'webmail2.{domain_name}', f'mail2.{domain_name}/roundcube',
                           f'webmail3.{domain_name}', f'roundcube2.{domain_name}', f'mail3.{domain_name}/roundcube',
                           f'rc.{domain_name}', f'webmail4.{domain_name}', f'roundcube3.{domain_name}',
                           f'mail4.{domain_name}/roundcube', f'webmail5.{domain_name}', f'roundcube4.{domain_name}',
                           f'mail5.{domain_name}/roundcube', f'webmail6.{domain_name}', f'roundcube5.{domain_name}',
                           f'mail6.{domain_name}/roundcube', f'rc2.{domain_name}', f'webmail7.{domain_name}',
                           f'roundcube6.{domain_name}', f'mail7.{domain_name}/roundcube', f'webmail8.{domain_name}',
                           f'roundcube7.{domain_name}', f'mail8.{domain_name}/roundcube', f'webmail9.{domain_name}',
                           f'roundcube8.{domain_name}', f'mail9.{domain_name}/roundcube', f'rc3.{domain_name}',
                           f'webmail10.{domain_name}', f'roundcube9.{domain_name}', f'mail10.{domain_name}/roundcube',
                           'mx1.cpmx.co.za.', f"{domain_name}.", 'fallbackmx.spamexperts.eu.', 'lastmx.spamexperts.net.',
                           'mx.spamexperts.com.', 'mx4.mtaroutes.com.', 'mx2.mtaroutes.com.', 'mx3.mtaroutes.com.',
                           'mx1.mtaroutes.com.', 'mx2.email-cluster.com.', 'failover1.email-cluster.com.',
                           'mx1.email-cluster.com.', 'mx2.mtaroutes.com.', 'mx4.mtaroutes.com.', 'mx1.mtaroutes.com.',
                           'mx3.mtaroutes.com.', 'email.tadmur.com.', 'lastmx.spamexperts.net.', 'fallbackmx.spamexperts.eu.',
                           'mx.spamexperts.com.', 'mx3-hosting.jellyfish.systems.', 'mx1-hosting.jellyfish.systems.',
                           'mx2-hosting.jellyfish.systems.', 'mx2.krystal.uk.', 'mx1.krystal.uk.', 'mx.stackmail.com.',
                           'mx.stackmail.com.', 'mx-1.mailsafe.email.', 'mx-2.mailsafe.email.', 'mx01.mailcluster.com.au.',
                           'mx02.mailcluster.com.au.', 'mx1.mailsentinel.net.', 'mx2.mailsentinel.net.']

        if domain_name not in disposable_domains:
            mx_records = get_mx_records(email_text)
            print(mx_records)
            for host in roundcube_hosts:
                for item in mx_records:
                    print(f"Sorting {email_text}")
                    if host in item:
                        print(f"{email_text} is RoundCube")
                        try:
                            with open(f'Roundcube-{number}.txt', "a") as file:
                                file.write(f'{email_text}\n')
                        except FileNotFoundError:
                            with open(f'Roundcube-{number}.txt', "w") as file:
                                file.write(f'{email_text}\n')
                        break
                    else:
                        with open(f'others-{number}.txt', "w") as file:
                            file.write(f'{email_text}\n')


@cache
def check_OWA(email_text):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(regex, email_text):
        disposable_domains = get_disposable_domains()
        domain_name = email_text.split('@')[1]
        OWA_hosts = [f'autodiscover.{domain_name}', f'mail.{domain_name}', f'owa.{domain_name}', f'outlook.{domain_name}',
                     f'exchange.{domain_name}', f'webmail.{domain_name}', f'outlookweb.{domain_name}', f'email.{domain_name}',
                     f'mail2.{domain_name}', f'portal.{domain_name}', f'protection.outlook.com', f'mail2.{domain_name}',
                     f'owa2.{domain_name}', f'owa3.{domain_name}', f'email2.{domain_name}', f'portal2.{domain_name}',
                     f'outlook2.{domain_name}', f'exchange2.{domain_name}', f'webmail2.{domain_name}',
                     f'mail3.{domain_name}', f'owa4.domain.com', f'mail4.domain.com/owa', f'webmail3.{domain_name}/owa',
                     f'outlook3.{domain_name}/owa', f'exchange3.{domain_name}/owa', f'portal3.{domain_name}/owa']

        if domain_name not in disposable_domains:
            for host in OWA_hosts:
                mx_records = get_mx_records(email_text)
                for item in mx_records:
                    print(f"Sorting {email_text}")
                    if host in item:
                        print(f"{email_text} is OWA")
                        try:
                            with open(f'OWA-{number}.txt', "a") as file:
                                file.write(f'{email_text}\n')
                        except FileNotFoundError:
                            with open(f'OWA-{number}.txt', "w") as file:
                                file.write(f'{email_text}\n')
                        break
                    else:
                        with open(f'others-{number}.txt', "w") as file:
                            file.write(f'{email_text}\n')

@cache
def sort_other_emails(email_text):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(regex, email_text):
        disposable_domains = get_disposable_domains()
        domain_name = email_text.split('@')[1]
        print(f"Sorting {email_text} in servers list")
        if domain_name not in disposable_domains:
            for host in host_name:
                mx_records = get_mx_records(email_text)

                for item in mx_records:
                    print(f"Sorting {email_text}")
                    if host.lower() in item:
                        print(f"{email_text} is a {host}")
                        try:
                            with open(f'{host}-{number}.txt', "a") as file:
                                file.write(f'{email_text}\n')
                        except FileNotFoundError:
                            with open(f'{host}-{number}.txt', "w") as file:
                                file.write(f'{email_text}\n')
                        break

                    else:
                        with open(f'others-{number}.txt', "w") as file:
                            file.write(f'{email_text}\n')

        else:
            print(f"{email_text} address is DISPOSABLE")

    else:
        print(f"{email_text} is wrongly formatted")

@cache
def check_godaddy(email_text):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(regex, email_text):
        disposable_domains = get_disposable_domains()
        domain_name = email_text.split('@')[1]
        godaddy_hosts = ['pop.secureserver.net', 'imap.secureserver.net','pop.email.secureserver.net',
                         'imap.email.secureserver.net','pop.secureserver.net (alternate server)',
                         'smtpout.secureserver.net (alternate server)', 'pop.protection.outlook.com',
                         'imap.protection.outlook.com', 'smtp.office365.com', 'outlook.office365.com',
                         'mailstore1.secureserver.net', 'smtpout.secureserver.net',
                         'mailstore1.asia.secureserver.net', 'smtp.asia.secureserver.net',
                         'mailstore1.europe.secureserver.net', 'smtp.europe.secureserver.net',
                         'pop.secureserver.net', 'imap.secureserver.net', 'pop.europe.secureserver.net',
                         'imap.europe.secureserver.net', 'pop.asia.secureserver.net', 'imap.asia.secureserver.net',
                         'email.secureserver.net', 'mx.secureserver.net', 'inbound.secureserver.net',
                         'outbound.secureserver.net', 'mailhost.secureserver.net', 'pop.hostedemail.com',
                         'imap.hostedemail.com', 'smtp.hostedemail.com', 'pop.europe.hostedemail.com',
                         'imap.europe.hostedemail.com', 'smtp.europe.hostedemail.com', 'pop.asia.hostedemail.com',
                         'imap.asia.hostedemail.com', 'smtp.asia.hostedemail.com', 'pop.na.hostedemail.com',
                         'imap.na.hostedemail.com', 'smtp.na.hostedemail.com', 'hostedemail']

        if domain_name not in disposable_domains:
            for host in godaddy_hosts:
                print(f"Sorting {email_text} in Godaddy server")
                mx_records = get_mx_records(email_text)
                for item in mx_records:

                    if host in item:
                        print(f"{email_text} is GODADDY")
                        try:
                            with open(f'Godaddy-{number}.txt', "a") as file:
                                file.write(f'{email_text}\n')
                        except FileNotFoundError:
                            with open(f'Godaddy-{number}.txt', "w") as file:
                                file.write(f'{email_text}\n')
                        break
                    else:
                        print(f"{email_text} is not {host}")
                        with open(f'others-{number}.txt', "w") as file:
                            file.write(f'{email_text}\n')

@cache
def check_zimbras(email_text):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(regex, email_text):
        disposable_domains = get_disposable_domains()
        domain_name = email_text.split('@')[1]
        zimbras_hosts = [f'mail.{domain_name}', f'webmail.{domain_name}', f'zimbra.{domain_name}',
                         f'imap.{domain_name}', f'smtp.{domain_name}', f'pop.{domain_name}',
                         f'autodiscover.{domain_name}', f'calendar.{domain_name}',
                         f'contacts.{domain_name}', f'chat.{domain_name}', f'conference.{domain_name}',
                         f'meetings.{domain_name}', f'messenger.{domain_name}', f'webchat.{domain_name}',
                         f'mail2.{domain_name}', f'owa.{domain_name}', f'activesync.{domain_name}', f'admin.{domain_name}',
                         f'config.{domain_name}', f'sync.{domain_name}', f'collaboration.{domain_name}', f'files.{domain_name}',
                         f'docs.{domain_name}', f'drive.{domain_name}', f'groups.{domain_name}', f'lists.{domain_name}',
                         f'notes.{domain_name}', f'tasks.{domain_name}', f'wiki.{domain_name}', f'portal.{domain_name}',
                         f'support.{domain_name}', f'help.{domain_name}', f'kb.{domain_name}', f'service.{domain_name}',
                         f'status.{domain_name}', f'updates.{domain_name}', f'reports.{domain_name}', f'stats.{domain_name}',
                         f'billing.{domain_name}']

        if domain_name not in disposable_domains:
            for host in zimbras_hosts:
                print(f"Sorting {email_text} in Zimbras server")
                mx_records = get_mx_records(email_text)
                for item in mx_records:

                    if host in item:
                        print(f"{email_text} is a {host}")
                        try:
                            with open(f'Zimbras-{number}.txt', "a") as file:
                                file.write(f'{email_text}\n')
                        except FileNotFoundError:
                            with open(f'Zimbras-{number}.txt', "w") as file:
                                file.write(f'{email_text}\n')
                        break
                    else:
                        print(f"{email_text} is not {host}")
                        with open(f'others-{number}.txt', "w") as file:
                            file.write(f'{email_text}\n')


if __name__ == '__main__':
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'),
                             'utf-8').split('\n')[1].strip()

    if current_machine_id == "B222BE53-3CB1-11E8-8536-47D65C0000DA" or \
            current_machine_id == '279D2D42-904E-ABF8-1CCE-DAC290EB3CC3':

        choice = input("Type 1 to check an email, 2 to check file: ")
        if choice == "1":
            email_c = input("Type the email address: ")
            user_input = input("Type 1 for ROUNDCUBE, 2 for OWA, 3 for GODADDY, 4 for zimbras, 5 for others: ")

            if user_input == "1":
                check_roundcube(email_c)
                print("\nTASK COMPLETE")

            elif user_input == "2":
                check_OWA(email_c)
                print("\nTASK COMPLETE")

            elif user_input == "3":
                check_godaddy(email_c)
                print("\nTASK COMPLETE")

            elif user_input == "4":
                check_zimbras(email_c)
                print("\nTASK COMPLETE")

            elif user_input == "5":
                sort_other_emails(email_c)
                print("\nTASK COMPLETE")

            else:
                ascii_image = '''       
                             ------INVALID INPUT------
                                   RUN APP AGAIN
                              '''
                print(ascii_image)
                time.sleep(1000)

        elif choice == '2':
            user_email = input("Please type the file name (e.g. email.txt): ").lower()
            user_input = input("Type 1 for ROUNDCUBE, 2 for OWA, 3 for GODADDY, 4 for others: ")
            if user_input == '1':
                try:
                    with open(f'{user_email}') as file:
                        f = file.readlines()
                    data = list(dict.fromkeys(f))

                    data = [x.strip('\n') for x in data if x.strip()]
                    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                        executor.map(check_roundcube, data)

                    print("\nTASK COMPLETE")
                    time.sleep(1000)
                except Exception as a:
                    print(a)
                    time.sleep(1000)

            elif user_input == '2':
                try:
                    with open(f'{user_email}') as file:
                        f = file.readlines()
                    data = list(dict.fromkeys(f))

                    data = [x.strip('\n') for x in data if x.strip()]
                    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                        executor.map(check_OWA, data)

                    print("\nTASK COMPLETE")
                    time.sleep(1000)
                except Exception as a:
                    print(a)
                    time.sleep(1000)

            elif user_input == '3':
                try:
                    with open(f'{user_email}') as file:
                        f = file.readlines()
                    data = list(dict.fromkeys(f))

                    data = [x.strip('\n') for x in data if x.strip()]
                    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                        executor.map(check_godaddy, data)

                    print("\nTASK COMPLETE")
                    time.sleep(1000)

                except Exception as a:
                    print(a)
                    time.sleep(1000)

            elif user_input == '4':
                try:
                    with open(f'{user_email}') as file:
                        f = file.readlines()
                    data = list(dict.fromkeys(f))

                    data = [x.strip('\n') for x in data if x.strip()]
                    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                        executor.map(check_zimbras, data)

                    print("\nTASK COMPLETE")
                    time.sleep(1000)
                except Exception as a:
                    print(a)
                    time.sleep(1000)

            elif user_input == '5':
                try:
                    with open(f'{user_email}') as file:
                        f = file.readlines()
                    data = list(dict.fromkeys(f))

                    data = [x.strip('\n') for x in data if x.strip()]
                    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                        executor.map(sort_other_emails, data)

                    print("\nTASK COMPLETE")
                    time.sleep(1000)
                except Exception as a:
                    print(a)
                    time.sleep(1000)

            else:
                ascii_image = '''       
                         ------INVALID INPUT------
                               RUN APP AGAIN
                              '''
                print(ascii_image)
                time.sleep(1000)

        else:
            ascii_image = '''       
                         ------INVALID INPUT------
                               RUN APP AGAIN
                          '''
            print(ascii_image)
            time.sleep(1000)
    else:
        ascii_image = '''       
                         ------UNAUTHORIZED USER------
                              Contact @MailionDev
                          '''
        print(ascii_image)
        time.sleep(1000)
