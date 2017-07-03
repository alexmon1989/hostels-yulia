from booking.models import Booking
from feedbacks.models import Feedback


def get_new_booking_count():
    return Booking.get_new_count()


def get_new_feedbacks_count():
    return Feedback.get_new_count()
