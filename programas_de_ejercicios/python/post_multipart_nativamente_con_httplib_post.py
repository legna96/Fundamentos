import httplib, mimetypes

def post_multipart(host, uri, fields, files):
  content_type, body = encode_multipart_formdata(fields, files)
  h = httplib.HTTPConnection(host)
  headers = {
    'User-Agent': 'INSERT USERAGENTNAME',
    'Content-Type': content_type
    }
  h.request('POST', uri, body, headers)
  res = h.getresponse()
  print(res.status, res.read())

def encode_multipart_formdata(fields, files):
  """
  fields is a sequence of (name, value) elements for regular form fields.
  files is a sequence of (name, filename, value) elements for data to be uploaded as files
  Return (content_type, body) ready for httplib.HTTP instance
  """
  BOUNDARY = '----------bound@ry_$'
  CRLF = '\r\n'
  L = []
  for (key, value) in fields:
    L.append('--' + BOUNDARY)
    L.append('Content-Disposition: form-data; name="%s"' % key)
    L.append('')
    L.append(value)
  for (key, filename, value) in files:
    L.append('--' + BOUNDARY)
    L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
    L.append('Content-Type: %s' % get_content_type(filename))
    L.append('')
    L.append(value)
  L.append('--' + BOUNDARY + '--')
  L.append('')
  body = CRLF.join(L)
  content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
  return content_type, body

def get_content_type(filename):
  return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

if __name__ == "__main__":
  filename = "C:\Users\pc1\Desktop\data.txt"
  archivo = open(filename, "r")
  post_multipart("localhost:8080", "/hello", [],[("archivo", "data.txt", archivo.read())])
