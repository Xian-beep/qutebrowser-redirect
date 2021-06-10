import qutebrowser.api.interceptor

def rewrite(request: qutebrowser.api.interceptor.Request):
    if request.request_url.host () == 'www.reddit.com':
        request.request_url.setHost ('teddit.net')

        try:
            request.redirect (request.request_url)
        except:
            pass

    if request.request_url.host () == 'www.instagram.com':
        request.request_url.setHost ('bibliogram.snopyta.org')

        try:
            request.redirect (request.request_url)
        except:
            pass

    if request.request_url.host () == 'twitter.com':
        request.request_url.setHost ('nitter.eu')

        try:
            request.redirect (request.request_url)
        except:
            pass

qutebrowser.api.interceptor.register(rewrite)
