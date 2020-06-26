import mechanize
br = mechanize.Browerser()
br.set_handle_robots( False )
url = raw_input("Enter URL :" )
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.open(url)
for form in br.forms():
  print form