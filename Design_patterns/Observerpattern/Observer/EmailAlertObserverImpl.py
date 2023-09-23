from Design_patterns.Observerpattern.Observer.NotificationAlertOberver import NotificationObserver


class EmailAlertObserverImpl(NotificationObserver):
    def __init__(self, email_id, observable):
        self.email_id = email_id
        self.observable = observable

    def update(self):
        self.send_email("product is in stock hurry up")

    def send_email(self, msg):
        print("mail sent to {}".format(self.email_id))


