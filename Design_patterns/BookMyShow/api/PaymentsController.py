class PaymentsController:
    def __init__(self, payments_service, booking_service):
        self.payments_service = payments_service
        self.booking_service = booking_service

    def payment_failed(self, booking_id, user):
        self.payments_service.process_payment_failed(self.booking_service.get_booking(booking_id), user)

    def payment_success(self, booking_id, user):
        self.booking_service.confirm_booking(self.booking_service.get_booking(booking_id), user)
