from rest_framework.response import Response

def api_response(status, message, data=None, status_code=200):
    return Response(
        {
            "status": status,
            "status_code": status_code,
            "message": message,
            "data": data,
        },
        status=status_code,
    )