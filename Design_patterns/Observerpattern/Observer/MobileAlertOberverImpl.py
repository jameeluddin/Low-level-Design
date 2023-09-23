from Design_patterns.Observerpattern.Observer.NotificationAlertOberver import NotificationObserver


class MobileAlertObserverImpl(NotificationObserver):
    def __init__(self, username, observable):
        self.username = username
        self.observable = observable

    def update(self):
        self.send_email("product is in stock hurry up")

    def send_email(self, msg):
        print("mail sent to {}".format(self.username))