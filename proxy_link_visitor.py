import urllib.request
import sys
import time
from threading import Thread

def proxyFetchPage(proxy, url):
	try:
		try:
			print(proxy, " -> ", url)
			headers={'User-agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A465 Twitter for iPhone BrandVerity/1.0 (http://www.brandverity.com/why-is-brandverity-visiting-me)'}
			headers={'Referer' : 'http://google.com'}
			proxy = {"html":"http://%s" % proxy}
			proxy_support = urllib.request.ProxyHandler(proxy)
			opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler(debuglevel=1))
			urllib.request.install_opener(opener)

			req = urllib.request.Request(url, None, headers)
			html = urllib.request.urlopen(req).read()
		except urllib.request.URLError:
			print("Error grabbing URL");
	finally:
		if html:
			print("%s - Complete" % proxy)
		time.sleep(float(sys.argv[3]))

if(len(sys.argv) < 4):
	print("syntax: %s [proxyfile] [urlfile] [delay]" % sys.argv[0])
	sys.exit()

proxyFile = open(sys.argv[1], 'r')
proxies = []
for proxy in proxyFile:
	proxies.append(proxy.strip())
proxyFile.close()

urlFile = open(sys.argv[2], 'r')
urls = []
for url in urlFile:
	urls.append(url.strip())
urlFile.close()

for currentProxy in proxies:
	for currentURL in urls:
		t = Thread(target=proxyFetchPage, args=(currentProxy,currentURL))
		t.start()
