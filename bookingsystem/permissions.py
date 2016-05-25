from rest_framework import permissions

class IsBookingOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, booking):
        if request.user:
            return booking.booker_of_slot == request.user
        return False
