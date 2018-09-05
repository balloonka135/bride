from .like import Like


def like(request):
    return {'like_context': Like(request)}
