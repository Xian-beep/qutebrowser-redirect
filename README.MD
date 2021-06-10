# redirect.py

## Used for redirecting website X to website Y in qutebrowser.

> I have literally no experiance in coding, what so ever.

As an example, it redirects the following:

	1. reddit.com -> teddit.net
	2. twitter.com -> nitter.eu
	3. instagram.com -> bibliogram.snopyta.org

To use the script, put it in `~/.config/qutebrowser/` and add `config.source('redirect.py')` in your `config.py` .

You can also add more websites by just adding one more if statement below the other ones like so:

```
if request.request_url.host () == 'www.websiteyouwanttoredirect.org':
    request.request_url.setHost ('www.websiteyouwanttouseinstead.net')
	
    try:
	request.redirect (request.request_url)
    except:
	pass
```

I guess it works. ¯\_ (ツ)_/¯
