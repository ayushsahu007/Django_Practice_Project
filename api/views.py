from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from vegie.models import Receipe
from .serializers import ReceipeSerializer, RegisterSerializer
from .utils import api_response


# ==========================================
# Recipe API
# ==========================================

class ReceipeAPIView(GenericAPIView):

    serializer_class = ReceipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Receipe.objects.filter(user=self.request.user)

    def get_object(self, id):
        return get_object_or_404(self.get_queryset(), id=id)

    # GET (List + Detail)
    def get(self, request, id=None):

        if id:
            serializer = self.get_serializer(self.get_object(id))
            return api_response(
                status=True,
                message="Recipe fetched successfully.",
                data=serializer.data,
                status_code=200,
            )

        serializer = self.get_serializer(
            self.get_queryset(),
            many=True
        )

        return api_response(
            status=True,
            message="Recipes fetched successfully.",
            data=serializer.data,
            status_code=200,
        )

    # POST
    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return api_response(
            status=True,
            message="Recipe created successfully.",
            data=serializer.data,
            status_code=201,
        )

    # PUT
    def put(self, request, id):

        serializer = self.get_serializer(
            self.get_object(id),
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return api_response(
            status=True,
            message="Recipe updated successfully.",
            data=serializer.data,
            status_code=200,
        )

    # PATCH
    def patch(self, request, id):

        serializer = self.get_serializer(
            self.get_object(id),
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return api_response(
            status=True,
            message="Recipe updated successfully.",
            data=serializer.data,
            status_code=200,
        )

    # DELETE
    def delete(self, request, id):

        self.get_object(id).delete()

        return api_response(
            status=True,
            message="Recipe deleted successfully.",
            status_code=200,
        )


# ==========================================
# Register API
# ==========================================

class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return api_response(
                status=True,
                message="User registered successfully.",
                status_code=201,
            )

        return api_response(
            status=False,
            message="Validation failed.",
            data=serializer.errors,
            status_code=400,
        )


# ==========================================
# Login API
# ==========================================

class LoginAPIView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:

            return api_response(
                status=False,
                message="Invalid username or password.",
                status_code=401,
            )

        refresh = RefreshToken.for_user(user)

        return api_response(
            status=True,
            message="Login successful.",
            data={
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status_code=200,
        )