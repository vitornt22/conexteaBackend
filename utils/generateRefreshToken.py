from rest_framework_simplejwt.tokens import RefreshToken

def gerar_tokens_jwt(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
